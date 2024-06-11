from django.shortcuts import render
from django.views import generic

# Create your views here.
class ExtensionView(generic.View):
    template_name = "extension/main.html"
    
    def get(self, request):
        context = {}
        return render(request, self.template_name, context)

