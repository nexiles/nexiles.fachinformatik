==============
Exercise 4.2.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Translate the following equations into Scheme functions:

4 · n + 2 = 62

2 · n2 = 102

4 · n2 + 6 · n + 2 = 462

Determine whether 10, 12, or 14 are solutions of these equations. 

Solution
========

#lang racket


(define (formel1 n)
   (= (+ (* 4 n) 2) 62)
)

(define (formel2 n)
   (= (* 2 (* n n))102)
)

(define (formel3 n)
    (=
         (+ (* (* n n )4) (* 6 n) 2) 462
    )
)


;; Testing formel1

(print (formel1 10))

(print (formel1 12))

(print (formel1 14))

;;Testting formel2

(print (formel2 10))

(print (formel2 12))

(print (formel2 14))

;; Testting formel3 

(print (formel3 10))

(print (formel3 12))

(print (formel3 14))
