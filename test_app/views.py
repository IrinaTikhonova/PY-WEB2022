from random import random
from django.views import View
from django.http import HttpResponse

class RandomNumber(View):
    def get(self, request):
        random_number = random()
        return HttpResponse(random_number)


# Create your views here.
