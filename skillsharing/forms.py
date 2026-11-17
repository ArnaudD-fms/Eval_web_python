from django import forms

from skillsharing.models import HelpRequest


class HelpRequestForm(forms.ModelForm):
    class Meta:
        model = HelpRequest

        fields = ["description", "skill", "start_date", "end_date"]

        widgets = {
            "start_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
            "end_date": forms.DateTimeInput(
                attrs={"type": "datetime-local"},
                format="%Y-%m-%dT%H:%M",
            ),
        }