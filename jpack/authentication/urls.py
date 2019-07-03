from django.contrib.auth import views as auth_views
from django.urls import path
from .views import (
    ReporterCreateView,

)
app_name = 'authentication'
urlpatterns = [

    path('reporter-create/', ReporterCreateView.as_view(), name='reporter_create'),


]
