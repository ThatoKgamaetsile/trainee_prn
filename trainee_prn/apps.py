from django.apps import AppConfig as DjangoAppConfig
from django.core.management.color import color_style
from trainee_prn import settings
style = color_style()


class AppConfig(DjangoAppConfig):
    name = 'trainee_prn'
    verbose_name = 'trainee prn'
    admin_site_name = 'trainee_prn_admin'

    def ready(self):
        from .models import study_termination_conclusion_on_post_save


if settings.APP_NAME == 'trainee_prn':
    from edc_visit_tracking.apps import (
        AppConfig as BaseEdcVisitTrackingAppConfig)
    from edc_appointment.apps import AppConfig as BaseEdcAppointmentAppConfig
    from edc_appointment.appointment_config import AppointmentConfig

    class EdcAppointmentAppConfig(BaseEdcAppointmentAppConfig):
        default_appt_type = 'clinic'
        configurations = [
            AppointmentConfig(
                model='edc_appointment.appointment',
                related_visit_model='trainee_subject.subjectvisit')
        ]
