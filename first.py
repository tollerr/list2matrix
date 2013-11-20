#import the library used to query a website

# from BeautifulSoup import BeautifulSoup
#  
# import urllib2 
# url = urllib2.urlopen("http://www.python.org")
#  
# content = url.read()
#  
# soup = BeautifulSoup(content)
#  
# links = soup.findAll("a")

from string import maketrans

lst=['rod','test','esta','e','a','historia','de','um','teste']
lst2=['esta','bagaca','foi','criada','por','um','rod']

for a in lst:
    print "%s tem tamanho %d"%(a,len(a))
    
for c in lst2:
    print c
    
print "*"*100

print lst2
print " ".join(lst2)

print "^"*100
transtab=maketrans(" ",",")
with open("first.py") as cfile:
    print cfile.read().translate(transtab)