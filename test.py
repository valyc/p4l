q=raw_input('Introdu un numar ')
try:
  q=int(q)
  if q%2==0: print ('numarul '), q, (' este par')
  else: print ('numarul '), q, (' este impar')
except:
  print q, (' nu este numar!')

# test 2 vid 5.3

ore_lucrate=raw_input('Introdu orele lucrate ')
rata=raw_input('Introdu plata per ora ')
try: 
  ore_lucrate=int(ore_lucrate)
  rata=int(rata)
  if ore_lucrate<=40:
    pay=ore_lucrate*rata
    print ('Pay '), pay
  else: 
    pay=(40*rata)+(ore_lucrate-40)*(rata*1.5)
    print ('pay '), pay
except:
  print (' nu ati introdus numere!')