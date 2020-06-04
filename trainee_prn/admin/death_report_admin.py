from django.contrib import admin
from edc_model_admin import audit_fieldset_tuple

from ..admin_site import trainee_prn_admin
from ..forms import SubjectDeathForm
from ..models import DeathReport
from .modeladmin_mixins import ModelAdminMixin


@admin.register(DeathReport, site=trainee_prn_admin)
class DeathReportAdmin(ModelAdminMixin, admin.ModelAdmin):

    form = SubjectDeathForm

    fieldsets = (
        (None, {
            'fields': (
                "subject_identifier",
                "death_date",
                "is_death_date_estimated",
                "death_cause_info",
                "death_cause_info_other",
                "death_cause",
                "death_cause_category",
                "death_cause_other",
                "comment"
            )}),
        audit_fieldset_tuple
    )
    radio_fields = {
        'is_death_date_estimated': admin.VERTICAL,
        'participant_hospitalized': admin.VERTICAL,
    }

    list_display = ('subject_identifier', 'death_date')
    filter_horizontal = (
        'death_cause_info',
        'death_cause_category',
        'death_reason_hospitalized')

    search_fields = ['subject_identifier']
