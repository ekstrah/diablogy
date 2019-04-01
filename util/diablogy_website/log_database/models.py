import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cqlengine.query import ModelQuerySet
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement
from django.db import models
from cassandra.cqlengine.management import sync_table

# Create your models here.




class Keyspaces(Model):
    id = columns.Integer(primary_key=True)
    keyspace_name = columns.Text()

    def __str(self):
        return self.keyspace_name

#Models of tables from keyspaces
#Tables from KEYSPACE techfossguru
class Employee(DjangoCassandraModel):
    __keyspace__ = 'techfossguru'
    emp_id = columns.Integer(primary_key=True)
    city = columns.Text()
    ename = columns.Text()
    sal = columns.Double()
    def __str__(self):
        return self.ename
    
#Tables from KEYSPACE beta
class Fullstack(DjangoCassandraModel):
    __keyspace__ = 'beta'
    id = columns.Integer(primary_key = True)
    contents = columns.Text()
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.Text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()
    def __str__(self):
        return self.id

class Teststack(DjangoCassandraModel):
    __keyspace__ = 'beta'
    id = columns.Integer(primary_key = True)
    contents = columns.Text()
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.Text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()

    def __str__(self):
        return self.id

class Pytest(DjangoCassandraModel):
    id = columns.Integer(primary_key = True)
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.Text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()
    def __str__(self):
        return self.id


class Error(DjangoCassandraModel):
    id = columns.Integer(primary_key = True)
    error =  columns.Text()
    msg = columns.Text()
    def __str__(self):
        return self.id

class Openstack(DjangoCassandraModel):
    id = columns.Integer(primary_key = True)
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.Text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()
    def __str__(self):
        return self.id