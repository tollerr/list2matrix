'''
Created on Nov 19, 2013

@author: rod
'''

import random
import datetime


def get_data():
    ports = [100,101,102,104,110,115,118,400,402,405,410,800,801,802,804,810,815,818]
    #print random.randrange(200,3000)
    
    
    base = datetime.datetime.today()
    numdays=360 * 4
    dateList = [ base - datetime.timedelta(days=x) for x in range(0,numdays) ]
    
    #print [[x,random.randrange(200,10000)] for x in ports]
    list_=[(a, b, random.randrange(200,3000)) for a in dateList for b in ports]
    
    #formated list
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
    
data=get_data() 

#create an indexed hash with uniq dates
dts={}    
dt = set([a[0] for a in data]) #get unique dates    
for i,v in enumerate(sorted(dt)): #create hash that returns the index of a date
    dts[v]=i

#create an index hash with unique ports
pts = {}    
pt = set([a[1] for a in data])
for i,v in enumerate(sorted(pt)):
    pts[v]=i

#print dts
#print sorted(pt)
#print '\n'.join(sorted(dt))

#for x in sorted(pt):
#    print "%d-->%d"%(x,pts[x])

#define a matrix
import numpy as np

#pts = np.array([[2,0],[3,0],[3,1],[5,0],[5,1],[5,2]])

matrix = np.zeros((len(pts),len(dts)), dtype='int32')
   
print "*******"*10 
for x in data:
    try:
        matrix[pts[x[1]]][dts[x[0]]] = x[2]
        #print "(%s,%s)(%d,%d)->%d"%(x[1],x[0],pts[x[1]],dts[x[0]] , x[2])
    except:
        print "Failed:",x
    
print matrix
# for y in matrix:
#     print y   
    
    
