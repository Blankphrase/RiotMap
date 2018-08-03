from django.conf.urls import url
from . import views
from .views import LookupView

urlpatterns = [
    url(r'^accounts/register/', views.signUp, name='signUp'),
    url(r'', LookupView.as_view(), name='lookup'),
]
