from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement
from .models import *
from .forms import *



#Webpages
def insert(request):
    return render(request, 'log_database/insert.html')

#Connects to each keyspace then sends it to webpage
def DisplayRows(request):
    cluster = Cluster(['155.230.91.227'])
    session = cluster.connect('techfossguru')
    rows = session.execute("select * from employee;")
    
    session = cluster.connect('beta')
    fullstack = session.execute("select * from fullstack limit 10;")
    teststack = session.execute("select * from teststack;")
    context = {
        'rows': rows,
        'fullstack': fullstack,
        'teststack': teststack,
    }
    return render(request, 'log_database/index.html', context)


def newQuery(request):
    if request.method == 'POST':
        form = InsertQuery(request.POST)
        if form.is_valid():
            new_query = form.save()
            return HttpResponseRedirect('../')
    else:
        form = InsertQuery()
    return render(request, 'log_database/insert.html', {'form': form })

def details(request, emp_id):
    return HttpResponse("You are looking at the employee number " + str(emp_id) + " details")
