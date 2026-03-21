import ephem

ephem1 = ephem.Jupiter('1230/1/1')
ephem2 = ephem.Jupiter('1995/1/1')
ephem3 = ephem.Jupiter('2026/1/1')

print(ephem1.sun_distance * 149597870.700)
print(ephem2.sun_distance * 149597870.700)
print(ephem3.sun_distance * 149597870.700)
