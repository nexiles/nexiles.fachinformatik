==============
Exercise 2.2.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Define the program dollar->euro, which consumes a number of dollars and produces the euro equivalent.
Use the currency table in the newspaper to look up the current exchange rate.

:source: http://www.umrechnung.org/waehrungskurse-heutige/tages-aktueller-devisenkurse.htm

Solution
========

::

    >(define (dollar->euro dollar)
     ;1 euro -> 1.2992 us-dollar
     (/ dollar 1.2992)
     )
    >(dollar->euro 1.2992)
    1.0
