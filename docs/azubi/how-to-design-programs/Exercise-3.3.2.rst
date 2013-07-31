==============
Exercise 3.3.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Develop the program volume-cylinder. It consumes the radius of a 
cylinder's base disk and its height; it computes the volume of the cylinder.

Solution
========

#lang racket

(define PI 3.14)

(define (calculate-volume-cylinder r h)
  (define base (* r r PI))
  (* base h)
)
