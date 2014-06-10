==============
Exercise 4.2.4
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Exercise 4.2.4.   Equations are not only ubiquitous in mathematics, they are also 
heavily used in programming. We have used equations to state what a function 
should do with examples, we have used them to evaluate expressions by hand, 
and we have added them as test cases to the Definitions

Solution
========

#lang racket


(define (test function value expect) 
    (=(function value) expect)
)

;;celsius -> Fahrenheit
;;this function produce the fahrenheit eqvivalent to celsius

(define (celsius-to-fahrenheit celsius)

  ;;1celsius = 2,12 Fahrenheit
  (* celsius 2.12)

)

(define (fahrenheit-to-celsius fahrenheit)
  (/ fahrenheit 2.12)
)


(define (I f)
  (celsius-to-fahrenheit (fahrenheit-to-celsius f))
)

;;Test should false
(test I 100 80)

;;Test should be true
(test celsius-to-fahrenheit 100 212)



