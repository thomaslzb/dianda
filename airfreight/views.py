import datetime

from django.shortcuts import render


# Create your views here.
# 海运整柜费用查询
from django.views import View
from django.utils.translation import gettext as _

from airfreight.forms import AirFreightForm
from airfreight.models import AirfreightReceiptLocal, AirfreightPrice, AirfreightPostcode, AirfreightPostcodeType, \
    AirfreightItemPrice
from ocean.calculation import get_quote_ref_no
from ocean.models import AmazonPriceModel, ExchangeModel
from utils.tools import format_postcode


class AirfreightInquireView(View):
    def get(self, request):
        amazon_warehouse = AmazonPriceModel.objects.all()
        receipt_area = AirfreightReceiptLocal.objects.all()
        context = {'amazon_warehouse': amazon_warehouse,
                   'receipt_area': receipt_area,
                   }
        return render(request, 'airfreight_inquire.html', context=context, )

    def post(self, request):
        forms = AirFreightForm(request.POST)
        error_string = ""
        if forms.data['delivery_warehouse'] == 'fba':
            if forms.data['fba_code'] == '':
                error_string = _("必须选择派送的FBA仓点")
        else:
            if forms.data['postcode'] == '':
                error_string = _("必须输入需要派送的英国邮编")
            else:
                # 检查是否是合法的英国postcode
                pass

        context = {'forms': 'forms', 'error_string': error_string}
        if forms.is_valid() and not error_string:
            context['air_result'] = calc_airfreight(request, forms)

            return render(request, 'airfreight_quotation.html', context=context, )

        amazon_warehouse = AmazonPriceModel.objects.all()
        receipt_area = AirfreightReceiptLocal.objects.all()
        context = {'amazon_warehouse': amazon_warehouse,
                   'receipt_area': receipt_area,
                   }
        return render(request, 'airfreight_inquire.html', context=context, )


# 判断体积重
def get_weight(weight, volume):
    # 重量和体积比例是w / m = 167:1, 即体积 * 167和实重对比，wm计算值取较大的这一个
    calc_weight = volume * 167
    if calc_weight > weight:
        calc_weight = weight
    if calc_weight < 45:   # 最低计费重量为45kg起
        calc_weight = 45
    return calc_weight


def calc_airfreight(request, forms):
    air_result = {'total_amount': 0}
    # 获取体积重
    air_result['weight'] = float(forms.data['weight'])
    air_result['volume'] = float(forms.data['volume'])
    air_result['calc_weight'] = get_weight(air_result['weight'], air_result['volume'])
    # 获取空运费的单价
    receipt_area = int(forms.data['receipt_area'])
    price_queryset = AirfreightPrice.objects.filter(receipt_area=receipt_area,
                                                    fee_type=1,
                                                    min_weight__lte=air_result['calc_weight'],
                                                    max_weight__gte=air_result['calc_weight'],
                                                    )
    air_price = 0
    if price_queryset:
        air_price = price_queryset[0].price

    postcode = format_postcode(forms.data['postcode'])
    # 是否非FBA地址
    no_fba_fee = 0
    if forms.data['delivery_warehouse'] == 'no_fba':
        # 需要判断 postcode 是否属于 1区， 2区， 还是中心区
        short_postcode = postcode[:-3].strip()
        queryset_london = AirfreightPostcode.objects.filter(begin_code__lte=short_postcode,
                                                            end_code__gte=short_postcode,
                                                            )
        if queryset_london:
            postcode_type = queryset_london[0].postcode_type.type_name
            if postcode_type == 'ZONE2':
                postcode_type_name = 'ZONE2'
            else:
                postcode_type_name = 'LONDON'
        else:
            postcode_type_name = 'ZONE1'
        no_fba_fee = AirfreightPostcodeType.objects.filter(type_name__exact=postcode_type_name)[0].price

    descriptions_magnetic = _('不带磁')
    # 是否带磁
    try:
        magnetic_fee = 0
        if forms.data['magnetic'] == 'on':
            magnetic_fee = AirfreightPrice.objects.filter(code__exact='Magne').first().price
            descriptions_magnetic = _('带磁')
    except:
        magnetic_fee = 0

    # 是否带电
    descriptions_electricity = _('不带电')
    try:
        electricity_fee = 0
        if forms.data['electricity'] == 'on':
            electricity_fee = AirfreightPrice.objects.filter(code__exact='Elect').first().price
            descriptions_electricity = _('带电')
    except:
        electricity_fee = 0

    # 是否有部分液体
    descriptions_liquid = _('不含有液体')
    try:
        liquid_fee = 0
        if forms.data['liquid'] == 'on':
            liquid_fee = AirfreightPrice.objects.filter(code__exact='Liqui').first().price
            descriptions_liquid = _('含部分液体')
    except:
        liquid_fee = 0

    air_result['other_desc'] = descriptions_magnetic + ',' + descriptions_electricity + ',' + descriptions_liquid

    # 空运费的单价及费用
    air_result['air_price'] = air_price + no_fba_fee + magnetic_fee + electricity_fee + liquid_fee
    air_result['airfreight_fee'] = air_result['air_price'] * air_result['calc_weight']
    air_result['total_amount'] += air_result['airfreight_fee']

    # 需要报关品种的数量
    air_result['hs_code_number'] = int(forms.data['hs_code_number'])
    # 获取附加费的单价
    air_result['export_custom'] = air_result['export_custom_extra'] = 0
    air_result['import_custom'] = air_result['import_custom_extra'] = 0
    air_result['export_custom_unit'] = air_result['export_custom_extra_unit'] = ''
    air_result['import_custom_unit'] = air_result['import_custom_extra_unit'] = ''
    air_result['export_custom_extra_total'] = air_result['import_custom_extra_total'] = 0
    item_price_queryset = AirfreightItemPrice.objects.filter(fee_type=2)
    if item_price_queryset:
        for record in item_price_queryset:
            if record.fee_code == 'OUTCU':
                air_result['export_custom'] = record.rate
                air_result['export_custom_unit'] = record.unit
            if record.fee_code == 'OUTEX':
                air_result['export_custom_extra'] = record.rate
                air_result['export_custom_extra_unit'] = record.unit
            if record.fee_code == 'INCU':
                air_result['import_custom'] = record.rate
                air_result['import_custom_unit'] = record.unit
            if record.fee_code == 'INEX':
                air_result['import_custom_extra'] = record.rate
                air_result['import_custom_extra_unit'] = record.unit

    # 国内出口报关费
    air_result['total_amount'] += air_result['export_custom']
    if air_result['hs_code_number'] > 5:
        air_result['export_custom_extra_total'] = (air_result['hs_code_number'] - 5) * air_result['export_custom_extra']
        air_result['total_amount'] += air_result['export_custom_extra_total']

    # 目的地进口报关费
    air_result['total_amount'] += air_result['import_custom']
    if air_result['hs_code_number'] > 5:
        air_result['import_custom_extra_total'] = (air_result['hs_code_number'] - 5) * air_result['import_custom_extra']
        air_result['total_amount'] += air_result['import_custom_extra_total']

    # #  获取汇率
    # qs_exchange_rate = ExchangeModel.objects.first()
    # air_result['exchange_rate'] = qs_exchange_rate.exchange_rate
    # air_result['total_rmb'] = air_result['total_amount'] * air_result['exchange_rate']

    # 获取编号及时间
    air_result['quote_ref_no'] = get_quote_ref_no(request, 'A')
    air_result['quote_time'] = datetime.datetime.strftime(datetime.datetime.now(), "%Y%m%d %H:%M:%S")

    return air_result

