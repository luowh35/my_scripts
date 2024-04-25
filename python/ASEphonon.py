#!/usr/bin/env python
import ase
from ase.phonons import Phonons
#from ase.build import bulk
from ase.io import read, write
from ase.optimize import MDMin
from deepmd.calculator import DP
import matplotlib as mpl
mpl.use('Agg') # for plot

calc=DP(model="graph.000.pb")
atoms = read("mp-30.poscar")
atoms.set_calculator(calc)
opt=MDMin(atoms)
opt.run(fmax=0.01)
write("CONTCAR",atoms)

# Phonon calculator
N = 25 
ph = Phonons(atoms, calc,supercell=(N, N, N), delta=0.05)
ph.run()  # calculate ph files. If ph files exist in the folder, we donot need to run
# Read forces and assemble the dynamical matrix
ph.read(acoustic=True)
#ph.clean()   # clean ph files
path = atoms.cell.bandpath([['G','X','U'],['K','G','L','W','X']], npoints=100) # Refer to https://wiki.fysik.dtu.dk/ase/ase/dft/kpoints.html for special points in Brillouin zone
bs = ph.get_band_structure(path)
## dos = ph.get_dos(kpts=(20, 20, 1)).sample_grid(npts=100, width=1e-3)

# Plot the band structure and DOS:
import matplotlib.pyplot as plt
fig = plt.figure(1, figsize=(7, 4))
ax = fig.add_axes([.12, .07, .67, .85])
emax = 0.05
emin = 0
bs.plot(ax=ax, show=False, emin=-emin, emax=emax , lw =1)
## dosax = fig.add_axes([.8, .07, .17, .85])
## dosax.fill_between( dos.energy, y2=0, color='grey',edgecolor='k', lw=1)

import numpy as np
# np.savetxt("dosx",dos.weights[0]) for replot
# np.savetxt("dosy",dos.energy)

## dosax.set_ylim(0, emax)
## dosax.set_yticks([])
## dosax.set_xticks([])
## dosax.set_xlabel("DOS", fontsize=18)
fig.savefig('Cu.png',dpi=300)
xcoords,label_xcoords,_=bs.get_labels()
e_kn=bs.energies[0]
np.savetxt("e_kn_dp",e_kn)
np.savetxt("xcoords_dp",xcoords)
np.savetxt("label_xcoords",label_xcoords)
