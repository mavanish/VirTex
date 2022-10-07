Welcome to VirTex's documentation!
===================================

**VirTex** is a Python library for performing virtual texture analysis for atomistic dataset
Such as, calculatiing rotation matirx, Euler angles, orientation, misoirnetation, Schmid Factor, etc.

It reads dump files from `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ with pre-calculated quartonion angles from `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ or `Ovito <https://www.ovito.org/>`_ and calculate all texture related properties. VirTex offers set of *simple* and *intuitive* python scripts (**In current form**).   

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

.. note::

   This project is under active development.

Citing
======

If VirTex helps in your research please cite the following paper.

.. code-block:: bibtex

  @article{mishra2022virtual,
    title={Virtual texture analysis to investigate the deformation mechanisms in metal microstructures at the atomic scale},
    author={Mishra, Avanish and Echeverria, Marco J and Ma, Ke and Parida, Shayani and Chen, Ching and Galitskiy, Sergey and Dongare, Avinash M},
    journal={Journal of Materials Science},
    pages={1--20},
    year={2022},
    publisher={Springer}
  }
..
   Contents
   --------

.. toctree::
   :hidden:
   
   about
   usage
   Tutorials
   Teams
   api
   citing
