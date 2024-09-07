import requests
from django.http import JsonResponse
from django.http import HttpResponse

def get_odds(request):
    url = "https://api-football-v1.p.rapidapi.com/v2/odds/league/865927/bookmaker/5"
    querystring = {"page": "2"}

    headers = {
        "x-rapidapi-key": "4809c7f7a3msh08a90eff7695782p1fc9c7jsn8deb488de5dc",
        "x-rapidapi-host": "api-football-v1.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    # Si la respuesta es válida, devolvemos los datos JSON
    if response.status_code == 200:
        data = response.json()
        return JsonResponse(data, safe=False)
    else:
        return JsonResponse({"error": "No se pudieron obtener los datos"}, status=response.status_code)
    
    
def home(request):
    return HttpResponse("Bienvenido a la API de Football")