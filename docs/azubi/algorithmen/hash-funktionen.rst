===============
Hash Funktionen
===============


Was ist eine Hash-Funktion?
===========================

Eine Funktion die eine große Eingebamenge
auf eine kleinere Zielmenge (Hahswert) abbildete.
Dabei kann die Eingabemenge auch Elemente mit
unterschiedlichen Längen enthalten,die Elemente
der Zielmenge haben dagegen meist eine feste Länge.
Die Zielmenge ist nicht eindeutig umkehrbar.

Grundsätzliche Funktionalität
=============================

Die grundsätzliche funktionalität einer Hash-Funktion,
bassiert auf dem nicht wieder eindeutig umkehbaren Verändern der Eingabedaten.
Das Resultat sind Ausgabedaten, die unabhängig von der Länge der Eingabedaten
Konsistent in ihrer Länge sind.



Kolisionen von Hashwerten
=========================

Eine Kolision kommt vor, wenn zwei verschiedene Eingabedaten den
gleichen Hashwert besitzen. Der Grund für dieses Phänomen ist die
Tatsache, dass der Werte Bereich der Hashfunktionen grundsätzlich
kleiner ist, als der Wertebereich der Eingabewerte.


Kriterien für eine gute Hash Funktion
=====================================


- Geringe Wahrscheinlcihkeit von Kollisionen.

- Eine geringe Änderung der Eingabedaten soll zu einer enormen Änderung der
  Ausgabedaten führen.

- Gleichverteilung auf die möglichen Hashwerte.

- Jeder Hashwert em definierten Wertebereich soll tatsächlich
  vorkommen können.

- Die Funktion sollte schnell berechenbar sein.


Ein kleines Beispiel
====================

Die folgende Hash Funktion (geschrieben in Python) liefert
einen Integerwert für einen String zurück.
::
    def hash_string(string):
        string_hex = string.encode('hex')
        nummber = int(string_hex, 16)
        modulo = [2,5,6,8,9,4,3,5,6,7,4,6,4,56,3,5,3,34]
        my_hash = 1
        m = 1
        for i in range(1,len(string_hex),1):
            try:
                mod = nummber % modulo[m]
                my_hash = my_hash + mod
                m = m + 1
            except:
                for u in range(1,my_hash,1):
                    tok = my_hash % u
                    my_hash = (tok * my_hash) % nummber
                m = 1
        return my_hash
