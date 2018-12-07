from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# code reference: https://www.youtube.com/watch?v=FdVuKt_iuSI&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=8

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    '''
    :param sender: user
    :param instance: model instance
    :param created: created
    :param kwargs: args
    :return: nothing
    '''
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    '''
    :param sender: user
    :param instance: model instance
    :param kwargs: args
    :return: nothing
    '''
    # saves profile instance
    instance.profile.save()
