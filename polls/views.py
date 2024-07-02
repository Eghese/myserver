from django.http import JsonResponse
import requests

def get_client_ip(request):
    ip= 'unknown'
    x_forwarded_for = request.META.get('HTTp_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip=x_forwarded_for.split(',')[0]
    else:
        ip= request.META.get('REMOTE_ADDR')
    return ip

def get_city_by_ip(ip):
 url= f"http://ip-api.com/json/{ip}"
 response = requests.get(url)
 data = response.json()

 if data['status'] == 'success':
    return data['city']
 return 'unknown'

def visitor(request):
   visitor_name = request.GET.get("visitor_name", "Guest")
   client_ip = get_client_ip(request)
   city = get_city_by_ip(client_ip)
   temperature = 11

   response_data = {
      "client_ip": client_ip,
      "location": city,
      "greeting": f"Hello, {visitor_name}!, the temperature is {temperature} degrees Celsius in {city}"

   }
   return JsonResponse(response_data)