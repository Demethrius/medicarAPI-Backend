from django.db import models
from django.contrib.auth.models import AbstractUser
  

class User(AbstractUser):
    cliente = models.BooleanField(default=False)

    class Meta:
        verbose_name="Usuário"
        verbose_name_plural="Usuários"
        ordering=['id']

    def __str__(self):
        return self.username

