from django.views import View
from rest_framework import status

from univol.models import Contribution
from rest_framework.response import Response


# Create your views here.

class PredictorView(View):
    def get(self, request):
        volunteer_id = request.GET

        input_prediction_data = [
            [contribution.values()]
            for contribution in Contribution.objects.all()
        ]

        input_prediction_data = pandas.DataFrame(
            input_prediction_data,
            columns=['id_person', 'id_organization', 'id_event']
        )

        prediction = self.make_order(volunteer_id, input_prediction_data)

        if not prediction:
            response = Response(
                {
                    "detail": ("No prediction for this")
                },
                status=status.HTTP_204_NO_CONTENT
            )
            return response

        return Response(
            {
                'prediction_result': prediction,
            },
            status=status.HTTP_200_OK
        )

    def make_order(self, id_person, event_data):
        person_event = event_data[event_data['id_person'] == id_person]
        if len(person_event) == 0:
            # пользователь новый. Рекомендуем ему всё самое популярное
            vivod = list(event_data['id_organization'].value_counts().keys())
        else:
            # Нахожу его последнее участие
            id_organization = list(person_event['id_organization'])[-1]
            # Рекомендую ему
            vivod = self.relevance(id_organization, event_data)
            try:
                pre_vivod = self.relevance(id_organization, event_data)
                print(pre_vivod)
                vivod = list(range(len(pre_vivod)))
                for i in range(len(pre_vivod)):
                    vivod[i] = pre_vivod[i][1]
            except Exception:
                print('Ошибка')
                # vivod = list(event_data['id_organization'].value_counts().keys())
                return None
        return vivod

    # для товара посчитать релевантность всех товаров
    def relevance(self, id_organization, data):
        all_organization = data['id_organization'].unique()
        # all_organization = [i for i in all_organization if i != id_organization]
        len_all = len(all_organization)
        res = list(range(len_all))

        for organization, i in zip(all_organization, range(len_all)):
            res[i] = [self.org_sim(id_organization, organization, data), organization]

        return sorted(res, key=lambda x: x[0], reverse=True)

    # мера сходства между организациями(товарами)
    def org_sim(self, first_org, second_org, data):
        # Множество волонтеров выбравших first
        set_first = set(data[data['id_organization'] == first_org]['id_person'].unique())
        # Множество волонтеров выбравших second
        set_second = set(data[data['id_organization'] == second_org]['id_person'].unique())
        # Множество волонтеров выбравших first_org and second_org
        intersection = set.intersection(set_first, set_second)
        # Множество волонт. выбравших first or second
        union = set.union(set_first, set_second)
        # print(set_second, set_first)
        return len(intersection) / len(union)