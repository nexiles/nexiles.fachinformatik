==============
Exercise 3.1.2
==============

:date: |today|
:author: Jan Börner

Task to solve
=============


Use the results of exercise 3.1.1 to determine how much it costs to run a show at $3.00, $4.00, and $5.00.
Also determine how much revenue each show produces at those prices.
Finally, figure out how much profit the monopolistic movie owner can make with each show.
Which is the best price (of these three) for maximizing the profit?


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
        (+ (* (nummber-of-attendes ticket-price) 0.04) 180)
    )
    ;;revenue : dollar -> revenue we will make
    ;;to compute the revenue in ref to the ticket price
    ;;the function takes the ticket price in dollar.
    ;;this function applies just for a ticket price <= 5.8 Dollar.
    ;;this function is using the nummber-of-attendes and
    ;;costs function as a helper funtion.
    (define (revenue ticket-price)
        (- (* ticket-price (nummber-of-attendes ticket-price)) (costs ticket-price))
    )



Testing
-------

::
    >(revenue 5)
    415.2
    >(revenue 4)
    889.2
    >(revenue 3)
    1063.2
