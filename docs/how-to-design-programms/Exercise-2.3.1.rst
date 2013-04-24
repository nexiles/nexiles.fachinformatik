==============
Exercise 2.3.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Utopia's tax accountants always use programs that compute income taxes even though the tax rate is a solid,
never-changing 15%. Define the program tax, which determines the tax on the gross pay.

Solution
========

:
    >(define (tax grosspay)
     (* 0.85 grosspay)
     )
