Usage
=====

.. _installation:

Pre Processing
--------------
**Before you use VirTex**, generate quaternion for each atom in the microstructure either by **Polyhedral Template Matching (PTM)** using `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ or `Ovito <https://www.ovito.org/>`_. 

See detials below-

1-If you are using LAMMPS to pefrome PTM and calculate quaternion use *ptm/atom* command. Examples are provided below for detial check `LAMMPS command page for PTM <https://docs.lammps.org/compute_ptm_atom.html>`_.


.. code-block:: console

   $ compute ID group-ID ptm/atom structures threshold group2-ID

ID, group-ID are documented in compute command\  
ptm/atom = style name of this compute command\  
structures = default or all or any hyphen-separated combination of fcc, hcp, bcc, ico, sc, dcub, dhex, or graphene = structure types to search for\  
threshold = lattice distortion threshold (RMSD)\  
group2-ID determines which group is used for neighbor selection (optional, default “all”)  

For example:

   compute 1 all ptm/atom default 0.1 all  
   compute 1 all ptm/atom fcc-hcp-dcub-dhex 0.15 all  
   compute 1 all ptm/atom all 0  


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

