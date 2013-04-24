==============
Exercise 2.3.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

The local supermarket needs a program that can compute the value of a bag of coins.
Define the program sum-coins. It consumes four numbers: the number of pennies, nickels,
dimes, and quarters in the bag; it produces the amount of money in the bag.


Solution
========

100 pennis = 1 Dollar
20 nickles = 1 Dollar
4 quarters =  1 Dollar
10 dimes = 1 Dollar

:
    >(define (sum-coins pennis nickels dimes quarters)
        (+ (/ pennis 100) (/ nickels 20) (/ quarters 4) (/ dimes 10))
     )
