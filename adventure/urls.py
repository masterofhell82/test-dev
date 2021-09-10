from django.urls import path

from adventure import views

# Added url "stop/"
urlpatterns = [
    path("create-vehicle/", views.CreateVehicleAPIView.as_view()),
    path("start/", views.StartJourneyAPIView.as_view()),
    path("stop/", views.StopJourneyAPIView.as_view()),
]
