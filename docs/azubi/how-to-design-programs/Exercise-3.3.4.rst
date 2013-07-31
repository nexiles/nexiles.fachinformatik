==============
Exercise 3.3.4
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Develop the function area-pipe. It computes the surface area of a pipe, which 
is an open cylinder. The program consumes three values: the pipe's inner radius, 
its length, and the thickness of its wall.



Solution
========

#lang racket

(define (area-pipe radius height thickness)


  (define PI 3.14) ;; The konstant PI

  ;;calculates a kaminisims
  (define (calculate-surface-pipe r h)
      (define u (* 2 r PI))
      (* u h)
  )

  ;;calulates the bottom and the top
  (define (calculate-top-bottom inner_radius wall_thickness)
      (define (calculate-surface-of-circle r)
          (* r  r PI)
      )
     (* 2
        (-
         (calculate-surface-of-circle (+ inner_radius wall_thickness)) 
         (calculate-surface-of-circle inner_radius)
        )
      )
   )

  (+

      (calculate-top-bottom radius thickness) 
      (calculate-surface-pipe radius height) 
      (calculate-surface-pipe (- radius thickness) height)

   )


)
