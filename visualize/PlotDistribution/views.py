from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
	return render(request,"PlotDistribution/index.html", {})

def Plot(request):
	return render(request, "PlotDistribution/Plot.html", {})
def Update(request):
	x = request.GET.get('x',0)
	y = request.GET.get('y',0)
	return HttpResponse(x + ", " + y, content_type="text/plain")

