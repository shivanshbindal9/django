from django.urls import path
from snippet import views

urlpatterns = [
        path('',views.create,name='create'),
        path('view/<int:key>/', views.view ,name='view'),
        ]
