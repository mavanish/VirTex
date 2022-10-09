Welcome to VirTex's documentation!
===================================

**VirTex** is a Python library for performing virtual texture analysis for atomistic dataset
Such as, calculatiing rotation matirx, Euler angles, orientation, misoirnetation, Schmid Factor, etc.

It reads dump files from `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ with pre-calculated quartonion angles from `LAMMPS <https://www.lammps.org/#gsc.tab=0>`_ or `Ovito <https://www.ovito.org/>`_ and calculate all texture related properties. VirTex offers set of *simple* and *intuitive* python scripts (**In current form**).   

Check out the :doc:`usage` section for further information, including
how to :ref:`installation` the project.

VirTex is developed at `Department of Materials Science and Engineering <https://mse.engr.uconn.edu/>`_, and `Institute of Materials Science <https://www.ims.uconn.edu/>`_, `University of Connecticut <https://uconn.edu/>`_, CT, USA in the group of Prof. Avinash M Dongare (`Computational Materials and Mechanics Group <https://dongare.group.uconn.edu/>`_). The article associated with VirTex proposes its application for finding orientation, misorientation, and angle-axis pairs. Still, for the package release, it is extended to calculate the Schmid Factor and automatic identification of peaks in angle-axis pair distribution. VirTex will be released in 2022 as an open-source package. We welcome collaborators for future development of the package; we would also focus on developing VirTex sister packages. Sister packages of VirTex are `pyMAINS <https://github.com/mrcavam/pyMAINS>`_ (*python-pandas package to analyze MD data*) and VirDi (**Virtual diffraction package** is *under development*). 

.. note::

   This project is under active development. We are actively adding various other capabilities to calculate various other texture related properties for atomistic microstructure. The code is published on `Github <https://github.com/mrcavam/VirTex>`_.

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
