==============
Exercise 2.3.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

 An old-style movie theater has a simple profit function. Each customer pays $5
 per ticket.Every performance costs the theater $20, plus $.50 per attendee.
 Develop the function total-profit. It consumes the numberof attendees
 (of a show) and produces how much income the attendees produce.

Solution
========

profit = 4.5x - 20

;;profit: nummber -> nummber
;;calculate the profit of a event in ref to
;;the nummber of attendes
(define (profit attendes)
  (-(* 4.5 attendes) 20)
)
