from django.shortcuts import render
from django.shortcuts import render_to_response
from .email import send_welcome_email
from django.views.generic.edit import FormView
from django.utils import timezone
from django.contrib.gis.geos import Point
from django.contrib.gis.db.models.functions import Distance
from .forms import SignUpForm, PlacesForm, LookupForm, NowForm, ProneForm, ProfileForm
from .models import Places, Profile, RiotPronePlaces, NowRioting
from django.contrib.auth.decorators import login_required
from django.views.generic.base import View
from django.template import RequestContext


# Create your views here.

class LookupView(View):
    form_class = LookupForm

    def get(self, request):
        return render(request, 'riot/lookup.html')

    def form_valid(self, form):
        # Get data
        latitude = form.cleaned_data['latitude']
        longitude = form.cleaned_data['longitude']
        # Get today's date
        now = timezone.now()
        # Get next week's date
        next_week = now + timezone.timedelta(weeks=1)
        # Get Point
        location = Point(longitude, latitude, srid=4326)
        # Look up events
        events = Profile.objects.filter(datetime__gte=now).filter(datetime__lte=next_week).annotate(distance=Distance('venue__location', location)).order_by('distance')[0:5]
        # Render the template
        return render_to_response('riot/lookupresults.html', {
            'events': events
            })


def signUp(request):
    form = SignUpForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['your_name']
            email = form.cleaned_data['email']

            recipient = Profile(username = username,email =email)
            recipient.save()
            send_welcome_email(username,email)

            HttpResponseRedirect('home')
            #.................
    return render(request, 'registration/signUp.html', {"SignUpForm":form})