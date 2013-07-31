==============
Exercise 3.1.3
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

After studying the cost structure of a show, the owner discovered several ways of
lowering the cost. As a result of his improvements, he no longer has a fixed cost.
He now simply pays $1.50 per attendee.
Modify both programs to reflect this change. When the programs are modified, test
them again with ticket prices of $3.00, $4.00, and $5.00 and compare the results.

Solution
========

We know that by a price of 5$ 120 attendes come.
And we alse know, that by a discount of a dime 15 people
more come.
==> p1(120/500)   p2(135/490)

It is: y = mx+b
m = 490 - 500 / 135 - 120 = -2/3
p1 and m in y = mx + b
500 = -2/3(120) + b
b = 580
ticket-price = -2/3*nummber-of-attendes + 580
nummber-of-attendes = (ticket-price-580)/(-2/3)


::
    ;;nummber-of-attendes : dollar -> nummber of attendes
    ;;to coumpute the nummber of attendes in ref to the ticket price
    ;;the function takes the ticket price in dollar.
    ;;this function applies just for a ticket price <= 5.8 Dollar.
    (define (nummber-of-attendes ticket-price)
        (/ (- (* ticket-price 100) 580) -2/3)
    )
    ;;costs : dollar -> costs in ref to ticket price
    ;;to compute the costs in ref to the ticket price
    ;;the function takes the ticket price in dollar.
    ;;this function applies just for a ticket price <= 5.8 Dollar.
    ;;this function is using the nummber-of-attendes function as a
    ;;helper funtion.
    (define (costs ticket-price)
        (* (nummber-of-attendes ticket-price) 1.5) )
    )
    ;;revenue : dollar -> revenue we will make
    ;;to compute the revenue in ref to the ticket price
    ;;the function takes the ticket price in dollar.
    ;;this function applies just for a ticket price <= 5.8 Dollar.
    ;;this function is using the nummber-of-attendes and
    ;;costs function as a helper funtion.
    (define (profit ticket-price)
        (- (* ticket-price (nummber-of-attendes ticket-price)) (costs ticket-price))
    )



Testing
-------

::
    >(profit 5)
    415.2
    >(profit 4)
    889.2
    >(profit 3)
    1063.2
