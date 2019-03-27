from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement
from .models import *



def DisplayRows(request):
    cluster = Cluster(['155.230.91.227'])
    session = cluster.connect('techfossguru')
    rows = session.execute("select * from employee;")
    context = {
        'rows': rows,
    }
    return render(request, 'log_database/index.html', context)

def details(request, emp_id):
    return HttpResponse("You are looking at the employee number " + str(emp_id) + " details")
