******
|name|
******

.. image:: https://img.shields.io/pypi/v/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme
   :alt: Pypi Version
.. image:: https://travis-ci.org/readthedocs/sphinx_rtd_theme.svg?branch=master
   :target: https://travis-ci.org/readthedocs/sphinx_rtd_theme
   :alt: Build Status
.. image:: https://img.shields.io/pypi/l/sphinx_rtd_theme.svg
   :target: https://pypi.python.org/pypi/sphinx_rtd_theme/
   :alt: License
.. image:: https://readthedocs.org/projects/sphinx-rtd-theme/badge/?version=latest
  :target: http://sphinx-rtd-theme.readthedocs.io/en/latest/?badge=latest
  :alt: Documentation Status

This Sphinx_ theme was designed to provide a great reader experience for
documentation users on both desktop and mobile devices. This theme is used
primarily on `Read the Docs`_ but can work with any Sphinx project. You can find
a working demo of the theme in the `theme documentation`_

.. _Sphinx: http://www.sphinx-doc.org
.. _Read the Docs: http://www.readthedocs.org
.. _theme documentation: https://sphinx-rtd-theme.readthedocs.io/en/latest/

Installation
============

Este pacote está disponível no PyPI_ e é pode ser instalado com o ``pip``:

.. code:: console

   $ pip install |name|

A baixo é um pequeno exemplo de como utilizar diferentes algoritmos para um
dado problema:

.. code:: python

	from pacote1_raiz import FireFly
	from pacote1_raiz import Pop, Abc, Pso, Sa


	nPop = 10
	nGen = 50
	ranges = np.array([[-50, 50]]*10)
	fun = rastrigin

	meta1 = Pso()
	meta2 = FireFly()
	meta3 = Abc()
	meta4 = Sa()
	  
	nRep = 100
	metas = {'Abc': [Pop(meta3, fun, ranges, int(nPop/2), nGen) for r in range(nRep)],
			 'Pso': [Pop(meta1, fun, ranges, nPop, nGen) for r in range(nRep)],
			 'FA': [Pop(meta2, fun, ranges, nPop, nGen) for r in range(nRep)],
			 'Sa': [Pop(meta4, fun, ranges, nPop, nGen) for r in range(nRep)]
			}

	for k, reps in tqdm(metas.items()):
		for r in reps:
			for g in range(1, nGen):
				next(r)

	for k, v in metas.items():
		bestRep = min(v, key=lambda m: m.pBest['value'][-1])
	   
		print('%s:' %k)
		print(bestRep.pBest['ch'][-1])
		print('FO:', bestRep.pBest['value'][-1])
		print()
		
Para mais informações consulte a pagina de instalação

.. _PyPI: https://pypi.python.org/pypi

Configuration
=============

This theme is highly customizable on both the page level and on a global level.
To see all the possible configuration options, read the documentation on
`configuring the theme`_.

.. _configuring the theme: https://sphinx-rtd-theme.readthedocs.io/en/latest/configuring.html

Contributing
============

If you would like to help modify or translate the theme, you'll find more
information on contributing in our `contributing guide`_.

.. _contributing guide: https://sphinx-rtd-theme.readthedocs.io/en/latest/contributing.html

.. |name| replace:: Biblioteca do Joao