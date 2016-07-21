import csv
import collections


def summary():
    try:
    
        f_ptr=open("incidents.csv","rt")
        r=csv.reader(f_ptr)

        b=[]
        for row in r:
            b.append(row[4])
            
        
        d = {x:b.count(x) for x in b}

        d['99999']=d['99999']+d['']+d['0']
        
        del d['0'],d[''],d['Zip Code']

        print("Zipcode crimes")
        
        
        for key,value in sorted(d.items()):
            print(key,value)
    except FileNotFoundError:
        print("the file specified could not be found")
    finally:
        f_ptr.close()


def vic_count():

    #offense num and description

    try:
        o_ptr=open("offenses.csv","rt")
        rd=csv.reader(o_ptr)

        g={}
        for row in rd:
            g[row[0]]=row[1]
        del g['Offense']

    #offense num and count
    
        i_ptr=open("incidents.csv","rt")
        r=csv.reader(i_ptr)

        c=[]
        for row in r:
            c.append(row[3])
        e={x:c.count(x) for x in c}
        del e['Offense']

    #merging two dictionaries into one
        h={}
        for key in e:
            for key in g:
                h[(g[key])]=e[key]
        
        for k,v in sorted(h.items(), key=lambda v:v[1], reverse = True):
            print (k,v)
    except FileNotFoundError:
        print("the file specified could not be found")
    finally:
        o_ptr.close()
        i_ptr.close()

def console():
    a=input()
    
    if a=="1":
        summary()

    elif a=="2":
        vic_count()
        

    elif a=="Q" or a=="q":
        quit()
    else:
        print("you must choose one of the selections 1,2,Q")
        console()

#for console        
print("1.Summary by zip code \n2.Victim count by offense Type\nQ.Quit \n")
console()
          
