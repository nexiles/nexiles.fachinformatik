==============
Exercise 3.1.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

The next step is to make up examples for each of the functions. Determine how many attendees can afford a show at a ticket price of $3.00, $4.00, and
$5.00. Use the examples to formulate a general rule that shows how to compute the number of attendees from the ticket price.
Make up more examples if needed.

Solution
========

We know that by a price of 5$ 120 attendes come.
And we alse know, that by a discount of a dime 15 people
more come.
==> p1(120/500)   p2(135/490)

It is:: 

  y = mx+b
  m = 490 - 500 / 135 - 120 = -2/3
  p1 and m in y = mx + b
  500 = -2/3(120) + b
  b = 580
  ticket-price = -2/3*nummber-of-attendes + 580
  nummber-of-attendes = (ticket-price-580)/(-2/3)

scheme code::

   ;;nummber-of-attendes : number -> number
   ;;to coumpute the nummber of attendes in ref to the ticket price
   ;;the function takes the ticket price in dollar.
   ;;this function applies just for a ticket price <= 5.8 Dollar.
   (define (nummber-of-attendes ticket-price)
        (/ (- (* ticket-price 100) 580) -2/3)
   )

Testing
-------

``
;; attendes by a ticket price of 5$
(nummber-of-attendes 5)
120
;; attendes by a ticket price of 3$
(nummber-of-attendes 3)
420
;; attendes by a ticket price of 4$
(nummber-of-attendes 4)
270
``

