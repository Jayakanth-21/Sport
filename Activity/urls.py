from django.urls import path

from . import views

urlpatterns = [

    path('', views.HomePageView.as_view(), name='admin page'),
    path('sportlist', views.SportSpecifics.as_view(), name='sportspecifics'),
    path('SportUser', views.CreateUserForm.as_view(), name='userform'),

]


