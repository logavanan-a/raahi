from django.db import models
from master_data.models import BaseContent
from django.contrib.auth.models import User, Group
from master_data.models import *

# Create your models here.
from django.core.validators import RegexValidator

alphanumeric = RegexValidator(
    r'^[0-9a-zA-Z-]*$', 'Only alphanumeric characters are allowed.')


class ReportMeta(BaseContent):
    page_slug = models.CharField(
        max_length=500, blank=True, null=True, validators=[alphanumeric])
    report_slug = models.CharField(
        max_length=500, blank=True, null=True, validators=[alphanumeric], unique=True)
    report_title = models.CharField(max_length=500, blank=True, null=True)
    report_header = models.JSONField(
        blank=True, null=True, help_text="report headers in json format")
    report_query = models.JSONField(
        blank=True, null=True, help_text="sql query and related filter details as json - with keys sqlquery, filters and etc")
    display_order = models.IntegerField(
        blank=True, null=True, help_text="order in which the charts have to be displayed")
    filter_info = models.JSONField(
        blank=True, null=True, help_text="report filters meta data in json format")
    sort_info = models.JSONField(
        blank=True, null=True, help_text="report sort meta data in json format")
    custom_export_header = models.JSONField(
        blank=True, null=True, help_text="custom headers for excel export to handle multilevel headers in json format")

    class Meta:
        verbose_name_plural = "Report Meta"
        ordering = ['display_order']

    def __str__(self):
        return self.report_slug


class MprIndicator(BaseContent):
    category = models.CharField(max_length=150, blank=True, null=True)
    sub_category = models.CharField(max_length=150, blank=True, null=True)
    code = models.IntegerField(default=0)
    ssmis_id = models.PositiveIntegerField(default=0,null=True, blank=True)
    type = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "MPR Indicator"
    
    def __str__(self):
        return self.sub_category

class TruckerMprData(BaseContent):
    mpr_indicator = models.ForeignKey(MprIndicator, on_delete=models.DO_NOTHING, null=True,blank=True)
    partner_id = models.IntegerField(default=0)
    state_id = models.IntegerField(default=0)
    district_id = models.IntegerField(default=0)
    vision_center_id = models.IntegerField(default=0)
    donor_id = models.IntegerField(default=0)
    partner_name = models.CharField(max_length=150, blank=True, null=True)
    vision_center_name = models.CharField(max_length=150, blank=True, null=True)
    donor_name = models.CharField(max_length=150, blank=True, null=True)
    priority = models.IntegerField(default=0)
    indicator_month = models.CharField(max_length=150, blank=True, null=True)
    indicator_year = models.CharField(max_length=150, blank=True, null=True)
    male_target = models.IntegerField(default=0)
    female_target = models.IntegerField(default=0)
    total_target = models.IntegerField(default=0)
    current_month_achievement_male = models.IntegerField(default=0)
    current_month_achievement_female = models.IntegerField(default=0)
    current_month_achievement_total = models.IntegerField(default=0)
    till_date_achievement = models.IntegerField(default=0)
    one_column_value = models.IntegerField(default=0)
    two_column_value = models.IntegerField(default=0)
    three_column_value = models.IntegerField(default=0)
    four_column_value = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Trucker MPR Data"

MPR_STATUS = (
        (0, 'Pending'),
        (1, 'Pending for Approval'),
        (2, 'Zonal Coordinator Approved'),
        (3, 'Zonal Coordinator Rejected'),
        (4, 'PPA Approved'),
        (5, 'PPA Rejected'),
        (6, 'National Coordinator Approved'),
        (7, 'National Coordinator Rejected'),
        (8, 'Super Admin Approved'),
        (9, 'Super Admin Rejected'),
        )

