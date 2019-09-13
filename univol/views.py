from django.shortcuts import render

# Create your views here.
# @login_required
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


def chat_view(request, responder):
    if request.method == 'GET':
        responds = list(
            Responds.objects.filter(
                volunteer_id=responder,
                organization_id=request.user.id
            ).order_by('send_date')
        )
        volunteers = Volunteer.objects.
        context = {
            'messages': responds,
        }
        return render(request, 'univol/responds.html', context)

    reporter_id = request.user.id

