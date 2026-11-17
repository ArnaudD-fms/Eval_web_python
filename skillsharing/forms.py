from django import forms

from skillsharing.models import HelpRequest


class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest
        fields = ["description", "skill", "start_date", "end_date"]