Não Sei o Nome a por(v1.0)
==================

Copyright (C) <2020> by João Vitor Coelho Estrela

.. image:: 
  :target: 
  
.. image:: 
   :target: 
   
.. image:: 
   :target: 
   
- **Documentation:** 
- **Source:** 
- **Bug Reports:** 
- **PyPI Homepage:** 

Introduction
------------
Mussum Ipsum, cacilds vidis litro abertis. Detraxit consequat et quo num tendi nada. Admodum accumsan disputationi eu sit. Vide electram sadipscing et per. Não sou faixa preta cumpadi, sou preto inteiris, inteiris. Todo mundo vê os porris que eu tomo, mas ninguém vê os tombis que eu levo!

Interagi no mé, cursus quis, vehicula ac nisi. Interessantiss quisso pudia ce receita de bolis, mais bolis eu num gostis. Pra lá , depois divoltis porris, paradis. Per aumento de cachacis, eu reclamis.

Install
-------
Installation with ``pip``
::

    $ pip install xx
    
or ``conda``
::

    $ conda install xx
    
Simple Example
--------------

This is a simple example for the detection of `sturctural hole spanners <https://en.wikipedia.org/wiki/Structural_holes>`_ 
using the `HIS <https://keg.cs.tsinghua.edu.cn/jietang/publications/WWW13-Lou&Tang-Structural-Hole-Information-Diffusion.pdf>`_ algorithm.

.. code:: python

  >>> from pacote1_raiz import FireFly
  >>> from pacote1_raiz import Pop, Abc, Pso, Sa


  >>> nPop = 10
  >>> nGen = 50
  >>> ranges = np.array([[-50, 50]]*10)
  >>> fun = rastrigin

  >>> meta1 = Pso()
  >>> meta2 = FireFly()
  >>> meta3 = Abc()
  >>> meta4 = Sa()
  
  >>> nRep = 100
  >>> metas = {'Abc': [Pop(meta3, fun, ranges, int(nPop/2), nGen) for r in range(nRep)],
  >>>          'Pso': [Pop(meta1, fun, ranges, nPop, nGen) for r in range(nRep)],
  >>>          'FA': [Pop(meta2, fun, ranges, nPop, nGen) for r in range(nRep)],
  >>>          'Sa': [Pop(meta4, fun, ranges, nPop, nGen) for r in range(nRep)]
  >>>        }

  >>> for k, reps in tqdm(metas.items()):
  >>>     for r in reps:
  >>>         for g in range(1, nGen):
  >>>             next(r)

  >>>for k, v in metas.items():
  >>>    bestRep = min(v, key=lambda m: m.pBest['value'][-1])
  >>>   
  >>>    print('%s:' %k)
  >>>    print(bestRep.pBest['ch'][-1])
  >>>    print('FO:', bestRep.pBest['value'][-1])
  >>>    print()
	
  Abc:
  [ 0.015 -1.026  0.135 -0.101  1.029 -0.07  -0.914  1.877  2.029 -2.881]
  FO: 25.642901925010136

  Pso:
  [ 0.     2.876 -5.359 -2.134 -2.459  9.951  0.    -5.076  3.268  0.421]
  FO: 257.00225268553163

  FA:
  [ 1.231 -2.834 -3.036 -7.618  0.344  2.142 -1.208 -0.978 -4.705 -5.721]
  FO: 221.60138308242358

  Sa:
  [16.209 14.471  8.622  1.827 17.874 12.463 10.841  9.506 10.493 -9.399]
  FO: 1566.1422362748294