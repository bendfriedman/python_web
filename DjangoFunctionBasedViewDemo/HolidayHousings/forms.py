from django import forms
from .models import HolidayHousing


class HolidayHousingForm(forms.ModelForm):

    class Meta:
        model = HolidayHousing

        fields = ['title', 'type', 'costs', 'location', 'rooms', 'specials']

        widgets = {
            'type': forms.Select(choices=HolidayHousing.HousingType),
            'costs': forms.Select(choices=HolidayHousing.CostType),
            'location': forms.Select(choices=HolidayHousing.LocationType),
        }
