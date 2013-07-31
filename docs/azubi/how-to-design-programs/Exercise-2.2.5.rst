==============
Exercise 2.2.5
==============

:date: |today|
:author: Jan Börner

Task to solve
=============
A typical exercise in an algebra book asks the reader to evaluate an expression like

n/3 + 2

for n = 2, n = 5, and n = 9. Using Scheme, we can formulate such an expression as a program and use the program as many times as necessary.
Here is the program that corresponds to the above expression:

(define (f n)
  (+ (/ n 3) 2))
First determine the result of the expression at n = 2, n = 5, and n = 9 by hand, then with DrScheme's stepper.

Also formulate the following three expressions as programs:

1) n2 + 10

2) (1/2) · n2 + 20

3) 2 - (1/n)

Determine their results for n = 2 and n = 9 by hand and with DrScheme.


Solution
========


n*n + 10
-------

:
    >(define (task1 n)
     (+(* n n) 10)
     )
    >(task1 2)
    14
    >(task1 9)
    91


(1/2) * n*n + 20
---------------

:
    >(define (task2 n)
     (+(*(* n n) 0.5) 20)
     )
    >(taks2 2)
    22.0
    >(task2 9)
    60.5


2 - (1/n)
---------

:
    >(define (task3 n)
     (- 2 (/ 1 n))
     )
    >(task3 2)
    1 1/2
    >(task3 9)
    1 8/9
