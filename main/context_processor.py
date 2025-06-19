from .models import *
from django.db.models import Count

def get_countries(request):
    countries = Country.objects.annotate(club_count=Count('club')).filter(club_count__gt=0).order_by('-club_count')

    length = countries.count()

    # if length % 2 == 1:
    #     left_countries = countries[:length // 2 + 1]
    #     right_countries = countries[length // 2 + 1:]
    # else:
    #     left_countries = countries[:length // 2]
    #     right_countries = countries[length // 2:]

    left_countries  = list(countries)[::2]
    rigth_countries = list(countries)[1::2]




    context = {
        'left_countries': left_countries,
        'right_countries': rigth_countries,
    }
    return context


