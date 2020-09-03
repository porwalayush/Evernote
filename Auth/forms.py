from django.forms import ModelForm
from .models import TODO
class todoform(ModelForm):
    class Meta:
        model= TODO
        fields=['Task','Task_Description','Important']