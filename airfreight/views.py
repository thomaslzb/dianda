from django.shortcuts import render


# Create your views here.
# 海运整柜费用查询
from django.views import View

from ocean.models import AmazonPriceModel


class AirfreightInquireView(View):
    def get(self, request):
        amazon_warehouse = AmazonPriceModel.objects.all()

        context = {'amazon_warehouse': amazon_warehouse,
                   }
        return render(request, 'airfreight_inquire.html', context=context, )

    def post(self, request):
        context = {'abc': 'abc'}
        return render(request, 'airfreight_quotation.html', context=context, )

