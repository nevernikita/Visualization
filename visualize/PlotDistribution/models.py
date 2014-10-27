from django.db import models

# Create your models here.
class RankIndegree(models.Model):
	rank = models.IntegerField(default= 0)
	indegree = models.IntegerField(default= 0)

class RankOutdegree(models.Model):
	rank = models.IntegerField(default= 0)
	outdegree = models.IntegerField(default= 0)

class Edge(models.Model):
	fromNode = models.IntegerField(default= 0)
	toNode = models.IntegerField(default= 0)

class NodeIndegree(models.Model):
	node = models.IntegerField(default= 0)
	indegree = models.IntegerField(default= 0)

class NodeOutdegree(models.Model):
	node = models.IntegerField(default= 0)
	outdegree = models.IntegerField(default= 0)
