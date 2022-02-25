from django.urls import path
# from django.contrib.auth import views as auth_views
# diff app views from django views

from . import views

urlpatterns = [
    path('',views.groups, name='groups'),
    path('<slug:slug>/', views.group, name='group'),
    # slug-type of parameter, slug -name from group views
]