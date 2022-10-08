Usage
=====

.. _installation:

Pre Processing
--------------
**Before you use VirTex**, generate quaternion angles for each atom in the microstructure via **Polyhedral Template Matching (PTM)** either by using `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ or `Ovito <https://www.ovito.org/>`_. 

| See details below-

LAMMPS
~~~~~~
**1- If you are using LAMMPS** to perform PTM and calculate quaternion angles, use the *ptm/atom* command. An example is provided below; however, for a detailed description, please check the `LAMMPS command page for PTM <https://docs.lammps.org/compute_ptm_atom.html>`_.

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

Ovito
~~~~~~
**2- If you are using Ovito** to perform PTM and calculate quaternion angles, use the *Polyhedral Template Matching* modifier in Ovito. For the **GUI** version of Ovito, use the *Polyhedral Template Matching* modifier and export the file in the *lammps dump* format. We recommend using Ovito python script to generate quaternions for single or all snapshots. *You might need the pro version of Ovito for this. If that is a challenge, please use LAMMPS*

We provide a short example to calculate quaternion angles using Ovito python scripting, for detail understanding check `Ovito PTM modifier <https://www.ovito.org/docs/current/python/modules/ovito_modifiers.html#ovito.modifiers.PolyhedralTemplateMatchingModifier>`_.

For example:

.. code-block:: python

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

The example directory contains a python script to carry out PTM for all snapshots using *for loop*. The directory also includes an example *bash* submission file to submit the job if you use HPC. Check here

Cautions
~~~~~~~

1. VirTex is written in python, heavily inspired by the I/O of `pyMAINS <https://github.com/mrcavam/pyMAINS>`_ to read and write dump/data files, which uses `pandas <https://pandas.pydata.org/>`_ library to avoid the use of *for loops* while performing analysis on big atomistic microstructures. Thus, we recommend users should have/get a basic understanding of pandas. It is very intuitive; however, if needed, please check pandas `cheat sheet <https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf>`_.

2. For the current version of VirTex, your atomistic dump file should have quaternion angles named as follows-

.. code-block:: python

	'orientationx', 'orientationy', 'orientationz', 'orientationw'

Otherwise, it would not utilize appropriate columns to calculate texture properties. One option to avoid such constrain is to rename columns after reading dump files in python. *We promise to fix this in an upcoming version.*


Installation
------------

To use VirTex, first install it using pip:

.. code-block:: console

   pip install virtex

..
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

