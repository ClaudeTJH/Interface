from django.urls import path, include

from . import views

urlpatterns = [       
    path('', views.menu, name='menu'), 
    path('sls/', views.sls, name='sls'),
    path('quittance/', views.quittance, name='quittance'),
    path('regularisation/', views.regularisation, name='regularisation'),
    path('relance/', views.relance, name='relance'),
]
