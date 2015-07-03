from django.shortcuts import render
from django.views.generic import TemplateView
# Create your view here.

class SplashView(TemplateView):
	template_name = "index.html"

	
