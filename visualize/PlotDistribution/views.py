from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist  
from django.db.models import F
import PlotDistribution
from PlotDistribution.models import *

# Create your views here.

def home(request):
	return render(request,"PlotDistribution/index.html", {})

def Plot(request):
	return render(request, "PlotDistribution/Plot.html", {})
def Update(request):
	plot = int(request.GET.get('plot',0))
	x = int(request.GET.get('x',0))
	y = int(request.GET.get('y',0))
	print plot, x, y
	resultStr = "";
	if plot == 1:
		print "click on plot 1"
		nodes = NodeIndegree.objects.filter(indegree = x)
		print len(nodes)
		for n in nodes:
			# print n.node
			try:
				correspondingNode = NodeOutdegree.objects.get(node = n.node)
				try:
					outDCount = OutdegreeCount.objects.get(outdegree = correspondingNode.outdegree)
					resultStr = resultStr + str(outDCount.outdegree) + "\t" + str(outDCount.count)+ ";"
				except RankOutdegree.DoesNotExist:
					resultStr = ""
			except NodeOutdegree.DoesNotExist:
				# outdegree = 0
				resultStr = ""
	else:
		print "click on plot 2"
		nodes = NodeOutdegree.objects.filter(outdegree = x)
		print len(nodes)
		for n in nodes:
			# print n.node
			try:
				correspondingNode = NodeIndegree.objects.get(node = n.node)
				try:
					inDCount = IndegreeCount.objects.get(indegree = correspondingNode.indegree)
					resultStr = resultStr + str(inDCount.indegree) + "\t" + str(inDCount.count)+ ";"
				except RankIndegree.DoesNotExist:
					resultStr = ""
			except NodeIndegree.DoesNotExist:
				# indegree = 0
				resultStr = ""
	print resultStr		
	return HttpResponse(resultStr, content_type="text/plain")

