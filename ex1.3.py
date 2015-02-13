dkm=10
dmile=dkm/1.61
dm=dkm*1000
ts=(43.0*60)+30
tore=ts/3600
vms=dm/ts
print ('Distanta m, timp s, viteza m/s  ///'), dm, ts, vms
vkmh=dkm/tore
print ('Distanta km, timp h, viteza km/h   ///'), dkm, tore, vkmh
vmileh=dmile/tore
print ('Distanta mile, timp h, viteza mile/h   ///'), dmile, tore, vmileh