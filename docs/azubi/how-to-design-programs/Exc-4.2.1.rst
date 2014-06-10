==============
Exercise 4.2.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

Translate the following five intervals on the real line into Scheme functions that accept a
number and return true if the number is in the interval and false if it is outside

Solution
========

;;the interval [3,7]
(define (interval-1 number)
  (and (<= number 7) (>= number 3))
)
;;Test with 5 should be true
(print (interval-1 5))

;;the interval (3, 7]
(define (interval-2 number)
  (and (> number 3) (<= number 7))
)
;;Test with 8 should be false
(print (interval-2 8))

;;the interval [3, 9)
(define (interval-3 number)
  (and (>= number 3) (< number 9))
)
;;Test with 6 should be true
(print (interval-3 6))

;;the union (1, 3) and (9,11)
(define (interval-4 number)

  (or
    (and (< number 3) (> number 1)  )
    (and (< number 11) (> number 9 ) )
  )
)

;;Test with 2 should be true
(print (interval-4 2))

;;the range outsite of [1, 3]
(define (interval-5 number)
  (or (<= number 1) (>= number 3))
)
;;Test with 4 should be true
(print (interval-5 4))
