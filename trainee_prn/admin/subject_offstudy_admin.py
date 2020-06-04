from django.contrib import admin
from edc_base.modeladmin_mixins import audit_fieldset_tuple

from ..admin_site import trainee_prn_admin
from ..forms import SubjectOffStudyForm
from ..models import SubjectOffstudy
from .modeladmin_mixins import ModelAdminMixin


@admin.register(SubjectOffstudy, site=trainee_prn_admin)
class SubjectOffStudyAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectOffStudyForm

    fieldsets = (
        (None, {
            'fields': [
                'subject_identifier',
                'report_datetime',
                'offstudy_date',
                'reason',
                'reason_other',
                'comment']}
         ), audit_fieldset_tuple)

    radio_fields = {
        'reason': admin.VERTICAL,
    }

    search_fields = ['subject_identifier']

    list_display = ('subject_identifier', 'offstudy_date')
