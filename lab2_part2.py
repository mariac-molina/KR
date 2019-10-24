from agents import *

class Dirt(Thing):
    pass

vac = VacuumEnvironment()
d1 = Dirt()
d2 = Dirt()
d3 = Dirt()
vac.add_thing(d1, [0,0])
vac.add_thing(d2, [0,1])
vac.add_thing(d3, [0,2])
