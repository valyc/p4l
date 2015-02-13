# p. 1
print ('3/4 integer, V sferei este ') , 4/3*3.14*5**3
print ('3/4 float,  V sferei este ') , 4/3.0*3.14*5**3
# p. 2
costcarte=24.95
costcarteredus=costcarte*0.6
deliv1=3
delivmore=0.75
nrcarti=raw_input('Numarul de carti comandate este  ')
nrcarti=int(nrcarti)
costtotal=costcarte+(nrcarti-1)*costcarteredus+deliv1+(nrcarti-1)*delivmore
print ('Cost total comanda plus delivery este '), costtotal, (' $')

# p. 3
tstartsec=6*3600+52*60
t1s=8*60+15
t2s=3*(7*60+12)
tfinishsec=tstartsec+t1s+t2s+t1s
tfh=tfinishsec/3600
tfm=(tfinishsec%3600)/60
tfs=tfinishsec-(tfh*3600+tfm*60)
print ('Timp pornire 6:52')
print ('Timp intoarcere la mic dejun '), tfh, (':'), tfm,  (':'), tfs