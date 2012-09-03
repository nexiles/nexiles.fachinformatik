======================
nexiles.fachinformatik
======================

:Autor: nexiles GmbH
:Datum: 03.09.2012


Einleitung
==========

Dies ist das nexiles.fachinformatik Repository.

Es beinhaltet unter Anderem den IHK Ausbildungsrahmenplan, beschreibt die
Projekte um Lerninhalte aus dem Rahmenplan zu vermitteln und definiert die
Ziele die erreicht werden müssen.

Alle ausbildungsspezifischen Inhalte können in diesem Repository gesammelt
werden.


Konventionen
============

Diese Dokumentation ist in deutscher Sprache.
Die Dokumentation wird in restructuredText geschrieben und mit Sphinx
generiert.


Schnellstart
============

1. Repository clonen::

    $ mkdir -p ~/develop/nexiles
    $ cd ~/develop/nexiles
    $ git clone git@github.com:nexiles/nexiles.fachinformatik.git

2. Virtualenv erstellen::

    $ mkvirtualenv nexiles.fachinformatik

3. Requirements installieren::

    $ pip install -r requirements.txt

4. Dokumentation erstellen::

    $ cd docs
    $ make html


Links
=====

**nexiles.fachinformatik Repository**
    https://github.com/nexiles/nexiles.fachinformatik

**IHK**
    http://www.weingarten.ihk.de

**Sphinx**
    http://sphinx.pocoo.org

**restructuredText**
    http://sphinx.pocoo.org/rest.html

..  vim: set ft=rst tw=75 nocin nosi ai sw=4 ts=4 expandtab:
