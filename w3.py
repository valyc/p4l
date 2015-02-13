#x=77
#if x<10: 
#  print 'mai mic'
# print 'aproape gata'
#if x>20: print 'mai mare'
#print 'gata'

# partea 2
#x=5
#if x==5:
#  print 'egal cu 5'
#  print 'yo yo'
#if x>=5:
#  print 'mai mare ca 5'
#  print 'yep yep'
#if x<=5:
#  print 'mai mic sau egal cu 5'

x=0
y=0
z=exit
x=raw_input('Introdu ceva ')
print x
#while x != z
  try:
    y=int(x)
    print y
    if y%2==0: 
      print 'numarul ', y, 'este par'
    else : print 'numarul ', y, 'este impar'
  except:
    if x!='exit': 
      print 'mai introdu odata'
print 'pina aici a mers ostasul'