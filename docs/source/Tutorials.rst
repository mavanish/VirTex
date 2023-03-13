Tutorials
=========

Due to initial development phase and very frequent update of VirTex package, we will provide turtorial along with the package. 

Furture version will have tutorial avaiavle here, Please check back

#Tutorials for using VirTex efficiently. After sucessfull installation of VirTex, first task would be to read the file. Based on the input type of you file, we recommend #normal *lammps dump* format, you would have to choose few inputs for reading the dump files with quartonions. 

# .. code-block:: python

    from virtex.io import readio
    names='filename.dummp' 
    skiprows=9
    df=readio(names, skiprows,'lammps_dump')
..#
