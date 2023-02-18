from django.urls import path

from .views import CurrentDateView, HelloWorld, IndexView

urlpatterns = [
   path('datetime/', CurrentDateView.as_view()),
   path('hello/', HelloWorld.as_view()),
   path('', IndexView.as_view()),
]
