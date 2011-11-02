import os
import sys
sys.path.append('../../common')
from env_indigo import *

indigo = Indigo()
m = indigo.createMolecule()
a0 = m.addAtom("C")
a1 = m.addAtom("N")
a2 = m.addAtom("O")
a3 = m.addAtom("P")
a0.addBond(a1, 1)
a0.addBond(a2, 1)
a0.addBond(a3, 1)
print(m.smiles())
a0.addStereocenter(indigo.ABS, a1.index(), a2.index(), a3.index())
m.layout()
print(m.smiles())
m.clearStereocenters()
a4 = m.addAtom("H")
a0.addBond(a4, 1)
a0.addStereocenter(indigo.ABS, a1.index(), a2.index(), a3.index(), a4.index())
print(m.smiles())
if not os.path.exists("out"):
   os.makedirs("out")
m.layout()
m.saveMolfile("out/stereocenters_out12.mol")
m.clearStereocenters()
a0.addStereocenter(indigo.ABS, a2.index(), a1.index(), a3.index(), a4.index())
print(m.smiles())
m.layout()
m.saveMolfile("out/stereocenters_out21.mol")
