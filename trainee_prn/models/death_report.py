from django.db import models
from edc_base.model_fields import IsDateEstimatedField
from edc_base.model_fields.custom_fields import OtherCharField
from edc_base.model_mixins.base_uuid_model import BaseUuidModel
from edc_base.model_validators.date import date_not_future
from edc_base.sites.site_model_mixin import SiteModelMixin
from edc_constants.choices import YES_NO
from edc_protocol.validators import date_not_before_study_start

from edc_action_item.model_mixins import ActionModelMixin

from ..action_items import DEATH_REPORT_ACTION
from .list_models import (
    DeathCauseInfo, CauseCategory, ReasonHospitalized)


class DeathReport(SiteModelMixin,
                  ActionModelMixin, BaseUuidModel):

    action_name = DEATH_REPORT_ACTION

    tracking_identifier_prefix = 'DR'

    is_death_date_estimated = IsDateEstimatedField(
        verbose_name='Is date of death estimated?',
        null=True,
        blank=False,
    )

    death_date = models.DateField(
        verbose_name='Date of Death:',
        validators=[
            date_not_before_study_start,
            date_not_future,
        ],
        help_text='',
    )

    death_cause_info = models.ManyToManyField(
        DeathCauseInfo,
        verbose_name='What is the primary source of cause of death '
                     'information? (if multiple source of information, list '
                     'one with the smallest number closest to the top of the '
                     'list) ',
        help_text='',
    )

    death_cause_info_other = OtherCharField(
        verbose_name='if other specify...',
        blank=True,
        null=True,
    )

    death_cause = models.TextField(
        max_length=1000,
        blank=True,
        null=True,
        verbose_name='Describe the major cause of death(including pertinent '
                     'autopsy information if available),starting with the '
                     'first noticeable illness thought to be related to '
                     'death,continuing to time of death. ',
        help_text='Note: Cardiac and pulmonary arrest are not major reasons '
                  'and should not be used to describe major cause)'
    )

    death_cause_category = models.ManyToManyField(
        CauseCategory,
        verbose_name='Based on the above description, what category best '
                     'defines the major cause of death? ',
        help_text='',
    )

    death_cause_other = OtherCharField(
        verbose_name='if other specify...',
        blank=True,
        null=True,
    )

    participant_hospitalized = models.CharField(
        max_length=3,
        choices=YES_NO,
        verbose_name='Was the participant hospitalised before death?',
        help_text='',
    )

    death_reason_hospitalized = models.ManyToManyField(
        ReasonHospitalized,
        verbose_name='if yes, hospitalized, what was the primary '
                     'reason for hospitalisation? ',
        help_text='',
        blank=True,
    )

    days_hospitalized = models.IntegerField(
        verbose_name='For how many days was the participant hospitalised '
                     'during the illness immediately before death? ',
        help_text='in days',
        default=0,
    )

    comment = models.TextField(
        max_length=500,
        verbose_name='Comments',
        blank=True,
        null=True,
    )

    class Meta:
        app_label = 'trainee_prn'
        verbose_name = 'Death Report'
