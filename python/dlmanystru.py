from mp_api.client import MPRester
from pymatgen.io.vasp.inputs import Poscar

with MPRester(api_key="FBSqxhdYS2x9d3qC4N87VxONfagupI9n") as mpr:
    # Structure for material id
    MPids = ["mp-557395"]
    for MPid in MPids:
        docs = mpr.summary.search(material_ids=[MPid], fields=["structure"])
        structure = docs[0].structure
        # save structure as a poscar file
        structure.to(fmt="poscar", filename=MPid + ".poscar")
