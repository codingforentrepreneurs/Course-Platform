from django.shortcuts import render

def home_view(request, *args, **kwargs):
    template_name = "home.html"
    return render(request, template_name)