from django.contrib import admin
from riot.models import Places, Profile, RiotPronePlaces, NowRioting

# Register your models here.

admin.site.register(RiotPronePlaces)
admin.site.register(NowRioting)
admin.site.register(Profile)
admin.site.register(Places)
