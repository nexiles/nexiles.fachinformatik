======================
Interfaces und Adapter
======================

:date: 9-08-2013
:author: Jan Börner

Interfaces
==========

Grundlegende Definition
-----------------------

Ein Interface definert bestimmte eigenschaften und Methoden
die in unterschiedlichen Klasse implementiert seien müssen!

Was machen Interfaces in der OOP?
---------------------------------

Schnittstellen bieten eine Garantie bezüglich bestimmter
Methoden einer Klasse wenn diese Klasse das bestimmte Interface
implementiert. Daraus folgt, das jedes Objeckt einer solchen
Klasse gleich behandelt werden kann.

Warum das Nutzen von Interfaces?
--------------------------------

1) In Programmiersprachen die keine Mehrfachvererbung unterstützen können Interfaces
   genutzt werden um Kompatibilität zwischen Klassen zu bieten die nicht von einander
   erben.

Adapter
=======

Grundlegende Definition
------------------------

Ein Adapter dient zur Übersetzung einer Schnittstelle von Klassen die inkompatible
Interfaces implementieren.


Anwendung
---------

Ein Adapter wird verwendet, wenn eine existierende Klasse verwendet werden soll,
deren Schnittstelle nicht der benötigten Schnittstelle enspricht.
Ein Adapter soll die Möglichkeit bieten einen zentrall gekopelten Punkt zwischen
zwei System zu bieten.




Ein Beispiel
============

from zope import interfaces


class IPerson(interface.Interface):

