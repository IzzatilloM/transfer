from django.db.models import F, FloatField, ExpressionWrapper, Sum, Value
from django.db.models.functions import Abs,Round,Coalesce
from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import *

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

class ClubsView(View):
    def get(self,request):
        clubs = Club.objects.all()

        country = request.GET.get('country')
        if country is not None:
            clubs = clubs.filter(country__id=country)
        context = {
            'clubs':clubs
        }
        return render(request,'clubs.html',context)

class ClubInfoView(View):
    def get (self,request,pk):
        club = get_object_or_404(Club, id=pk)
        players = club.player_set.order_by('-price')
        context = {
            'club':club,
            'players':players
        }
        return render(request,'club-info.html',context)

class LatestTransfers(View):
    def get(self,request):
        transfers = Transfer.objects.filter(season=Season.objects.last()).order_by('-price')
        context = {
            'transfers':transfers
        }
        return render(request,'latest-transfers.html',context)



class PlayerView(View):
    def get(self,request):
        players = Player.objects.all().order_by('-price')
        context = {
            'players':players
        }
        return render(request,'players.html',context)

class PlayerU20View(View):
    def get(self, req):
        players = Player.objects.filter(age__lte=20)
        context = {
            'players': players
        }
        return render(req, 'U-20 players.html', context)


class TryoutsView(View):
    def get(self, req):
        return render(req, 'tryouts.html')


class AboutView(View):
    def get(self, req):
        return render(req, 'about.html')

class TransferRecordsView(View):
    def get(self, req):
        transfers = Transfer.objects.order_by('-price')
        context = {
            'transfers': transfers
        }
        return render(req, 'stats/transfer-records.html', context)


class StatsView(View):
    def get(self, req):
        return render(req, 'stats.html')


class Top15PredictionsView(View):
    def get(self, request):
        transfers = Transfer.objects.annotate(
            price_diff=Round(
                ExpressionWrapper(
                    Abs(F('price') - F('price_tft')) / F('price') * 100,
                    output_field=FloatField()
                ),
                precision=2
            )
        ).order_by('-price_diff')[:150]
        context = {
            'transfers': transfers
        }
        return render(request, 'stats/150-accurate-predictions.html', context)


class Top50ExpenditureView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_expend=Coalesce(
            Sum('income_transfers__price'),
                Value(0.0)
            )
        ).order_by('-total_expend')[:50]
        context = {
            'clubs': clubs,
        }

        return render(request, 'stats/top-50-clubs-expenditure.html', context)



class Top50IncomesView(View):
    def get(self, request):
        clubs = Club.objects.annotate(
            total_income=Coalesce(
                Sum('expenditure_transfers__price'),
                Value(0.0)
            )
        ).order_by('-total_income')[:50]
        context = {
            'clubs': clubs,
        }

        return render(request, 'stats/top-50-clubs-income.html', context)