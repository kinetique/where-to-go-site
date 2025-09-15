from django.shortcuts import render, get_object_or_404

from places.models import Place


def index(request):
    place_ids = request.session.get('place_ids', [])
    places = Place.objects.filter(id__in=place_ids)
    selected_place = None
    return render(request, 'places/index.html', {'selected_place': selected_place})


def places_list(request):
    place_ids = request.session.get('place_ids', [])
    places = Place.objects.filter(id__in=place_ids).order_by('-created_at')
    return render(request, 'places/places_list.html', {'places': places})


def places_details(request):
    place_ids = request.session.get('place_ids', [])
    place = get_object_or_404(Place, id__in=place_ids)
    return render(request, 'places/place_detail.html', {'place': place})


def add_place(request):
    return
