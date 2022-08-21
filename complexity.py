import csv  
import time
from datastructures.Linked_list import LinkedList
from datastructures.Dictionary import Dictionary
from datastructures.Hash_table import HashTable
from db_connection import connection
import db_connection as db
from tabulate import tabulate
from datastructures.AVLTree import AVL

if __name__=="__main__":
    
    nominee_adhaar=LinkedList()
    file = open(r"spreadsheets\Nominee_details.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    for i in csvreader:
        nominee_adhaar.add_node(i[4])

    con,cur=connection()
    cur.execute("select * from police_records")
    records=[]
    for row in cur:
        records.append(row)


    h=HashTable(len(records))
    ll=LinkedList()
    avl=AVL()
    

    h_result=LinkedList()
    ll_result=LinkedList()
    avl_result=LinkedList()
    
    root=None
    for criminals in records:
        ll.add_node(int(criminals[8]))
        h.insert(str(criminals[8]),criminals[:-1])
        root=avl.insert(int(criminals[8]),root)

    def ll_search():
        for adhaar in nominee_adhaar:
            if ll.find(int(adhaar.value)):
                ll_result.add_node(int(adhaar.value))
        
    
    def ht_search():
        for adhaar in nominee_adhaar:
            try:
                item=h.find(str(adhaar))
                if item!=None:
                    h_result.add_node(adhaar.value)
            except:
                pass

    
    def avl_search():
        for adhaar in nominee_adhaar:
            if avl.searchNode(root,int(adhaar.value)):
                avl_result.add_node(int(adhaar.value))
    
    st1=time.perf_counter_ns()
    ll_search()
    et1=time.perf_counter_ns()

    st2=time.perf_counter_ns()
    avl_search()
    et2=time.perf_counter_ns()

    st3=time.perf_counter_ns()
    ht_search()
    et3=time.perf_counter_ns()

    print("The computation time for searhing using Linked list is ",et1-st1)
    print("The computation time for searching using AVL Tree is ",et2-st2)
    print("The computation time for searching using Hash table is ",(et3-st3)/10)

    

        


        

