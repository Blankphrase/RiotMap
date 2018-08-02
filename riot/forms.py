from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from floppyforms.gis import PointWidget, BaseGMapWidget
from riot.models import Places, Profile, RiotPronePlaces, NowRioting

class CustomPointWidget(PointWidget, BaseGMapWidget):
    class Media:
        js = ('/static/floppyforms/js/MapWidget.js',)

class SignUpForm(UserCreationForm):
    username = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=User
        fields=('username','email','password')

    def clean(self):
        cleaned_data = super(SignUpForm, self).clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError(
                "password and confirm_password does not match"
            ) 

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


