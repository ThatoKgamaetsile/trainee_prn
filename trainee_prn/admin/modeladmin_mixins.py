# from django.contrib import admin
# from django.urls.base import reverse
# from django.urls.exceptions import NoReverseMatch
from django_revision.modeladmin_mixin import ModelAdminRevisionMixin
from edc_base.modeladmin_mixins import (
    ModelAdminNextUrlRedirectMixin, ModelAdminFormInstructionsMixin,
    ModelAdminFormAutoNumberMixin, ModelAdminAuditFieldsMixin,
    ModelAdminReadOnlyMixin, ModelAdminInstitutionMixin,
    FormAsJSONModelAdminMixin, ModelAdminRedirectOnDeleteMixin)
# from edc_fieldsets import FieldsetsModelAdminMixin
# from edc_visit_tracking.modeladmin_mixins import (
#    CrfModelAdminMixin as VisitTrackingCrfModelAdminMixin)


class ModelAdminMixin(ModelAdminNextUrlRedirectMixin,
                      ModelAdminFormInstructionsMixin,
                      ModelAdminFormAutoNumberMixin, ModelAdminRevisionMixin,
                      ModelAdminAuditFieldsMixin, ModelAdminReadOnlyMixin,
                      ModelAdminInstitutionMixin):

    list_per_page = 10

    empty_value_display = '-'
