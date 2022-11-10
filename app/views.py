from django.shortcuts import render
import requests
def index(request):
    user_ip = get_client_ip(request)
    info = requests.get(f"http://ip-api.com/json/{user_ip}?fields=status,message,country,countryCode,region,regionName,city,zip,lat,lon,timezone,isp,org,as,query")
    info = info.json()
    return render(request, "index.html", {'ip': info})
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


