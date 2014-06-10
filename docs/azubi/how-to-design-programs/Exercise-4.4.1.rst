==============
Exercise 4.4.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Develop the function interest. Like interest-rate, it consumes a deposit amount.
Instead of the rate, it produces the actual amount of interest that the money
earns in a year. The bank pays a flat 4% for deposits of up to $1,000, a flat
4.5% per year for deposits of up to $5,000, and a flat 5% for deposits of more
than $5,000.

Solution
========

#lang racket

(define (test function value expect)
  (= (function value) expect)
)


(define (interest amount)
  
 (cond 
   [(and (<= amount 1000) ( > amount 0)) (* amount 0.04 )]
   [(and (> amount 1000) (<= amount 5000)) (* amount 0.045 )]
   [(> amount 5000) (* amount 0.05 )]
   [else false]
  
  )
  
) 


;;Test1 should be true
(test interest 3000 135.0)
;;Test2 should be false
(test interest 4000 230.0)

