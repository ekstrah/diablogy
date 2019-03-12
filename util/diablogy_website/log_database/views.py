from django.shortcuts import render
from django.http import HttpResponse
import logging
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement

def index(request):
    return HttpResponse("Hello, world. You're at the index.")
