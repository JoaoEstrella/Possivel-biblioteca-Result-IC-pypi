Installation
************

Install the package (or add it to your ``requirements.txt`` file):

.. code:: console

    $ pip install PACOTE

In your ``conf.py`` file:

.. code:: python

	from pacote1_raiz import Pop, Abc

	nPop = 10
	nGen = 50
	ranges = np.array([[-50, 50]]*10)
	fun = rastrigin

	meta = Abc()
	  
	abc = Pop(meta, fun, ranges, int(nPop/2), nGen)
	
	for g in range(1, nGen):
		next(abc)


.. note::
    A geração ``nG=0`` é a população aleatória.

Via Git or Download
===================

bla bla bla