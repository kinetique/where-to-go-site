from django import forms


class PlaceForm(forms.Form):
    name = forms.CharField(max_length=100, required=True)
    description = forms.CharField(widget=forms.Textarea, required=True)
    place_type = forms.CharField(max_length=50, required=True)
    location = forms.CharField(max_length=100, required=False)
    rating = forms.IntegerField(min_value=1, max_value=5)
    photo = forms.URLField(required=False)
