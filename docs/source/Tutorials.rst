Tutorials
=========

Due to the initial development phase and frequent updates of the VirTex package, we will provide a tutorial along with the package. 

.. The future version will have a tutorial available here; Please check back! 

Following is short tuortial for using VirTex efficiently.

 *** After sucessfull installation of VirTex, first task would be to read the file. Based on the input type of you file, we recommend #normal *lammps dump* format, you would have to choose few inputs for reading the dump files with quartonions.*** 

.. code-block:: python

    from virtex.io import readio
    names='filename.dummp' 
    skiprows=9
    df=readio(names, skiprows,'lammps_dump')

.. note:: 

    Convert quartonin angle to rotation matrix using `quaternions_to_rotation`. Also, make sure you have following columns in dump file 'orientationx', 'orientationy', 'orientationz','orientationw'
    
    type='clock' or 'left' clockwise rotation and type='anticlock' or 'right' anti-clockwise rotation

.. code-block:: python

    from virtex.rotation import quaternions_to_rotation
    df_rot=quaternions_to_rotation(df, type='clock')  
 
.. note:: 

    Convert quartonin angle to Euler angles using `quaternions_to_euler`. Also, make sure you have following columns in dump file 'orientationx', 'orientationy', 'orientationz','orientationw'
    
    type='clock' or 'left' clockwise rotation and type='anticlock' or 'right' anti-clockwise rotation
    
.. code-block:: python

    from virtex.rotation import quaternions_to_euler
    df_rot_eul=quaternions_to_euler(df, type='clock')  


    
    
    

    

