from django import forms
from .models import PilatesClass


class PilatesClassForm(forms.ModelForm):

    new_instructor = forms.CharField(
        required=False,
        label="Add New Instructor"
    )

    class Meta:
        model = PilatesClass
        fields = [
            "date",
            "instructor",
            "arms",
            "legs",
            "abs",
            "notes",
        ]