#!/usr/bin/python

# Weather Station program below outputs the total precipitations and average precipitations per month from
# 2000 - 2009. The Total monthly precipitation is stored in a output file, which path will be given by user
# And the average monthly precipitation from 2000 - 2009 is output printed on the screen.

import csv
import calendar
import os, sys
##import pylab as plt

# The below method is to check if the array value of dictionary is present or not.
# If not present then it inserts into list 'a'
a = list()
def checkinArray(arrayvalue):
    if arrayvalue in a:
        return False
    else:
        a.append(arrayvalue)
        return True

# The below method is to check if the array value of dictionary is present or not.
# If not present then it inserts into list 'b'
b = list()
def checkinjArray(jvalue):
    if jvalue in b:
        return False
    else:
        b.append(jvalue)
        return True
    pass

#The below method is to check whether the given parameter is float or non-float value
def isfloat(value):
  try:
    float(value)
    return True
  except:
    return False

while 1:
    input_file = input('Enter the file with precipitation data ==>')
    if os.path.isfile(input_file):
        break
    else:
        print ('The file specified could not be found') 

while 1:
    month_input_file = input('Enter the monthly data file to save to. ==>')
    if month_input_file[-4:] == ".csv":
            mifile = open(month_input_file, "w")
            try:
                break
            except (IOError, OSError) as e:
                    print  ('The file specified had an IO Error ')
            finally:
                    mifile.close()
    else:
            print  ('The file specified had an IO Error')
#The below code totals the monthly precipitation values
idict = {}
ifile  = open(input_file, "rt")
try:
    reader = csv.reader(ifile)
    for row in reader:
        if isfloat(row[1]):
            if checkinArray(row[0][:6]):
                idict.update({row[0][:6] : float(row[1]) })
            else:
                idict.update({row[0][:6] : idict[row[0][:6]] + float(row[1]) }) 
finally:
    ifile.close()

# The below code inserts the total precipitation values into the file mentioned by user
mifile = open(month_input_file, "w")
try:
    writer = csv.writer(mifile, delimiter=',')
    for x in a:
        writer.writerow([x, idict[x]])
except (IOError, OSError) as e:
    print  ('The file specified had an IO Error ')
finally:
    mifile.close()

jdict = {}
for key,value in idict.items():
    if checkinjArray(key[4:]):
        jdict.update({key[4:] : float(value) })
    else:
        jdict.update({key[4:] : jdict[key[4:]] + float(value) })    

b.sort()
avg_precipitation = []
print ("\nMonthly Average precipitation since 2000-2009")
print ("=============================================")
for x in b:
    avg_precipitation.append(jdict[x]/10)
    print ("%10s \t || \t%s\n" % (calendar.month_name[int(x)], jdict[x]/10) )

print ('\nThe monthly total precipitation file is present in %s' % month_input_file )

##months_text = ['Jan', 'Feb', 'March', 'April', 'May', 'June', 'July', 'Aug', 'Sept', 'Oct', 'Nov', 'Dec']
##months = [1,2,3,4,5,6,7,8,9,10,11,12]
##plt.title("Monthly Total Averages")
##plt.xlabel("Month")
##plt.ylabel("Precip(mm)")
##plt.xticks(months, months_text)
##plt.plot(months, avg_precipitation)
##plt.show()
