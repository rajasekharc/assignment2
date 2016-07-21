import csv
import calendar



try:
    input_f=input("Enter the file with precipitation data==>")
    ptr=open(input_f,"rt")
    r=csv.reader(ptr)   

    #day and precipitation dictionary
    c=[]
    for row in r:
        if row[0][0:6] not in c:
            c.append(row[0][0:6])
    
    y=0.0
    d={}   
    
    for x in c:
        pointer=open(input_f,"rt")
        r=csv.reader(pointer)
        for key in r:
            try:
                if x==key[0][0:6]:
                    y=y+float(key[1])
                    d[x]=y
                else:
                    pass
            except ValueError:
                pass
        y = 0.0
         
    output_f=input("Enter the monthly data file to save to==>")

    o_ptr=open(output_f,"wt", newline = '')
    wr=csv.writer(o_ptr)

    for key,value in sorted(d.items()):
        wr.writerow([key,value])
    o_ptr.close()
    ptr.close()
    
               
except IOError:
    print("The file specified could not be found")


try:
    n_ptr=open(output_f,"rt")
    rd=csv.reader(n_ptr)
    j=[]
    for row in rd:
        if row[0][4:] not in j:
                j.append(row[0][4:])
        
    k=0.0
    q={'01':'Jan','02':'Feb','03':'March','04':'April','05': 'May','06':'June','07':'July','08':'Aug','09':'Sept','10':'Oct','11':'Nov','12':'Dec'}
    s=['Jan', 'Feb', 'March', 'April','May','June','July','Aug','Sept','Oct','Nov','Dec']
    p={}
    r={}
    for x in j:
        m_ptr=open(output_f,"rt")
        rc=csv.reader(m_ptr)

        for y in rc:
            if x==y[0][4:]:
                k=k+float(y[1])
                p[x]=k/10
                
            else:
                pass
        k = 0.0
    
    for key in p:
        for key in q:
            r[q[key]]=p[key]
    print("Monthly Total Averages")
    print("%15s\t%s\n\t  ===============" %('Month','AvgPrecip'))
    for key,value in (sorted(r.items(), key=lambda t:s.index(t[0]))):
        print("%15s\t%8.4f"%(key,r[key]))
        
except IOError:
    print("the file specified could not be found")
   
    
