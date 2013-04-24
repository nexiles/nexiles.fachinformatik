==============
Exercise 2.2.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Define the program triangle. It consumes the length of a triangle's side and the perpendicular height.
The program produces the area of the triangle. Use a geometry book to look up the formula for computing
the area of a triangle.

Solution
========

A = 1/2c * h

:
    >(define (triangle_area g h)
        (*(* 0.5 g) h)
     )
    >(triangle_area 6 3)
    9.0
