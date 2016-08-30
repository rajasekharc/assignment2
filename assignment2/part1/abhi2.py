#!/usr/bin/python

# The program is to find the summary of the zip codes and the victim count of each assault
import csv, collections
import os, sys
from operator import itemgetter

flag = 1
offense_dict = {}
incidents_dict = {}
first_row = 1
details_first_row = 1
details_dict = {}
details_list = list()
offense_list = list()
offense_count_dict = {}

# To check whether all the input files are in the present directory or not.
if os.path.isfile("offenses.csv"):
    #do nothing
    pass
else:
    flag = 0
    print ('offenses.csv file is not found in the directory') 

if os.path.isfile("incidents.csv"):
    #do nothing
    pass
else:
    flag = 0
    print ('incidents.csv file is not found in the directory') 

if os.path.isfile("details.csv"):
    #do nothing
    pass
else:
    flag = 0
    print (' details.csv file is not found in the directory') 

# Enter into main program if all the files are present only.
if flag:
    print("Starting......")
    # Opens offenses.csv file and copies the offense description to the key of offense number, in a dictionary.
    offenses_file  = open("offenses.csv", "rt")
    try:
        csv_reader = csv.reader(offenses_file)
        for row in csv_reader:
            offense_dict[row[0]] = row[1]
    except (IOError, OSError) as e:
        print  ('The file specified had an IO Error ')
    finally:
        offenses_file.close()

    # Opens details.csv and copies the report numbers, who are 'VIC' (victims) only
    details_file  = open("details.csv", "rt")
    try:
        csv_reader = csv.reader(details_file)
        for row in csv_reader:
            if details_first_row:
                details_first_row = 0
                continue
            if row[1] == 'VIC':
                if row[0] not in details_list:
                    details_list.append(row[0])       
    except (IOError, OSError) as e:
        print  ('The file specified had an IO Error ')
    finally:
        offenses_file.close()

    # Opens incidenst.csv does the following things
    # 1. Aggregates the number of counts of zip code
    # 2. Aggregates the number of counts of a particular assault on victims
    incidents_file  = open("incidents.csv", "rt")
    try:
        csv_reader = csv.reader(incidents_file)
        for row in csv_reader:
            if first_row:
                first_row = 0
                continue
            # Here we check if the input is empty or 0. If so we increment the '99999' key
            if row[4] == '' or row[4] == '0':
                if "99999" in incidents_dict:
                    incidents_dict["99999"] = incidents_dict["99999"] + 1
                else:
                    incidents_dict["99999"] = 1
            else:
                # Here we check for the zip code and increment the count the total count for a particular zip code
                if row[4] in incidents_dict:
                    incidents_dict[row[4]] = incidents_dict[row[4]] + 1
                else:
                    incidents_dict[row[4]] = 1
            # Here we check for the offense type and increment the count to get the total count for a particular offense        
            if row[0] in details_list:
                if row[3] in offense_list:
                    offense_count_dict[row[3]] = offense_count_dict[row[3]] + 1
                else:
                    offense_list.append(row[3])
                    offense_count_dict[row[3]] = 1
    except (IOError, OSError) as e:
        print  ('The file specified had an IO Error ')
    finally:
        offenses_file.close()

    # Function to call when option 2 is selected.
    # First we sort the offense dictionary by value, so that we get the sorted dictionary of count
    def offense_list():
        print ("Offense \t \t  Victims")
        print ("=====================================")
        sorted_offenses = collections.OrderedDict(sorted(offense_count_dict.items(), key=itemgetter(1), reverse=True ))
        for key,value in sorted_offenses.items():
            print ("%21s \t  %s" % (offense_dict[key], value))       

    # Function to call when option 1 is selected.
    # First we sort the zip dictionary by key, so that we get the sorted dictionary of zipcode
    def summary():
        print ("Zip Code     Crimes")
        print ("====================")
        sorted_incidents = collections.OrderedDict(sorted(incidents_dict.items()))
        for key,value in sorted_incidents.items():
            print ("%5s \t  %5s\n" % (key, value))
        
    while 1:
        print('\n             KCPD Crime Statistics      ')
        print('1. Summary by Zip Code ')
        print('2. Victim count by offense Type')
        print('Q. Quit')
        input_option = input()
        if input_option in ["1", "2", "q", "Q"]:
            if (input_option == "q") or (input_option == "Q"):
                break
            if (input_option == "1"):
                summary()
            if (input_option == "2"):
                offense_list()
        else:
            print('You must choose one of the selections 1,2,Q')
