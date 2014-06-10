==============
Exercise 4.4.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Exercise 4.4.2.   Develop the function tax, which consumes the gross pay and 
produces the amount of tax owed. For a gross pay of $240 or less, the tax is 
0%; for over $240 and $480 or 
less, the tax rate is 15%; and for any pay over $480, the tax rate is 28%.

Also develop netpay. The function determines the net pay of an employee from the 
number of hours worked. The net pay is the gross pay minus the tax. Assume the
hourly pay rate is $12.

Solution
========

#lang racket

(define (test function value expect)
  (= (function value) expect)
)

    
(define (tax income)

  (cond

    [(and (<= income 240 ) (>= income 0)) 0]

    [(and (<= income 480 ) (> income 240)) (* income 0.15)]

    [(> income 480) (* income 0.28)]

  )

)

(define (netpay hourse)

  (define pay (* hourse 12))
  (define  taxes (tax pay))
  (- pay taxes)

)

;;Test1 should be true
(test tax 200 0)
;;Test2 should be false
(test tax 500 70)
