from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from decouple import config
from django.core.mail import send_mail


# Create your models here.

class User(AbstractUser):
    full_name = models.CharField(max_length=255)


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    photo = models.ImageField(default='Profiles/default-user.png', upload_to='Profiles', blank=True, null=True)
    profession = models.CharField(max_length=50, null=True)
    about = models.TextField(null=True)
    birthday = models.DateField(null=True)
    twitter = models.URLField(max_length=50, null=True)
    linkedin = models.URLField(max_length=50, null=True)
    facebook = models.URLField(max_length=50, null=True)


    def __str__(self):
        return self.user.username


@receiver(post_save, sender=User)
def email(sender, instance, created, **kwargs):
    if created:
        send_mail('Bienvenido al Blog de Piace',
                  str('Hola ' + instance.full_name + 'Usted se a registrado satisfactoriamente en el BLog'
                                                     'Es un placer que sea parte de nuestra familia'),
                  config('EMAIL_HOST_USER'), [instance.email]

                  )
