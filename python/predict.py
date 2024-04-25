import dpdata, deepmd
from deepmd.infer import DeepPot
import numpy as np
system = dpdata.System('POSCAR')
dp = DeepPot('graph.000.pb')
labeled_sys= system.predict(dp)
print ('the energy is ',labeled_sys['energies'][0])
