==============
Exercise 2.2.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Define the program Fahrenheit->Celsius,6 which consumes a temperature
measured in Fahrenheit and produces the Celsius equivalent.
Use a chemistry or physics book to look up the conversion formula.

Solution
========

Formel
------
Celsius = ( TFahrenheit - 32 ) × 5 / 9

:source: http://de.answers.yahoo.com/question/index?qid=20070509082240AAxuQXp

Implementation
--------------
:
     >(define (fa_to_cel fa)
          (*(- fa 32)(/ 5 9))
      )
     >(fa_to_cel 61)
     16 1/9
