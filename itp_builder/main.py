import numpy as np
from core_bond import bond_core
from long_diag import long_diagonal_bond
from short_diag import short_diag_bond
from side_left import side_left
from side_right import side_right
from middle_constraint import middle_constraint
from main_dihedral import main_dihedral
from across_dihedral import across_dihedral
from vertical_diagonal import vertical_diagonal
from vs import virtual_site1, virtual_site2
from virtual_site import virtual_site
from grouping import regroup
from exclusions import exclusions


def main():
    """
    This code needs to be changed later to accomodate wide-range of structure files (gro format)
    """
    list_of_middle = [np.arange(i, i+10) for i in np.arange(1, 90 +1, 10)]
    list_of = [i.tolist() for i in list_of_middle]
    for_bonds = []
    for i in range(len(list_of)):
        if i % 2 == 0:
            for_bonds.append(list_of[i])
    new_list = []
    for i in for_bonds:
        new_list.append(regroup(i))

    vs = virtual_site1(new_list) + virtual_site2(list_of)

    dc = {}
    il = []
    for i in list_of:
        for j in i:
            il.append(j)
        for i in il:
            dc[i] = 36
        
        for i in range(len(vs)):
            dc[vs[i][0]] = 0
            
        for i in range(len(vs)):
            for j, k in dc.items():
                if j in vs[i][-2:]:
                    dc[j] +=18
        
    

    
    


    with open('graphene.itp', 'w+') as f:
        f.write(";;;;;Graphene\n\n[ moleculetype ]\n; molname nrexcl\n   GRA       1;\n\n[ atoms ]\n; nr type resnr residue atom cgnr charge mass \n")
        for i in np.arange(1,91):
            f.write(f"   {i:4}   TC5   0   GRA   B{i}   {i:4}   {0:4}   {dc[i]:4}\n")
        f.write("\n\n")
        f.write("[ bonds ]\n")
        f.write("; i j funct length kb\n")
        bond_core(new_list, f)
        long_diagonal_bond(new_list,f)
        short_diag_bond(new_list,f)
        side_left(list_of, f)
        side_right(list_of, f)
        f.write("\n\n")
        f.write("#ifndef FLEXIBLE\n")
        f.write("[constraints]\n")
        f.write("#endif\n")
        f.write("; i j funct length \n")
        middle_constraint(new_list,f)
        f.write("\n\n")
        f.write("[ dihedrals ]\n")
        f.write(";  i j k l funct ref.angle force_k\n")
        main_dihedral(new_list,f)
        across_dihedral(new_list,f)
        vertical_diagonal(new_list, f)
        f.write("\n\n")
        f.write("[ virtual_sitesn ]\n")
        f.write("; site funct constructing atom indices\n")
        virtual_site(new_list, list_of, f)
        f.write("\n\n")
        f.write("[ exclusions ]\n")
        exclusions(list_of, f)
    


main()
    

    

    


 

    
