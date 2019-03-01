# -*- coding: utf-8 -*-
"""
Created on Mon Jul 31 00:43:49 2017

@author: nxu
"""
point = []
with open("grid.txt","r") as reader:
    p = 1
    for index ,line in enumerate(reader):
        j = 0
        for i in range(len(line)):
            if line[j] != " ":
                point.append(str(p)+" 1 "+ str(float(index+1))+ "  "+str(float(i+1))+"  0.0   0  0  0  "+"\n")
                print(p,1,index+1,i+1)
            else:
                point.append(str(p)+" 2 "+ str(float(index+1))+ "  "+str(float(i+1))+"  0.0  0  0  0"+"\n")
                print(p,2,index+1,i+1)
            p+=1 
            j+=1


s='''LAMMPS data file by lmp_data

%s atoms
2 atom types


0 %s xlo xhi
0 %s ylo yhi
-1 1  zlo zhi

Masses

1 1
2 1

Atoms

''' %(p-1,index+2,i+2)
print(s)
point.insert(0,s)
point.append("\n")
with open("lmp.data","w") as writer:
    writer.writelines(point)