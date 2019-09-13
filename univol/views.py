from django.shortcuts import render, redirect
from django.template.defaulttags import csrf_token

from univol.models import Vacancy, Responds
from users.models import Volunteer


def index(request):
    context = {
        "some_content": 'you you are here'
    }
    return render(request, 'univol/index.html', context)


def home(request):
    context = {
        "some_content": 'you you are here'
    }
    return render(request, 'univol/index.html', context)


def get_vacancies(request):
    if request.method == 'GET':
        vacancies = list(
            vacancy for vacancy in Vacancy.objects.all()
        )
        context = {
            'vacancies': vacancies
        }
        return render(request, 'univol/vacancies.html', context)

    if request.method == 'POST':
        vacancy_id = Vacancy.objects.get(id=request.POST['vacancy_id'])
        org_id = request.POST['organization_id']
        volunteer_id = Volunteer.objects.get(user_id=request.user.id)

        resp = Responds(
            organization_id=3,
            volunteer=volunteer_id,
            vacancy=vacancy_id,
        )
        Responds.objects.get_or_create(organization_id=3, volunteer=volunteer_id, vacancy=vacancy_id)
        return redirect('/vacancies/')


def chat_view(request, responder):
    if request.method == 'GET':
        responds = list(
            Responds.objects.filter(
                volunteer_id=responder,
                organization_id=request.user.id
            ).order_by('send_date')
        )
        context = {
            'messages': responds,
        }
        return render(request, 'univol/responds.html', context)

    reporter_id = request.user.id

