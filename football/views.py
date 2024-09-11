import requests
from django.http import JsonResponse, HttpResponse

# Vista principal, por ejemplo, para la página de bienvenida
def home(request):
    return HttpResponse("Bienvenido a la API de Football")

# Vista para odds/live
def get_live_odds(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/odds/live"
    
    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)

# Vista para obtener equipos por país
def get_teams_by_country(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/teams/countries"
    
    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)

# Vista para head-to-head de partidos
def get_headtohead_fixtures(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/fixtures/headtohead"
    
    team1 = request.GET.get('team1', 1)  # Parámetro GET para el equipo 1
    team2 = request.GET.get('team2', 2)  # Parámetro GET para el equipo 2
    status = request.GET.get('status', 'FT')  # Estado de los partidos (por defecto: FT - Full Time)
    venue = request.GET.get('venue', 'home')  # Lugar del partido (por defecto: home)

    querystring = {
        "h2h": f"{team1}-{team2}",
        "status": status,
        "venue": venue
    }

    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)

# Vista para obtener datos de lesiones
def get_injuries(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/injuries"
    
    querystring = {
        "league": "39",  # Premier League (ejemplo)
        "season": "2023"  # Temporada actual
    }

    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)

# Vista para obtener jugadores con más tarjetas amarillas
def get_top_yellow_cards(request):
    url = "https://api-football-v1.p.rapidapi.com/v3/players/topyellowcards"
    
    querystring = {
        "league": "39",  # Premier League (ejemplo)
        "season": "2023"  # Temporada actual
    }

    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)
