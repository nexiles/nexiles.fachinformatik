==============
Exercise 3.3.4
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Develop the program height, which computes 
the height that a rocket reaches in a given amount of time. 
If the rocket accelerates at a constant rate g, it reaches a 
speed of g · t in t time units and a height of 1/2 * v * t 
where v is the speed at t.



Solution (not solved yet)
=========================

;;name of programm height -> calculates a height that a rocket can reach
;;
;;accelaration is a constant g
;;speed is g * t(time)
;;height is 1/2 * v(speed at time t) * t 

#lang racket

(define (height-of-rocket accelaration time)
  
  (define speed (* accelaration time))
  (* 0.5 speed time)
  
)



