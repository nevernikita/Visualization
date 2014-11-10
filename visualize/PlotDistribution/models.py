from django.db import models

# Create your models here.
class IndegreeCount(models.Model):
	indegree = models.IntegerField(default= 0)
	count = models.IntegerField(default= 0)

class OutdegreeCount(models.Model):
	outdegree = models.IntegerField(default= 0)
	count = models.IntegerField(default= 0)
	
class Edge(models.Model):
	fromNode = models.IntegerField(default= 0, db_index=True)
	toNode = models.IntegerField(default= 0, db_index=True)

class NodeIndegree(models.Model):
	node = models.IntegerField(default= 0)
	indegree = models.IntegerField(default= 0)

class NodeOutdegree(models.Model):
	node = models.IntegerField(default= 0)
	outdegree = models.IntegerField(default= 0)