class TruckerMpr(models.Model):
    mpr_month = models.CharField(max_length=150, blank=False, null=False)
    mpr_year = models.CharField(max_length=150, blank=False, null=False)
    vision_center_id = models.IntegerField(null=False)
    vision_center_name = models.CharField(max_length=500, blank=True, null=True)
    ssmis_id = models.IntegerField(default=0, blank=True, null=True)
    partner_id = models.IntegerField(default=0, blank=True, null=True)
    parter_name = models.CharField(max_length=500, blank=True, null=True)
    zone_id = models.IntegerField(default=0, blank=True, null=True)
    zone_name = models.CharField(max_length=500, blank=True, null=True)
    state_id = models.IntegerField(default=0, blank=True, null=True)
    state_name = models.CharField(max_length=500, blank=True, null=True)
    district_id = models.IntegerField(default=0, blank=True, null=True)
    district_name = models.CharField(max_length=500, blank=True, null=True)
    donor_id = models.IntegerField(default=0, blank=True, null=True)
    donor_name = models.CharField(max_length=500, blank=True, null=True)
    camp_id = models.IntegerField(default=0, blank=True, null=True)
    camp_name = models.CharField(max_length=500, blank=True, null=True)
    camp_date = models.DateTimeField(blank=True, null=True)
    i_1_achive_male = models.IntegerField(default=0)
    i_1_achive_female = models.IntegerField(default=0)
    i_1_achive_total = models.IntegerField(default=0)
    i_1_achive_till_date = models.IntegerField(default=0)
    i_1_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_1_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_2_achive_male = models.IntegerField(default=0)
    i_2_achive_female = models.IntegerField(default=0)
    i_2_achive_total = models.IntegerField(default=0)
    i_2_achive_till_date = models.IntegerField(default=0)
    i_2_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_2_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_3_achive_male = models.IntegerField(default=0)
    i_3_achive_female = models.IntegerField(default=0)
    i_3_achive_total = models.IntegerField(default=0)
    i_3_achive_till_date = models.IntegerField(default=0)
    i_3_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_3_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_4_achive_male = models.IntegerField(default=0)
    i_4_achive_female = models.IntegerField(default=0)
    i_4_achive_total = models.IntegerField(default=0)
    i_4_achive_till_date = models.IntegerField(default=0)
    i_4_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_4_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_5_achive_male = models.IntegerField(default=0)
    i_5_achive_female = models.IntegerField(default=0)
    i_5_achive_total = models.IntegerField(default=0)
    i_5_achive_till_date = models.IntegerField(default=0)
    i_5_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_5_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_6_achive_male = models.IntegerField(default=0)
    i_6_achive_female = models.IntegerField(default=0)
    i_6_achive_total = models.IntegerField(default=0)
    i_6_achive_till_date = models.IntegerField(default=0)
    i_6_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_6_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_7_achive_male = models.IntegerField(default=0)
    i_7_achive_female = models.IntegerField(default=0)
    i_7_achive_total = models.IntegerField(default=0)
    i_7_achive_till_date = models.IntegerField(default=0)
    i_7_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_7_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_8_achive_male = models.IntegerField(default=0)
    i_8_achive_female = models.IntegerField(default=0)
    i_8_achive_total = models.IntegerField(default=0)
    i_8_achive_till_date = models.IntegerField(default=0)
    i_8_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_8_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_9_achive_male = models.IntegerField(default=0)
    i_9_achive_female = models.IntegerField(default=0)
    i_9_achive_total = models.IntegerField(default=0)
    i_9_achive_till_date = models.IntegerField(default=0)
    i_9_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_9_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_10_achive_male = models.IntegerField(default=0)
    i_10_achive_female = models.IntegerField(default=0)
    i_10_achive_total = models.IntegerField(default=0)
    i_10_achive_till_date = models.IntegerField(default=0)
    i_10_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_10_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_11_achive_male = models.IntegerField(default=0)
    i_11_achive_female = models.IntegerField(default=0)
    i_11_achive_total = models.IntegerField(default=0)
    i_11_achive_till_date = models.IntegerField(default=0)
    i_11_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_11_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_12_achive_male = models.IntegerField(default=0)
    i_12_achive_female = models.IntegerField(default=0)
    i_12_achive_total = models.IntegerField(default=0)
    i_12_achive_till_date = models.IntegerField(default=0)
    i_12_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_12_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_13_achive_male = models.IntegerField(default=0)
    i_13_achive_female = models.IntegerField(default=0)
    i_13_achive_total = models.IntegerField(default=0)
    i_13_achive_till_date = models.IntegerField(default=0)
    i_13_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_13_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_14_achive_male = models.IntegerField(default=0)
    i_14_achive_female = models.IntegerField(default=0)
    i_14_achive_total = models.IntegerField(default=0)
    i_14_achive_till_date = models.IntegerField(default=0)
    i_14_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_14_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_15_achive_male = models.IntegerField(default=0)
    i_15_achive_female = models.IntegerField(default=0)
    i_15_achive_total = models.IntegerField(default=0)
    i_15_achive_till_date = models.IntegerField(default=0)
    i_15_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_15_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_16_achive_male = models.IntegerField(default=0)
    i_16_achive_female = models.IntegerField(default=0)
    i_16_achive_total = models.IntegerField(default=0)
    i_16_achive_till_date = models.IntegerField(default=0)
    i_16_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_16_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_17_achive_male = models.IntegerField(default=0)
    i_17_achive_female = models.IntegerField(default=0)
    i_17_achive_total = models.IntegerField(default=0)
    i_17_achive_till_date = models.IntegerField(default=0)
    i_17_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_17_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_18_achive_male = models.IntegerField(default=0)
    i_18_achive_female = models.IntegerField(default=0)
    i_18_achive_total = models.IntegerField(default=0)
    i_18_achive_till_date = models.IntegerField(default=0)
    i_18_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_18_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_19_achive_male = models.IntegerField(default=0)
    i_19_achive_female = models.IntegerField(default=0)
    i_19_achive_total = models.IntegerField(default=0)
    i_19_achive_till_date = models.IntegerField(default=0)
    i_19_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_19_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_20_achive_male = models.IntegerField(default=0)
    i_20_achive_female = models.IntegerField(default=0)
    i_20_achive_total = models.IntegerField(default=0)
    i_20_achive_till_date = models.IntegerField(default=0)
    i_20_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_20_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_21_achive_male = models.IntegerField(default=0)
    i_21_achive_female = models.IntegerField(default=0)
    i_21_achive_total = models.IntegerField(default=0)
    i_21_achive_till_date = models.IntegerField(default=0)
    i_21_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_21_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_22_achive_male = models.IntegerField(default=0)
    i_22_achive_female = models.IntegerField(default=0)
    i_22_achive_total = models.IntegerField(default=0)
    i_22_achive_till_date = models.IntegerField(default=0)
    i_22_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_22_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_23_achive_male = models.IntegerField(default=0)
    i_23_achive_female = models.IntegerField(default=0)
    i_23_achive_total = models.IntegerField(default=0)
    i_23_achive_till_date = models.IntegerField(default=0)
    i_23_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_23_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_24_achive_male = models.IntegerField(default=0)
    i_24_achive_female = models.IntegerField(default=0)
    i_24_achive_total = models.IntegerField(default=0)
    i_24_achive_till_date = models.IntegerField(default=0)
    i_24_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_24_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_25_achive_male = models.IntegerField(default=0)
    i_25_achive_female = models.IntegerField(default=0)
    i_25_achive_total = models.IntegerField(default=0)
    i_25_achive_till_date = models.IntegerField(default=0)
    i_25_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_25_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_26_achive_male = models.IntegerField(default=0)
    i_26_achive_female = models.IntegerField(default=0)
    i_26_achive_total = models.IntegerField(default=0)
    i_26_achive_till_date = models.IntegerField(default=0)
    i_26_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_26_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_27_achive_male = models.IntegerField(default=0)
    i_27_achive_female = models.IntegerField(default=0)
    i_27_achive_total = models.IntegerField(default=0)
    i_27_achive_till_date = models.IntegerField(default=0)
    i_27_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_27_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_28_achive_male = models.IntegerField(default=0)
    i_28_achive_female = models.IntegerField(default=0)
    i_28_achive_total = models.IntegerField(default=0)
    i_28_achive_till_date = models.IntegerField(default=0)
    i_28_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_28_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_29_achive_male = models.IntegerField(default=0)
    i_29_achive_female = models.IntegerField(default=0)
    i_29_achive_total = models.IntegerField(default=0)
    i_29_achive_till_date = models.IntegerField(default=0)
    i_29_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_29_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_30_achive_male = models.IntegerField(default=0)
    i_30_achive_female = models.IntegerField(default=0)
    i_30_achive_total = models.IntegerField(default=0)
    i_30_achive_till_date = models.IntegerField(default=0)
    i_30_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_30_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_31_achive_male = models.IntegerField(default=0)
    i_31_achive_female = models.IntegerField(default=0)
    i_31_achive_total = models.IntegerField(default=0)
    i_31_achive_till_date = models.IntegerField(default=0)
    i_31_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_31_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_32_achive_male = models.IntegerField(default=0)
    i_32_achive_female = models.IntegerField(default=0)
    i_32_achive_total = models.IntegerField(default=0)
    i_32_achive_till_date = models.IntegerField(default=0)
    i_32_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_32_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_33_achive_male = models.IntegerField(default=0)
    i_33_achive_female = models.IntegerField(default=0)
    i_33_achive_total = models.IntegerField(default=0)
    i_33_achive_till_date = models.IntegerField(default=0)
    i_33_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_33_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_34_achive_male = models.IntegerField(default=0)
    i_34_achive_female = models.IntegerField(default=0)
    i_34_achive_total = models.IntegerField(default=0)
    i_34_achive_till_date = models.IntegerField(default=0)
    i_34_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_34_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_35_achive_male = models.IntegerField(default=0)
    i_35_achive_female = models.IntegerField(default=0)
    i_35_achive_total = models.IntegerField(default=0)
    i_35_achive_till_date = models.IntegerField(default=0)
    i_35_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_35_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_36_achive_male = models.IntegerField(default=0)
    i_36_achive_female = models.IntegerField(default=0)
    i_36_achive_total = models.IntegerField(default=0)
    i_36_achive_till_date = models.IntegerField(default=0)
    i_36_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_36_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_37_achive_male = models.IntegerField(default=0)
    i_37_achive_female = models.IntegerField(default=0)
    i_37_achive_total = models.IntegerField(default=0)
    i_37_achive_till_date = models.IntegerField(default=0)
    i_37_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_37_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_38_achive_male = models.IntegerField(default=0)
    i_38_achive_female = models.IntegerField(default=0)
    i_38_achive_total = models.IntegerField(default=0)
    i_38_achive_till_date = models.IntegerField(default=0)
    i_38_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_38_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_39_achive_male = models.IntegerField(default=0)
    i_39_achive_female = models.IntegerField(default=0)
    i_39_achive_total = models.IntegerField(default=0)
    i_39_achive_till_date = models.IntegerField(default=0)
    i_39_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_39_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_40_achive_male = models.IntegerField(default=0)
    i_40_achive_female = models.IntegerField(default=0)
    i_40_achive_total = models.IntegerField(default=0)
    i_40_achive_till_date = models.IntegerField(default=0)
    i_40_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_40_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_41_achive_male = models.IntegerField(default=0)
    i_41_achive_female = models.IntegerField(default=0)
    i_41_achive_total = models.IntegerField(default=0)
    i_41_achive_till_date = models.IntegerField(default=0)
    i_41_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_41_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_42_achive_male = models.IntegerField(default=0)
    i_42_achive_female = models.IntegerField(default=0)
    i_42_achive_total = models.IntegerField(default=0)
    i_42_achive_till_date = models.IntegerField(default=0)
    i_42_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_42_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_43_achive_male = models.IntegerField(default=0)
    i_43_achive_female = models.IntegerField(default=0)
    i_43_achive_total = models.IntegerField(default=0)
    i_43_achive_till_date = models.IntegerField(default=0)
    i_43_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_43_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_44_achive_male = models.IntegerField(default=0)
    i_44_achive_female = models.IntegerField(default=0)
    i_44_achive_total = models.IntegerField(default=0)
    i_44_achive_till_date = models.IntegerField(default=0)
    i_44_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_44_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_45_achive_male = models.IntegerField(default=0)
    i_45_achive_female = models.IntegerField(default=0)
    i_45_achive_total = models.IntegerField(default=0)
    i_45_achive_till_date = models.IntegerField(default=0)
    i_45_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_45_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_46_achive_male = models.IntegerField(default=0)
    i_46_achive_female = models.IntegerField(default=0)
    i_46_achive_total = models.IntegerField(default=0)
    i_46_achive_till_date = models.IntegerField(default=0)
    i_46_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_46_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_47_achive_male = models.IntegerField(default=0)
    i_47_achive_female = models.IntegerField(default=0)
    i_47_achive_total = models.IntegerField(default=0)
    i_47_achive_till_date = models.IntegerField(default=0)
    i_47_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_47_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_48_achive_male = models.IntegerField(default=0)
    i_48_achive_female = models.IntegerField(default=0)
    i_48_achive_total = models.IntegerField(default=0)
    i_48_achive_till_date = models.IntegerField(default=0)
    i_48_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_48_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_49_achive_male = models.IntegerField(default=0)
    i_49_achive_female = models.IntegerField(default=0)
    i_49_achive_total = models.IntegerField(default=0)
    i_49_achive_till_date = models.IntegerField(default=0)
    i_49_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_49_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_50_achive_male = models.IntegerField(default=0)
    i_50_achive_female = models.IntegerField(default=0)
    i_50_achive_total = models.IntegerField(default=0)
    i_50_achive_till_date = models.IntegerField(default=0)
    i_50_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_50_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_51_achive_male = models.IntegerField(default=0)
    i_51_achive_female = models.IntegerField(default=0)
    i_51_achive_total = models.IntegerField(default=0)
    i_51_achive_till_date = models.IntegerField(default=0)
    i_51_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_51_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_52_achive_male = models.IntegerField(default=0)
    i_52_achive_female = models.IntegerField(default=0)
    i_52_achive_total = models.IntegerField(default=0)
    i_52_achive_till_date = models.IntegerField(default=0)
    i_52_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_52_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_53_achive_male = models.IntegerField(default=0)
    i_53_achive_female = models.IntegerField(default=0)
    i_53_achive_total = models.IntegerField(default=0)
    i_53_achive_till_date = models.IntegerField(default=0)
    i_53_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_53_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_54_achive_male = models.IntegerField(default=0)
    i_54_achive_female = models.IntegerField(default=0)
    i_54_achive_total = models.IntegerField(default=0)
    i_54_achive_till_date = models.IntegerField(default=0)
    i_54_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_54_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_55_achive_male = models.IntegerField(default=0)
    i_55_achive_female = models.IntegerField(default=0)
    i_55_achive_total = models.IntegerField(default=0)
    i_55_achive_till_date = models.IntegerField(default=0)
    i_55_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_55_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_56_achive_male = models.IntegerField(default=0)
    i_56_achive_female = models.IntegerField(default=0)
    i_56_achive_total = models.IntegerField(default=0)
    i_56_achive_till_date = models.IntegerField(default=0)
    i_56_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_56_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_57_achive_male = models.IntegerField(default=0)
    i_57_achive_female = models.IntegerField(default=0)
    i_57_achive_total = models.IntegerField(default=0)
    i_57_achive_till_date = models.IntegerField(default=0)
    i_57_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_57_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_58_achive_male = models.IntegerField(default=0)
    i_58_achive_female = models.IntegerField(default=0)
    i_58_achive_total = models.IntegerField(default=0)
    i_58_achive_till_date = models.IntegerField(default=0)
    i_58_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_58_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_59_achive_male = models.IntegerField(default=0)
    i_59_achive_female = models.IntegerField(default=0)
    i_59_achive_total = models.IntegerField(default=0)
    i_59_achive_till_date = models.IntegerField(default=0)
    i_59_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_59_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_60_achive_male = models.IntegerField(default=0)
    i_60_achive_female = models.IntegerField(default=0)
    i_60_achive_total = models.IntegerField(default=0)
    i_60_achive_till_date = models.IntegerField(default=0)
    i_60_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_60_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_61_achive_male = models.IntegerField(default=0)
    i_61_achive_female = models.IntegerField(default=0)
    i_61_achive_total = models.IntegerField(default=0)
    i_61_achive_till_date = models.IntegerField(default=0)
    i_61_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_61_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_62_achive_male = models.IntegerField(default=0)
    i_62_achive_female = models.IntegerField(default=0)
    i_62_achive_total = models.IntegerField(default=0)
    i_62_achive_till_date = models.IntegerField(default=0)
    i_62_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_62_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_63_achive_male = models.IntegerField(default=0)
    i_63_achive_female = models.IntegerField(default=0)
    i_63_achive_total = models.IntegerField(default=0)
    i_63_achive_till_date = models.IntegerField(default=0)
    i_63_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_63_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_64_achive_male = models.IntegerField(default=0)
    i_64_achive_female = models.IntegerField(default=0)
    i_64_achive_total = models.IntegerField(default=0)
    i_64_achive_till_date = models.IntegerField(default=0)
    i_64_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_64_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_65_achive_male = models.IntegerField(default=0)
    i_65_achive_female = models.IntegerField(default=0)
    i_65_achive_total = models.IntegerField(default=0)
    i_65_achive_till_date = models.IntegerField(default=0)
    i_65_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_65_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_66_achive_male = models.IntegerField(default=0)
    i_66_achive_female = models.IntegerField(default=0)
    i_66_achive_total = models.IntegerField(default=0)
    i_66_achive_till_date = models.IntegerField(default=0)
    i_66_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_66_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_67_achive_male = models.IntegerField(default=0)
    i_67_achive_female = models.IntegerField(default=0)
    i_67_achive_total = models.IntegerField(default=0)
    i_67_achive_till_date = models.IntegerField(default=0)
    i_67_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_67_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_68_achive_male = models.IntegerField(default=0)
    i_68_achive_female = models.IntegerField(default=0)
    i_68_achive_total = models.IntegerField(default=0)
    i_68_achive_till_date = models.IntegerField(default=0)
    i_68_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_68_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_69_achive_male = models.IntegerField(default=0)
    i_69_achive_female = models.IntegerField(default=0)
    i_69_achive_total = models.IntegerField(default=0)
    i_69_achive_till_date = models.IntegerField(default=0)
    i_69_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_69_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_70_achive_male = models.IntegerField(default=0)
    i_70_achive_female = models.IntegerField(default=0)
    i_70_achive_total = models.IntegerField(default=0)
    i_70_achive_till_date = models.IntegerField(default=0)
    i_70_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_70_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_71_achive_male = models.IntegerField(default=0)
    i_71_achive_female = models.IntegerField(default=0)
    i_71_achive_total = models.IntegerField(default=0)
    i_71_achive_till_date = models.IntegerField(default=0)
    i_71_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_71_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_72_achive_male = models.IntegerField(default=0)
    i_72_achive_female = models.IntegerField(default=0)
    i_72_achive_total = models.IntegerField(default=0)
    i_72_achive_till_date = models.IntegerField(default=0)
    i_72_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_72_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_73_achive_male = models.IntegerField(default=0)
    i_73_achive_female = models.IntegerField(default=0)
    i_73_achive_total = models.IntegerField(default=0)
    i_73_achive_till_date = models.IntegerField(default=0)
    i_73_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_73_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_74_achive_male = models.IntegerField(default=0)
    i_74_achive_female = models.IntegerField(default=0)
    i_74_achive_total = models.IntegerField(default=0)
    i_74_achive_till_date = models.IntegerField(default=0)
    i_74_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_74_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_75_achive_male = models.IntegerField(default=0)
    i_75_achive_female = models.IntegerField(default=0)
    i_75_achive_total = models.IntegerField(default=0)
    i_75_achive_till_date = models.IntegerField(default=0)
    i_75_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_75_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_76_achive_male = models.IntegerField(default=0)
    i_76_achive_female = models.IntegerField(default=0)
    i_76_achive_total = models.IntegerField(default=0)
    i_76_achive_till_date = models.IntegerField(default=0)
    i_76_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_76_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_77_achive_male = models.IntegerField(default=0)
    i_77_achive_female = models.IntegerField(default=0)
    i_77_achive_total = models.IntegerField(default=0)
    i_77_achive_till_date = models.IntegerField(default=0)
    i_77_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_77_metric_code = models.IntegerField(default=0, blank=True, null=True)
    i_78_achive_male = models.IntegerField(default=0)
    i_78_achive_female = models.IntegerField(default=0)
    i_78_achive_total = models.IntegerField(default=0)
    i_78_achive_till_date = models.IntegerField(default=0)
    i_78_indi_code = models.IntegerField(default=0, blank=True, null=True)
    i_78_metric_code = models.IntegerField(default=0, blank=True, null=True)
    # i_79_achive_male = models.IntegerField(default=0)
    # i_79_achive_female = models.IntegerField(default=0)
    # i_79_achive_total = models.IntegerField(default=0)
    # i_79_achive_till_date = models.IntegerField(default=0)
    # i_79_indi_code = models.IntegerField(default=0, blank=True, null=True)
    # i_79_metric_code = models.IntegerField(default=0, blank=True, null=True)
    mpr_status = models.IntegerField(choices=MPR_STATUS,default=0)
    
    class Meta:
        verbose_name_plural = "Trucker Mpr"


