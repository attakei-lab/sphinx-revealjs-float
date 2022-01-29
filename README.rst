sphinx-revealjs-float
=====================

Experimental add-ons for ``sphinx-revealjs``

Overview
--------

This is sphinx extension to implement small syntax likely "Grid Layouts" from GitPitch with sphinx-revealjs.

.. note::

   * This is feature for only "sphinx-revealjs" but splitted from it because experimentals.
   * There is probability to change directive name. (current: ``revealjs-float``)

Install
-------

This is not registered in PyPI.

.. code-block:: console

   $ pip install https://github.com/attakei-lab/sphinx-revealjs-float/archive/refs/heads/development.zip

.. code-block:: python

   extentions = [
       "sphinx_revealjs",
       "sphinx_revealjs_float",
   ]

Usage
-----

Please demo presentation source and build at localmachine (please see ``docs`` directory).

HTML demo is `here <https://attakei-lab.github.io/sphinx-revealjs-float/>`_

Refs
----

* `Description for Grid Layouts from GitPitch <https://gitpitch.github.io/gitpitch/#/grid-layouts/>`_
* `Documentation of sphinx-revealjs <https://sphinx-revealjs.readthedocs.io/>`_
