from django.conf import settings
from django.db import models


# 收货地点
class AirfreightReceiptLocal(models.Model):
    id = models.AutoField(primary_key=True)
    city = models.CharField(max_length=10, null=False, default="", unique=True, verbose_name="city", )
    op_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='op_air_receipt_local',
                                on_delete=models.CASCADE, default=1, verbose_name="Operator")
    op_last_update = models.DateTimeField(auto_now=True, blank=True, verbose_name="Operate Datetime", )

    class Meta:
        db_table = "airfreight_receipt_local"
        verbose_name = "airfreight_receipt_local"
        ordering = ['city', ]


# 空运 postcode 分类 收费列表
class AirfreightPostcodeType(models.Model):
    id = models.AutoField(primary_key=True)
    type_name = models.CharField(max_length=50, null=False, default="", unique=True, verbose_name="en_name", )
    currency = models.CharField(max_length=3, null=False, default="RMB", verbose_name="currency", )
    price = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                                verbose_name='price')
    op_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='op_air_postcode_type',
                                on_delete=models.CASCADE, default=1, verbose_name="Operator")
    op_last_update = models.DateTimeField(auto_now=True, blank=True, verbose_name="Operate Datetime", )

    class Meta:
        db_table = "airfreight_postcode_price"
        verbose_name = "airfreight_postcode_price"
        ordering = ['type_name', ]


# 空运 postcode 分类
class AirfreightPostcode(models.Model):
    id = models.AutoField(primary_key=True)
    postcode_type = models.ForeignKey('AirfreightPostcodeType', to_field='id', verbose_name="postcode_type",
                                      on_delete=models.CASCADE)
    begin_code = models.CharField(max_length=10, null=False, default="", unique=True, verbose_name="begin_code", )
    end_code = models.CharField(max_length=10, null=False, default="", verbose_name="end_code", )
    op_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='op_air_postcode_detail',
                                on_delete=models.CASCADE, default=1, verbose_name="Operator")
    op_last_update = models.DateTimeField(auto_now=True, blank=True, verbose_name="Operate Datetime", )

    class Meta:
        db_table = "airfreight_postcode_detail"
        verbose_name = "ocean_postcode_detail"
        ordering = ['postcode_type', 'begin_code', ]


# 空运费用项目列表
class AirfreightItemPrice(models.Model):
    id = models.AutoField(primary_key=True)
    fee_code = models.CharField(max_length=5, null=False, default="", unique=True, verbose_name="fee_code", )
    en_name = models.CharField(max_length=50, null=False, default="", verbose_name="en_name", )
    cn_name = models.CharField(max_length=50, null=False, default="", verbose_name="cn_name", )
    unit = models.CharField(max_length=20, null=False, default="", verbose_name="unit", )
    rate = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                               verbose_name='rate')
    currency = models.CharField(max_length=3, null=False, default="RMB", verbose_name="currency", )
    minimum_charge = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                                         verbose_name='minimum_charge')
    fee_type = models.IntegerField(default="0", verbose_name="fee_type", )  # 费用类型 0 - 固定费用， 1 - 附加费用
    remark = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="remark", )
    op_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='op_airfreight_item_price',
                                on_delete=models.CASCADE, default=1, verbose_name="Operator")
    op_last_update = models.DateTimeField(auto_now=True, blank=True, verbose_name="Operate Datetime", )

    class Meta:
        db_table = "airfreight_item_price"
        verbose_name = "airfreight_item_price"
        ordering = ['en_name', ]


# 空运收费列表
class AirfreightPrice(models.Model):
    id = models.AutoField(primary_key=True)
    code = models.CharField(max_length=5, null=False, default="", unique=True, verbose_name="code", )
    en_name = models.CharField(max_length=50, null=False, default="", verbose_name="en_name", )
    cn_name = models.CharField(max_length=50, null=False, default="", verbose_name="cn_name", )
    currency = models.CharField(max_length=3, null=False, default="RMB", verbose_name="currency", )
    min_weight = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                                     verbose_name='min_weight')
    max_weight = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                                     verbose_name='max_weight')
    price = models.DecimalField(blank=True, default=0, max_digits=8, decimal_places=2,
                                verbose_name='price')
    fee_type = models.IntegerField(default="0", verbose_name="fee_type", )  # 费用类型 0 - 固定费用， 1 - 附加费用
    remark = models.CharField(max_length=100, default="", blank=True, null=True, verbose_name="remark", )
    op_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='op_airfreight_price',
                                on_delete=models.CASCADE, default=1, verbose_name="Operator")
    op_last_update = models.DateTimeField(auto_now=True, blank=True, verbose_name="Operate Datetime", )

    class Meta:
        db_table = "airfreight_price"
        verbose_name = "airfreight_price"
        ordering = ['code', ]
