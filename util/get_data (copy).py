import logging
from cassandra import ConsistencyLevel
from cassandra.cluster import Cluster, BatchStatement
from cassandra.query import SimpleStatement


def Connect():
    keyspace = "beta"
    cluster = Cluster(['155.230.91.227'])
    session = cluster.connect(keyspace)
    rows = session.execute('SELECT * from fullstack;')
    for row in rows:
        print("id = "+str(row.id)+ "  " + "proc_name = " + row.proc_name + "   "+"thread_id = "+ row.thread_id)
        

if __name__ == '__main__':
    Connect()



