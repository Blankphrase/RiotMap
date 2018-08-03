from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from floppyforms.gis import PointWidget, BaseGMapWidget
from riot.models import Places, Profile, RiotPronePlaces, NowRioting
from django.forms import Form, FloatField
class LookupForm(Form):
    latitude = FloatField()
    longitude = FloatField()

class CustomPointWidget(PointWidget, BaseGMapWidget):
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
 
class PlacesForm(ModelForm):
    class Meta:
        model = Places
        fields = ['name', 'location']
        widgets = {
            'location': CustomPointWidget()
        }

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['user', 'place']
        widgets = {
            'place': CustomPointWidget()
        }

class ProneForm(ModelForm):
    class Meta:
        model = RiotPronePlaces
        fields = ['place']
        widgets = {
            'place': CustomPointWidget()
        }

class NowForm(ModelForm):
    class Meta:
        model = NowRioting
        fields = [ 'place']
        widgets = {
            'place': CustomPointWidget()
        }


