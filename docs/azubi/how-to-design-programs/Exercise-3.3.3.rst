==============
Exercise 3.3.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Develop area-cylinder. The program consumes the radius of the cylinder's base 
disk and its height. Its result is the surface area of the cylinder.

Solution
========

#lang racket

(define PI 3.14)

(define (calculate-surface-cylinder r h)
    (define base (* 2 (* r r PI))) ;; bottom and top
    (define body (* h (* 2 PI r )) ) ;; 
    (+ base body) ;; in addition the surface 
)
