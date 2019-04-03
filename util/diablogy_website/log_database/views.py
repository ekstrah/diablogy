from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.views.generic import ListView,CreateView,UpdateView
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement
from .models import *
from .forms import *



#Webpages
def home(request):
    return render(request, 'index.html')
def insert(request):
    return render(request, 'log_database/insert.html')
def details(request, emp_id):
    return HttpResponse("You are looking at the employee number " + str(emp_id) + " details")


#Connects to each keyspace then sends it to webpage
def displayTables(request):
    keyspace = Keyspaces.objects.first()
    cluster = Cluster(['155.230.91.227'])
    session = cluster.connect(keyspace.keyspace_name)
    if keyspace.keyspace_name == "beta":
        fullstack = session.execute("select * from fullstack limit 50;")
        error = session.execute("select * from error;")
        openstack = session.execute("select * from openstack limit 50")
        context = {
        'fullstack': fullstack,
        'error': error,
        'openstack': openstack,
        }
        return render(request, 'log_database/display.html', context)
    elif keyspace.keyspace_name == "techfossguru":
        employee = session.execute("select * from employee;")
        context = {
        'employee': employee,
        }
        return render(request, 'log_database/display.html', context)
        

def getKeyspaces(request):
    if request.method == 'POST':
        form = KeyspaceForm(request.POST)
        if form.is_valid():
            if Keyspaces.objects.if_not_exists():
                keyspace = Keyspaces.objects().create(
                    keyspace_name = form.cleaned_data.get('keyspace'),
                    id = 1
                )
            else:
                keyspace = Keyspaces.objects(id=1).update(
                    keyspace_name = form.cleaned_data.get('keyspace')
                )
            return HttpResponseRedirect('display/')
    else:
        form = KeyspaceForm()
    return render(request,'log_database/index.html', {'form': form})

def tableDetails(request):
    if request.method == 'POST':
        form = TableForm(request.Post)
        if form.is_valid():
            if TableObject.objects.if_not_exits():
                table = TableObject.objects().create(
                    table_column_name = form.cleaned_data('table_columns'),
                    id = 1
                )
            else:
                table = TableObject.objects(id=1).update(
                    table_column_name = form.cleaned_data('table_columns')
                )
            return HttpResponseRedirect('display/')
        else:
            form = TableForm()
        return render(request, 'log_database/display.html', {'tableForm': form})

def newOpenstackQuery(request):
    if request.method == 'POST':
        form = InsertQueryForm(request.POST)
        if form.is_valid():
            new_query = form.save()
            return HttpResponseRedirect('./')
    else:
        form = InsertQueryForm()
    return render(request, 'log_database/insertOpen.html', {'OpenstackForm': form })

def newFullstackQuery(request):
    if request.method == 'POST':
        form = InsertFullStackForm(request.POST)
        if form.is_valid():
            new_query = form.save()
            return HttpResponseRedirect('./')
    else:
        form = InsertFullStackForm()
    return render(request, 'log_database/insert.html', {'form': form })


def newEmployeeQuery(request):
    if request.method == 'POST':
        form = InsertEmployeeForm(request.POST)
        if form.is_valid():
            new_query = form.save()
            return HttpResponseRedirect('./')
    else:
        form = InsertEmployeeForm()
    return render(request, 'log_database/insertEmployee.html', {'EmployeeForm': form })
