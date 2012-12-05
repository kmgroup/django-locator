import json

from django.template.response import TemplateResponse
from django.http import HttpResponse

from .models import Location


def locator(request):
    return TemplateResponse(request, 'locator/locator.html')


def locations(request):
    locations = Location.objects.all()
    formatted_locations = []
    count = 1
    for location in locations:
        formatted_locations.append({
            'id': str(count),
            'locname': location.name,
            'lat': location.latitude,
            'lng': location.longitude,
            'address': location.street,
            'address2': '',
            'city': location.city,
            'state': location.state,
            'postal': location.postal,
            'phone': location.phone,
            'web': location.website,
            'hours1': location.hours,
            'hours2': '',
            'hours3': '',
        })
        count += 1
    return HttpResponse(json.dumps(formatted_locations),
                        mimetype='application/json')
