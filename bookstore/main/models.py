from django.db import models


class Subscribe(models.Model):
    mail_subscribe = models.EmailField('Пошта', max_length=40)

    def __str__(self):
        return self.mail_subscribe

    class Meta:
        verbose_name = 'підписку'
        verbose_name_plural = 'Підписки'
