import csv
import collections
from collections import defaultdict

def summary():
    f_ptr=open("incidents.csv","rt")
    r=csv.reader(f_ptr)
    b=[]
    for row in r:
        b.append(row[4])
        
    
    d = {x:b.count(x) for x in b}
    d['99999']=d['99999']+d['']+d['0']
    del d['0']
    del d['']
    del d['Zip Code']
    print("Zipcode crimes")
    for key in d:
        print ("%s   %s" %(key,d[key])) 

def vic_count():
    

    #offense num and description
    o_ptr=open("offenses.csv","rt")
    rd=csv.reader(o_ptr)

    g={}

    for row in rd:
        g[row[0]]=row[1]
    del g['Offense']
##    for key in g:
##        print(key,g[key])

##    m=(sorted(g.items(), key=lambda x: x[0]))
##    print (m)

#offense num and count

    i_ptr=open("incidents.csv","rt")
    r=csv.reader(i_ptr)
    c=[]
    for row in r:
        c.append(row[3])
    e={x:c.count(x) for x in c}
    del e['Offense']
    
    h={}
    for key in e:
        for key in g:
            h[(g[key])]=e[key]
    for key in h:
        print (key,h[key])
    f=(sorted(h.items(), key=lambda x: x[1]))
            
##    for key in (e,g):
##        h[e[key]]=g[key]
##    for key in h:
##        print(key,h[key])
##        

    
##    for key in e:
##        print(key,e[key])
##    
##    
##    print(f)        

     


    #merging two dictionaries e{num,count},g{offense num,description}
##    f=defaultdict(list)
##    for i in (e,g):
##        for key,value in d.iteritems():
##            f[key].append(value)
##    for key in f:
##        print(key,f[key])

        
    
    
    

    
    





#for console 
a=input("1.Summary by zip code \n2.Victim count by offense Type\nQ.Quit \n")

if a=="1":
    summary()

elif a=="2":
    vic_count()
    

elif a=="Q" or a=="q":
    quit()
else:
    print("you must choose one of the selections 1,2,Q")
    
          
