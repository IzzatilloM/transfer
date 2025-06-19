from django.contrib import admin
from django.urls import path
    
from django.conf.urls.static import static
from django.conf import settings
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',IndexView.as_view(),name='index'),
    path('clubs/',ClubsView.as_view(),name='clubs'),
    path('clubs/<int:pk>/',ClubInfoView.as_view(),name='club-info'),
    path('latest-tansfers/', LatestTransfers.as_view(), name='latest-transfers'),
    path('players/', PlayerView.as_view(), name='players'),
    path('playeru20/', PlayerU20View.as_view(), name='playeru20'),
    path('tryouts/',TryoutsView.as_view(),name='tryouts'),
    path('about/',AboutView.as_view(),name='about'),
    path('transfer-records/', TransferRecordsView.as_view(), name='transfer-records'),
    path('stats/', StatsView.as_view(), name='stats'),
    path('stats/top-150-accurate-predictions/', Top15PredictionsView.as_view(), name='top-150-accurate-predictions'),
    path('stats/top-50-expenditure/', Top50ExpenditureView.as_view(), name='top-50-expenditure'),
    path('stats/top-50-incomes/', Top50IncomesView.as_view(), name='top-50-incomes'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

