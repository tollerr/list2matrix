'''
Created on Nov 19, 2013

@author: rod
'''

import random
import datetime
import numpy as np


def get_data():
    ports = [100,101,102,104,110,115,118,400,402,405,410,800,801,802,804,810,815,818]
    #print random.randrange(200,3000)
    
    
    base = datetime.datetime.today()
    numdays=360 * 4
    dateList = [ base - datetime.timedelta(days=x) for x in range(0,numdays) ]
    
    #print [[x,random.randrange(200,10000)] for x in ports]
    list_=[(a, b, random.randrange(200,3000)) for a in dateList for b in ports]
    
    #formated list, get only weekdays
    flist=[ (a.strftime("%Y/%m/%d"),b,c) for (a,b,c) in list_ if a.isoweekday() in range(1, 6)]
    # for (a,b,c) in list_:
    #     if a.isoweekday() in range(1, 6):
    #         #print "'%s',%d,%d"%(a.strftime("%Y/%m/%d"),b,c)
    #         print "'%s',%d,%d"%(a.strftime("%Y/%m/%d"),b,c)
    return flist




    
def test():    
    xxx=get_data()
            
    for x in xxx:
        print x




def get_indexed_data(data, idx):
    #create an indexed hash with unique values
    idx_values = {}
    dt = set([a[idx] for a in data]) #get unique dates
    for i, v in enumerate(sorted(dt)): #create hash that returns the index of a date
        idx_values[v] = i
    
    return idx_values

def convert_to_matrix(data):
    
    #get indexed values for the Date - index 0
    dts = get_indexed_data(data,0)

    #create an index hash with unique ports - index 1
    pts = get_indexed_data(data,1)    
    
    ##Note needed
    #print dts
    #print sorted(pt)
    #print '\n'.join(sorted(dt))
    
    #for x in sorted(pt):
    #    print "%d-->%d"%(x,pts[x])
    
    #define a matrix

    

    matrix = np.zeros((len(pts),len(dts)), dtype='int32')
       
  
    for x in data:
        try:
            matrix[pts[x[1]]][dts[x[0]]] = x[2]
            # print "(%s,%s)(%d,%d)->%d"%(x[1],x[0],pts[x[1]],dts[x[0]] , x[2])
        except:
            print "Failed:",x
     
    return matrix
    # for y in matrix:
    #     print y   

def save_matrix(matrix):
    np.savetxt("test.csv", matrix, delimiter=",")
    return 
 
def save_dates(dts):
    with open('dates.csv','wb') as cfile:
        cfile.write('\n'.join(dts))
    return   



if __name__ == 'main':
    
    data=get_data()[:10]
    print data
    matrix=convert_to_matrix(data)    
    print "done"