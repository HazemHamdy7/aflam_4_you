from django.shortcuts import render
from django.views import View


# Create your views here.


def Home(request):
    # def get(self, request, *args, **kwargs):

    return render(request, 'aflam_app/index.html')