class ReportExport(BaseContent):
    DOWNLOAD_CHOICES = (
        (1, 'No'),
        (2, 'Yes')
    )
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    report = models.ForeignKey(ReportMeta, on_delete=models.DO_NOTHING)
    downloaded_at = models.DateTimeField(auto_now_add=True)
    export_status = models.IntegerField(choices=DOWNLOAD_CHOICES)

    class Meta:
        verbose_name_plural = "Report Export"

    def __str__(self):
        return f"{self.user.username} downloaded data at {self.downloaded_at}" 
    
class ReportTracket(BaseContent):
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING)
    year = models.IntegerField(default=0)
    code = models.IntegerField(default=0)
    tracket_col_1 =  models.IntegerField(default=0)
    tracket_col_2 =  models.IntegerField(default=0)


class MprStatusUpdate(BaseContent):
    month = models.IntegerField()
    year = models.IntegerField()
    partner = models.ForeignKey(Partner, on_delete=models.DO_NOTHING, blank=True, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True)
    forward_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='forward_by')
    forward_to_super_admin_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='forward_to_super_admin_by')
    ssims_user = models.ForeignKey(User, on_delete=models.DO_NOTHING, blank=True, null=True, related_name='ssims_user')
    mpr_report_code = models.PositiveIntegerField()    
    mpr_status = models.IntegerField(choices=MPR_STATUS,default=0)
    remark = models.TextField(blank=True, null=True)
    forward_nc_command = models.TextField(blank=True, null=True)
    national_remark = models.TextField(blank=True, null=True)
    super_admin_remark = models.TextField(blank=True, null=True)
    partner_date = models.DateTimeField(null=True, blank=True)
    zonal_coordinator_date = models.DateTimeField(null=True, blank=True)
    ppa_date = models.DateTimeField(null=True, blank=True)
    national_coordinator_date = models.DateTimeField(null=True, blank=True)
    super_admin_date = models.DateTimeField(null=True, blank=True)
    def __str__(self):
        return self.created_by.username
    
   






    