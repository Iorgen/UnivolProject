from django import forms
from univol.models import Vacancy
import datetime


class AddVacancyForm(forms.ModelForm):
    date_range = forms.DateField(initial=datetime.date.today)

    class Meta:
        model = Vacancy
        fields = ('vacancy_name', 'date_range', 'description',
                  'competitions_keywords', 'event_name', 'organization')