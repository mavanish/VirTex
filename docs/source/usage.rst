Usage
=====

.. _installation:

Pre Processing
--------------
**Before you use VirTex**, generate quaternion for each atom in the microstructure either by **Polyhedral Template Matching (PTM)** using `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ or `Ovito <https://www.ovito.org/>`_. 

| See detials below-
| ---------------------------------------------------------

LAMMPS
======
**1- If you are using LAMMPS** to pefrome PTM and calculate quaternion use *ptm/atom* command. Examples are provided below for detial check `LAMMPS command page for PTM <https://docs.lammps.org/compute_ptm_atom.html>`_.


.. code-block:: console

   compute ID group-ID ptm/atom structures threshold group2-ID
..

* ID, group-ID are documented in compute command
* ptm/atom = style name of this compute command 
* structures = default or all or any hyphen-separated combination of fcc, hcp, bcc, ico, sc, dcub, dhex, or graphene = structure types to search for
* threshold = lattice distortion threshold (RMSD)  
* group2-ID determines which group is used for neighbor selection (optional, default “all”)  

For example:

   | compute 1 all ptm/atom default 0.1 all
   | compute 1 all ptm/atom fcc-hcp-dcub-dhex 0.15 all
   | compute 1 all ptm/atom all 0
| ---------------------------------------------------------
**2- If you are using Ovito** to pefrome PTM and calculate quaternion use *Polyhedral Template Matching* modifier in Ovito application or best way would be running python script to generate quaternions for all snapshots. 

Short example is provided below for detial check `Ovito PTM modifier <https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html#ovito.modifiers.PolyhedralTemplateMatchingModifier>`_.

For example:

.. code-block:: console

   from ovito.io import import_file, export_file
   from ovito.modifiers import PolyhedralTemplateMatchingModifier
   
   node = import_file("filename.dump")
   modifier = PolyhedralTemplateMatchingModifier(output_orientation = True)
	node.modifiers.append(modifier)
	node.compute()
   
   export_file(node, "filename_PTM.dump", 'lammps_dump',
	columns = ['Particle Identifier', 'Particle Type', 'Position.X', 'Position.Y', 'Position.Z',\
					'Structure Type','Orientation.X','Orientation.Y','Orientation.Z','Orientation.W'])
..

The exmaple directory contains a python script to carry-out PTM for all snapshot using *for loop*. The directory also contain an example bash file to submit the job if you are using HPC. Check here
   
Installation
------------

To use VirTex, first install it using pip:

.. code-block:: console

   (.venv) $ pip install virtex

Creating recipes
----------------

To retrieve a list of random ingredients,
you can use the ``lumache.get_random_ingredients()`` function:

.. autofunction:: lumache.get_random_ingredients

The ``kind`` parameter should be either ``"meat"``, ``"fish"``,
or ``"veggies"``. Otherwise, :py:func:`lumache.get_random_ingredients`
will raise an exception.

.. autoexception:: lumache.InvalidKindError

For examples:

>>> import lumache
>>> lumache.get_random_ingredients()
['shells', 'gorgonzola', 'parsley']

