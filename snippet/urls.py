from django.urls import path
from snippet import views

urlpatterns = [
    path('', views.SnippetList.as_view()),
    path('snippets/', views.SnippetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view()),
    path('users/', views.UserList.as_view()),
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('teams/', views.TeamList.as_view()),
    path('teams/<int:pk>/', views.TeamDetail().as_view()),
    path('resources/', views.ResourceList.as_view()),
    path('resources/<int:pk>/', views.ResourceDetail.as_view()),
    path('parlinglot/', views.ParkingLotList.as_view()),
    path('parkinglot/<int:pk>/', views.ParkingLotDetails.as_view()),
    path('vehicle/', views.VehicleList.as_view()),
    path('vehicle/<int:pk>/', views.VehicleDetail.as_view())
]
