from django.shortcuts import render, get_object_or_404, redirect

from places.forms import PlaceForm
from places.models import Place
import random


def index(request):
    place_ids = request.session.get('place_ids', [])
    places = Place.objects.filter(id__in=place_ids)
    selected_place = None
    if places.exists():
        selected_place = get_place(places)

    return render(request, 'places/index.html', {'selected_place': selected_place})


def places_list(request):
    place_ids = request.session.get('place_ids', [])
    places = Place.objects.filter(id__in=place_ids).order_by('-created_at')
    return render(request, 'places/places_list.html', {'places': places})


def place_detail(request, pk):
    place_ids = request.session.get('place_ids', [])
    place = get_object_or_404(Place, pk=pk, id__in=place_ids)
    return render(request, 'places/place_detail.html', {'place': place})


def add_place(request):
    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            place = Place.objects.create(
                name=form.cleaned_data['name'],
                description=form.cleaned_data['description'],
                place_type=form.cleaned_data['place_type'],
                location=form.cleaned_data['location'],
                rating=form.cleaned_data['rating'],
                photo=form.cleaned_data['photo'],
            )

            place_ids = request.session.get('place_ids', [])
            place_ids.append(place.id)
            request.session['place_ids'] = place_ids

            return redirect('places_list')
    else:
        form = PlaceForm()
    return render(request, 'places/add_place.html', {'form': form})


def get_place(places):
    weighted_list = []
    for place in places:
        if place.rating == 5:
            weighted_list.append(60)
        elif place.rating == 4:
            weighted_list.append(20)
        elif place.rating == 3:
            weighted_list.append(10)
        elif place.rating == 2:
            weighted_list.append(7)
        elif place.rating == 1:
            weighted_list.append(3)
        else:
            weighted_list.append(1)
    return random.choices(places, weights=weighted_list, k=1)[0]
