from django.forms import ModelForm
from .models import *

class postjobform(ModelForm):
    class Meta:
        model = postjob
        fields = ['jobname','companyname','package','description','location']
        