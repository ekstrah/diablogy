import uuid
from cassandra.cqlengine import columns
from django_cassandra_engine.models import DjangoCassandraModel
from cassandra.cqlengine.models import Model
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement


# Create your models here.


#Models of tables from keyspaces
#Tables from KEYSPACE techfossguru
class Employee(DjangoCassandraModel):
    __keyspace__ = 'techfossguru'
    emp_id = columns.UUID(primary_key=True)
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

class Teststack(Model):
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


class Pytest(Model):
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


class Error(Model):
    id = columns.Integer(primary_key = True)
    error =  columns.Text()
    msg = columns.Text()
    def __str__(self):
        return self.id

#OPENSTACK TABLE - USED FOR USERS??
class Openstack(Model):
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

#setup connection to cassandra server
connection.setup(['155.230.91.227'], "cqlengine", protocol_version=3)

cluster = Cluster(['155.230.91.227'])
session = cluster.connect('beta')
rows = session.execute("select * from fullstack;")
for row in rows:
    example = Fullstack.create(
        contents = row.contents,
        end_time = row.end_time,
        fd = row.fd,
        host_name = row.host_name,
        pipe_val = row.pipe_val,
        proc_id = row.proc_id,
        proc_name = row.proc_name,
        return_byte = row.return_byte,
        sock_type = row.sock_type,
        start_time = row.sock_type,
        sys_call = row.sys_call,
        thread_id = row.thread_id,
        turnaround_time = row.turnaround_time,
        valid = row.valid
    )
