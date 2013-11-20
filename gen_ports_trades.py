'''
Created on Nov 19, 2013

@author: rod
'''

import random
import datetime
import numpy as np


def get_data():
    #define ports
    ports = [100,101,102,104,110,115,118,400,402,405,410,800,801,802,804,810,815,818]
    
    #define date interval
    base = datetime.datetime.today()
    numdays=360 * 4
    dateList = [ base - datetime.timedelta(days=x) for x in range(0,numdays) ]
    
    #create a list with date,port, and a random number
    list_=[(a, b, random.randrange(200,3000)) for a in dateList for b in ports]
    
    #formated list, get only weekdays
    flist=[ (a.strftime("%Y/%m/%d"),b,c) for (a,b,c) in list_ if a.isoweekday() in range(1, 6)]

    #return a list of tuple (date,port,rnd)
    return flist




    
def test(): 
    """ Unused """   
    xxx=get_data()
            
    for x in xxx:
        print x




def get_indexed_data(data, idx):
    """based on an list of list, creates an indexed hash for element at idx
    create an indexed hash with unique values"""
    idx_values = {}
    dt = sorted(set([a[idx] for a in data])) #get unique sorted items
    for i, v in enumerate(dt): #create hash that returns the index of a item
        idx_values[v] = i 
    
    return idx_values ,dt

def convert_to_matrix(data):
    """ based on list of 3 values list, create a matrix 
    where value 1 is column and value 2 is row"""
    
    #get indexed values for the Date - index 0
    dts = get_indexed_data(data,0)

    #create an index hash with unique ports - index 1
    pts = get_indexed_data(data,1)    
  
    #defines a matrix with zero values
    matrix = np.zeros((len(pts),len(dts)), dtype='int32')
     
    #puts in the matrix the list of (date,port,#) 
    for x in data:
        try:
            matrix[pts[x[1]]][dts[x[0]]] = x[2]
            # print "(%s,%s)(%d,%d)->%d"%(x[1],x[0],pts[x[1]],dts[x[0]] , x[2])
        except:
            print "Failed:",x
     
    return matrix
    # for y in matrix:
    #     print y   

def save_matrix(matrix, filen):
    """ saves the matrix """
    np.savetxt(filen, matrix, delimiter=",")
    return 
 
def save_list(lst, filen):
    """ saves any list """
    with open(filen,'wb') as cfile:
        cfile.write('\n'.join(lst))
    return   



###########################3
# main

    
data=get_data()[:21]

print '-'*40
print data
print '-'*40
print get_indexed_data(data, 0)
print '-'*40
print get_indexed_data(data, 1)
print '-'*40
matrix=convert_to_matrix(data)
print matrix    
print "done"   

