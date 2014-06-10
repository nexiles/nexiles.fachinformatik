===================
Was ist Bubblesort?
===================


Bubblesort ist ein sortier Algoryhtmus, der durch vergeliche ein Liste
nach einer Ordnungbedningung odnet.(Beispiel nach dem Größten).

Bubblesort arbeitet in-place! Das bedeutet, das der Algoyhtmus keinen
zusätzlichen Speicherplatz braucht, sondern die bereits besthenden
varaiblen der Eingabeliste verwendet.(Plus eine konstante, welche die länge der Liste beschreibt.)

Implementation von Bubblesort
==============================


def bubblesort(liste):
    length = len(liste)
    done = True
    while(done ==  True):
        done = False
        for l in range(0,length-1,1):
            temp = liste[l]
            if liste[l] > liste[l+1]:
                liste[l] = liste[l+1]
                liste[l+1] = temp
                done = True
    return liste


Berechnung von O(n)
===================

Die Dauer des Bubblesort Algoryhtmus ist von zwei Faktoren abhängig.

1) Die Länge der Liste ==> Umso mehr Elemente die Liste hat, desto mehr Vergleiche
müssen angesellt werden. Vergleiche pro Durchgang = n - 1. (Wobei n = die Elemenete
der Liste beschreibt)

2) Die Anzahl der Durchgänge. Dieser Faktor hängt von dem Ausgang der
zu ordnenden Liste ab. Umso besser der geordnete Ausgang der Liste ist, umso
weniger Durchgänge werden gebraucht.

Hier gibt es drei verschiedene Ausgangssituationen.

1. Schlechtester Fall: Durchgänge = n
2. Bester Fall: Durchgänge = 1
3. Durschnitt: Wird nicht betrachtet.


Warum Bubblesort schlecht ist
=============================

Ausgehend vom schlechtesten Fall ist O(n) = n*n-n.
Das bedeutet mit der Länge einer Liste, steigt die Anzahl der
Berechnungen enorm.

Die exiziens von Bubblesort steht und fällt mit der Ausgangssituation der Liste.
Umso durchmischter die Liste, desto größer O.

O is ein vielfaches

Formel
======

k = Durchgänge.
O(n) = k(n-1).



Eine bessere Alternative
========================

Als schnelle Alternative die in der Realtität meist angewandt wird dient Quicksort.

Quicksort funktioniert in dem man die zu ordnende Liste nach einem bestimmten Teiler (Das Pivoteelement) rekrusiv 
in Teillisten zerlegt und dann soritert.




Laufzeit
--------

Best Case = O(n*log(n))
Worst Case = O(n*n)
Average Case = O(log n)


