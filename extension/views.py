from django.shortcuts import render
from django.views import generic

class ExtensionView(generic.View):
    template_name = "extension/main.html"
    
    def get(self, request):
        return render(request, self.template_name, {})

