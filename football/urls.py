from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('odds/live/', views.get_live_odds, name='get_live_odds'),
    path('teams/countries/', views.get_teams_by_country, name='get_teams_by_country'),
    path('fixtures/headtohead/', views.get_headtohead_fixtures, name='get_headtohead_fixtures'),
    path('injuries/', views.get_injuries, name='get_injuries'),
    path('players/topyellowcards/', views.get_top_yellow_cards, name='get_top_yellow_cards'),
]
