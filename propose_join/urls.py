from django.urls import path
from . import views

app_name= "propose_join"    
urlpatterns=[
    path('button', views.ProposedClubForm, name='button'),

]
