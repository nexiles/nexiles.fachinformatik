=====================
Das Amdahlsche Gesetz
=====================

Was ist das Amdahlsche Gesetz?
==============================

Das Amdahlsche Gesetzt besagt,
das die Anzahl von Kernen eines CPU'S,
nicht Proportinal zur Ausführung eines
Programms steht.

Begründung
==========

Der Grund zu dieser Annahme,
ist die Problematik die sich
beim Zerteilen von einem großen
Problem zu vielen kleinen Teilproblemen
ergibt.

Grund 1
-------

Prozesse sind von bestimmeten Ergebnissen
anderer Prozesse abhängig.
==> Blockierender Prozess.

Grund 2
-------

Prozesse sind in einer Form voneinander Abhängig.
Daraus ergibt sich, dass Prozesse in Gruppen geteilt
werden, welche entweder, von einander abhängen, oder
parralel zueinander laufen können.

Beispiel
========

Angenommen, ein Programm benötigt 20 Stunden
auf einem Rechner mit einer CPU,
und eine Stunde davon wird sequentiell
ausgeführt (beispielsweise Initialisierungs-Routinen
oder Speicher-Allokation).
Die verbleibenden 19 Stunden machen 95 % des
Gesamtaufwandes aus und können auf beliebig
viele Prozessoren verteilt werden.
Die Gesamtrechenzeit kann aber selbst mit unendlich
vielen Prozessoren nicht unter 1 Stunde fallen, die maximale
Beschleunigung (SpeedUp) ist also Faktor 20.
