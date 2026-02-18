# Monte Carlo example and python programming

This is one of the classical and simplest example of a Monte Carlo simulation, the calculation of the area of a circle and the Pi number using Monte Carlo method.
The only assumption is that the area of a square is known.

We provide here two different algorithms for the same calculation: simple direct Monte Carlo and Markov chain Monte Carlo.
The implementations are provided in pyhton3 scripts and Google Colab notebooks.

The convergence folder provides an example of the performance of the algorithms as we increase the number of attemps.

The algorithms are an implementation of Algorithm 1.1 and 1.2 from the book by W Krauth "Statistical Mechanics Algorithms and Computations" Oxford University press (see book site [here](http://global.oup.com/booksites/content/9780198515364/)

For other similar implementations see for [example](https://gist.github.com/louismullie/3769218 and many others) (see also the animated gif in [Wikipedia MonteCarlo article](https://en.wikipedia.org/wiki/Monte_Carlo_method) ).

The implementation provided here shows a plot illustrating the number of succesful attemps that launched over a circle for pedagogical purposes.

We also provide a simple code that plots a circle inside a unit square (used for the graphical part of the code)
