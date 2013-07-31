==============
Exercise 3.3.1
==============

:date: |today|
:author: Jan Börner

Task to solve
=============

The United States uses the English system of (length) measurements.
The rest of the world uses the metric system. So, people who travel
abroad and companies that trade with foreign partners often need to 
convert English measurements to metric ones and vice versa.
Here is a table that shows the six major units of length measurements 
of the English system.

Solution
========



#lang racket
(define inch 2.54)
(define foot (* inch 12)) ;; 30.48inch
(define yard (* foot 3)) ;; 91.44inch
(define rod (* 5.5 yard))
(define furlong (* 40 rod))
(define mile (* 8 furlong))


;; inches-to-cm _ inches -> cm
;; converts inches to cm
(define (inches-to-cm inches) 
  (* inch inches)
)
;; feet-to-inches: feet -> inch
;; converts feet to inch
(define (feet-to-inches feet_number)
  (* feet_number foot )  
)

;; yards-to-feet: -> number_of_yards -> feet
;; converts yards to feet
(define (yards-to-feet number_of_yards)
    (* number_of_yards  3)
)

;; rods-to-yards: -> number_of_rods -> yards
;; converts rods to yards
(define (rods-to-yards number_of_rods)
    (* number_of_rods 5.5)  
)

;; furlongs-to-rods: -> number_of_furlongs -> rods
;; converts furlongs to rods
(define (furlongs-to-rods number_of_furlongs)
    (* number_of_furlongs 40)  
)

;; miles-to-furlongs: -> number_of_miles -> furlongs
;; converts miles to furlongs
(define (miles-to-furlongs number_of_miles)
    (* number_of_miles 8)  
)

;; feet-to-cm: -> number_of_feet -> cm
;; converts feet to cm
(define (feet-to-cm number_of_feets)
 (* number_of_feets foot)  
)

;; yards-to-cm: -> number_of_yards -> cm
;; converts yard to cm
(define (yards-to-cm number_of_yards)
    (* number_of_yards yard)  
)

;; rods-to-inches: -> number_of_roads -> inches
;; converts rods to yards
(define (rods-to-inches number_of_rods)
     (/ (* number_of_rods rod)  inch)
)
;; miles-to-inches: -> number_of_miles -> feet  
;; converts miles to feets
(define (miles-to-feet number_of_miles)
     (/ (* number_of_miles mile) foot)
)

