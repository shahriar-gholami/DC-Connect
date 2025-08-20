from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from . models import *

# Create your views here.

class IndexView(LoginRequiredMixin, View):
    template_name = 'info/index.html'

    def get(self, request):

        routes = Route.objects.all()

        return render(request, self.template_name, {'routes':routes})