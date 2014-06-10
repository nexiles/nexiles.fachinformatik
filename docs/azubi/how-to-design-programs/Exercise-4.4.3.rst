==============
Exercise 4.4.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Exercise 4.4.3.   Some credit card companies pay back a small portion of the 
charges a customer makes over a year. One company returns

1) .25% for the first $500 of charges,

2) .50% for the next $1000 (that is, the portion between $500 and $1500),

3) .75% for the next $1000 (that is, the portion between $1500 and $2500),

4) and 1.0% for everything above $2500.


Thus, a customer who charges $400 a year receives 
$1.00, which is 0.25 · 1/100 · 400, and one who charges 
$1,400 a year receives $5.75, which is 1.25 = 0.25 · 1/100 · 500 
for the first $500 and 0.50 · 1/100 · 900 = 4.50 for the next $900.
Determine by hand the pay-backs for a customer who charged $2000 
and one who charged $2600.
Define the function pay-back, which consumes a charge amount and computes
the corresponding pay-back amount.

Solution
========

#lang racket

(define (pay-back charges)

  (cond

    [(<= charges 500) (* charges (* 0.25 (/ 1 100)))]

    [(and (> charges 500) (<= charges 1500)) 
         (+ (* 500 (* 0.25 (/ 1 100)))   ( * (- charges 500) (* 0.50 (/ 1 100))))]

    [(and (> charges 1500) (<= charges 2500))
         (+ (* 500 (* 0.25 (/ 1 100)))   ( * 1000 (* 0.50 (/ 1 100))) (* (- charges 1500) (* 0.75 (/ 1 100))) ) ]
    [(> charges 2500)
     (+ (* 500 (* 0.25 (/ 1 100)))   ( * 1000 (* 0.50 (/ 1 100))) (* 1000 (* 0.75 (/ 1 100))) (* (- charges 2500) (* 1 (/ 1 100))) )]

   )
)
