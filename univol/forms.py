from django import forms

from univol.models import Vacancy


# class VacancyRespondForm(forms.ModelForm):
#     vacancy_name = forms.CharField(max_length=50)
#     date_range = forms.CharField(max_length=21)
#     description = forms.TextInput()
#     # organization = forms.CharField(max_length=30)
#     competitions_keywords = forms.TextInput()
#     event_name = forms.CharField(max_length=1000)
#
#     class Meta:
#         model = Vacancy
#
#         fields = [
#             'vacancy_name',
#             'date_range',
#             'description',
#             'competitions_keywords',
#             'event_name'
#         ]
