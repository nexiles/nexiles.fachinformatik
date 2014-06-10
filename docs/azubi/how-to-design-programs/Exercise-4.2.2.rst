==============
Exercise 4.2.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

   Translate the following three Scheme functions into intervals on the line of 
   reals:

1. (define (in-interval-1? x)
       (and (< -3 x) (< x 0)))

2. (define (in-interval-2? x)
       (or (< x 1) (> x 2)))

3. (define (in-interval-3? x)
       (not (and (<= 1 x) (<= x 5))))

Solution
========

1. (-3, 0)

2. alle R ausgesclossen {[1, 2]}

3. alle R augeschlossen {[1, 5]}
