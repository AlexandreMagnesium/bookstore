from .models import Subscribe
from django.forms import ModelForm, TextInput, Textarea


class SubscribeForm(ModelForm):
    class Meta:
        model = Subscribe
        fields = ["mail_subscribe"]
        widgets = {
            "mail_subscribe": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введіть свою пошту'
            }),
        }
