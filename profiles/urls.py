from django.urls import path

from .views import ProfileListView
from . import views

app_name = 'profiles'

urlpatterns = [
    path('', ProfileListView.as_view(), name='list'),
    path('create/', views.profile_create, name='create'),
    path('<int:pk>/edit/', views.profile_edit, name='update'),
    path('<int:pk>/edit/password/', views.admin_edit_password, name='admin_password_update'),
    path('create/group/', views.group_create, name='create_group'),
]
