from django.db.models.signals import post_save
from django.dispatch import receiver

from .subject_offstudy import SubjectOffstudy


@receiver(post_save, weak=False, sender=SubjectOffstudy,
          dispatch_uid='subject_offstudy_on_post_save')
def study_termination_conclusion_on_post_save(sender, instance, raw, created,
                                              **kwargs):

    if not raw:
        instance.take_off_schedule()
