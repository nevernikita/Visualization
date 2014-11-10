from django.shortcuts import render
from django.http import HttpResponse
from django.db import connections
from django.core.exceptions import ObjectDoesNotExist
from django.db.utils import ConnectionDoesNotExist  
from django.db.models import F
from django.db.models import Q
import PlotDistribution
from PlotDistribution.models import *
from sets import Set
import time
import random

# Create your views here.

def home(request):
	return render(request,"PlotDistribution/index.html", {})

def Plot(request):
	return render(request, "PlotDistribution/Plot.html", {})

def Egonet(request):
	return render(request, "PlotDistribution/Egonet.html", {})

def GetEgonet(request):
	print "enter GetEgonet"
	start_time = time.time()
	resultStr = ""
	nodeid = int(request.GET.get('nodeid',0))
	print nodeid
	outedges = Edge.objects.filter(fromNode = nodeid)
	inedges = Edge.objects.filter(toNode = nodeid)
	nodes = Set([])
	# nodes = Set([nodeid])
	for oe in outedges:
		nodes.add(oe.toNode)
	for ie in inedges:
		nodes.add(ie.fromNode)
	print len(nodes)
	# sample the neighbor
	sampleNum = 10;
	if len(nodes) > sampleNum:
		nodes = random.sample(nodes,sampleNum)
	nodes.append(nodeid)
	validEdges = Edge.objects.filter(fromNode__in=nodes, toNode__in=nodes)
	for e in validEdges:
		resultStr = resultStr + str(e.fromNode) + "\t" + str(e.toNode)+ "\n"
	# for n1 in nodes:
	# 	for n2 in nodes:
	# 		try:
	# 			validedge = Edge.objects.filter(fromNode = n1).get(toNode = n2)
	# 			resultStr = resultStr + str(n1) + "\t" + str(n2)+ "\n"
	# 		except Edge.DoesNotExist:
	# 			# do nothing
	# 			print ""
	print len(resultStr)
	print("--- %s seconds ---" % str(time.time() - start_time))
	return HttpResponse(resultStr, content_type="text/plain")

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

