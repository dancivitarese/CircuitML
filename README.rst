.. -*- rst -*- 

CircuitML
=========

Package Description
-------------------
CircuitML is an extension to NeuroML 2.0 that enables one to define reusable
heterogeneous circuit motifs and connectivity patterns and use them to construct complex 
networks.

This package contains the following:

- An XML schema defining the CircuitML extensions to NeuroML 2.0. This schema
  defines the following major constructs:

  - subcircuit: a reusable heterogeneous circuit container.
  - interface: a subcircuit interface that enables addressing of circuit
    elements contributed by multiple constituent subcircuits via a unified namespace 
    specific to the outermost subcircuit.
  - connectivity: a synaptic connectivity pattern that describes connections
    between potentially heterogeneous elements in two subcircuits.
- A Python parser that extends libNeuroML [2] to enable processing of files containing
  CircuitML constructs.
- A libNeuroML backend for storing data specified using CircuitML to GPU-based
  data structures using PyCUDA [3].

Installation Instructions
=========================

Installation Dependencies
-------------------------

* `lxml <http://lxml.de/>`_ 2.3 or later.
* `NumPy <http://numpy.scipy.org>`_ 1.2.0 or later.
* `SciPy <http://numpy.scipy.org>`_ 0.11.0 or later.
* `libNeuroML <https://github.com/NeuralEnsemble/libNeuroML>`_ 0.1.9 or later.
* `PyCUDA <http://mathema.tician.de/software/pycuda>`_ 2011.1.2 or
  later.

.. [1] http://neuroml.org/neuroml2.php
.. [2] https://github.com/NeuralEnsemble/libNeuroML
.. [3] http://mathema.tician.de/software/pycuda
