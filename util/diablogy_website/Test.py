    
from django.shortcuts import render
from django.http import HttpResponse
import logging
from cassandra.cqlengine import connection
from cassandra.cqlengine.management import sync_table
from django.http import HttpResponse
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement


    
cluster = Cluster(['155.230.91.227'])
session = cluster.connect('beta')
rows = session.execute('select * from fullstack;')
for row in rows:
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
    print("contents = " + row.contents , "thread id = " + row.thread_id)