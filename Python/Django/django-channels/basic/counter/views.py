import re
from django.shortcuts import render
from django.views import View

# Create your views here.


class Home(View):
    def get(self, request):

        context = {"count": "hello world"}

        return render(
            request=request, template_name="counter/index.html", context=context
        )
