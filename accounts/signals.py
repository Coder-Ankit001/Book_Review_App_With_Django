from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        send_mail(
            subject='Welcome to Akashic Records',
            message=f'Hi {instance.username}, welcome to Akashic Records',
            from_email='noreply@akashicrecords.com',
            recipient_list=[instance.email],
            fail_silently=True,
        )

@receiver(post_delete, sender=User)
def delete_user_avatar(sender, instance, **kwargs):
    if instance.avatar:
        instance.avatar.delete(save=False)
