==============
Exercise 3.3.6
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Recall the program Fahrenheit->Celsius from exercise 2.2.1. 
The program consumes a temperature 
measured in Fahrenheit and produces the Celsius equivalent.
Develop the program Celsius->Fahrenheit, which consumes a 
temperature measured in Celsius and produces the Fahrenheit equivalent.


Solution
========

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

;;Test
(define result  (I 100))
(print result)
;;Result -> 100
