import time

from django.shortcuts import render
from django.views import generic

class ExtensionView(generic.View):
    template_name = "extension/main.html"
    
    def get(self, request):
        # Sleep for 3 seconds to simulate lengthy backend processing
        time.sleep(3)
        return render(request, self.template_name, {})

