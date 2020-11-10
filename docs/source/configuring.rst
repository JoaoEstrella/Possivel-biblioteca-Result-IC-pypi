Configuração
*************

Como usar
=========

No arquivo ``main.py``:

.. code:: python

	from pacote1_raiz import Pop, Abc

	nPop = 10
	nGen = 50
	ranges = np.array([[-50, 50]]*10)
	fun = rastrigin

	meta = Abc()
	  
	abc = Pop(meta, fun, ranges, int(nPop/2), nGen)

Para iterar existem varias formas:

.. code:: python

	for g in range(1, nGen):
		next(abc)

Outra maneira é:

.. code:: python

	for gen in abc:
		pass

.. note::
    A geração ``nG=0`` é a população aleatória inicial. Enquanto que ``gen`` retorna o valor da melhor ``FO`` atual.