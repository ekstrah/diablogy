import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine import DjangoCassandraModel
from django.db import connection

# Create your models here.

#Models of tables from keyspaces
#Tables from KEYSPACE techfossguru
class Employee(DjangoCassandraModel):
    emp_id = columns.UUID(primary_key=True, default=uuid.uuid4)
    city = columns.Text()
    ename = columns.Text()
    sal = columns.Double()
    
#Tables from KEYSPACE beta
class Fullstack(DjangoCassandraModel):
    id = columns.UUID(primary_key = True)
    contents = columns.Text()
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()


class Teststack(DjangoCassandraModel):
    id = columns.UUID(primary_key = True)
    contents = columns.Text()
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()

class Pytest(DjangoCassandraModel):
    id = columns.UUID(primary_key = True)
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()

class Error(DjangoCassandraModel):
    id = columns.UUID(primary_key = True)
    error =  columns.Text()
    msg = columns.Text()

#OPENSTACK TABLE - USED FOR USERS??
class Openstack(DjangoCassandraModel):
    id = columns.UUID(primary_key = True)
    end_time = columns.Double()
    fd = columns.Integer()
    host_name = columns.Text()
    pipe_val = columns.Text()
    proc_id = columns.Text()
    proc_name = columns.Text()
    return_byte = columns.Integer()
    sock_type = columns.text()
    start_time = columns.Double()
    sys_call = columns.Text()
    thread_id = columns.Text()
    turnaround_time = columns.Double()
    valid = columns.Text()

