from ase.io import read, write
from ase.build import make_supercell

# 读取POSCAR文件
POSCAR = "mp-92.poscar"
structure = read(POSCAR)

# 构造2x2x2的超胞
supercell = make_supercell(structure, [[2, 0, 0], [0, 2, 0], [0, 0, 4]])

# 将超胞保存为POSCAR格式文件
write(POSCAR + '_224supercell', supercell, format='vasp')
