from edc_base.model_mixins import ListModelMixin
from edc_base.model_mixins.base_uuid_model import BaseUuidModel


class DeathCauseInfo (ListModelMixin, BaseUuidModel):
    class Meta:
        app_label = "trainee_prn"


class ReasonHospitalized (ListModelMixin, BaseUuidModel):

    class Meta:
        app_label = "trainee_prn"


class CauseCategory (ListModelMixin, BaseUuidModel):

    class Meta:
        app_label = "trainee_prn"
