from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import studentAccount

@receiver(post_save, sender = User)
def create_studentAccount(sender, instance, created, **kwargs):
    if created:
        studentAccount.objects.create(user = instance)
        def ready(self):
            from .signals import create_profile