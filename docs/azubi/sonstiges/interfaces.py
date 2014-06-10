from zope.interface import Interface
from zope.interface import implements


class IMensch(Interface):

    def __inti__(self, name, vorname, geschlecht, wohnort, beruf):
        """Basis Inforamtion eines Menschens"""

    def sprechen(self, satz):
        """Jeder Mensch 'kann' sprechen"""

    def laufen(self):
        """Jeder Mensch 'kann' laufen"""

    def essen(self):
        """Jeder Mensch muss essen"""

    def trinken(self):
        """Jeder Mensch muss trinken"""

    def schlafen(self):
        """Jeder Mensch muss schlafen"""

class IMenschStum(Interface)

    def __init__(self, name, vorname, geschlecht, wohnort, beruf):
        """Basis Inforamtion eines Menschens"""

    def laufen(self):
        """Jeder Mensch 'kann' laufen"""

    def essen(self):
        """Jeder Mensch muss essen"""

    def trinken(self):
        """Jeder Mensch muss trinken"""

    def schlafen(self):
        """Jeder Mensch muss schlafen"""

class MenschZuStumAdapter():
    implements(IMenschStum)
    __used_for_ = IMensch

    




class Man():
    implements(IMensch)

    def __init__(self, name, vorname, geschlecht, wohnort, beruf):
        """initialisierung
        """
        self.name = name
        self.vorname = vorname
        self.geschlecht = "man"
        self.wohnort = wohnort
        self.beruf = beruf

    def sprechen(self, satz):
        print satz

    def laufen(self):
        pass

    def essen(self):
        pass

    def trinken(self):
        pass

    def schlafen(self):
        pass


class Frau():
    implements(IMensch)

    def __init__(self, name, vorname, geschlecht, wohnort, beruf):
        """initialisierung
        """
        self.name = name
        self.vorname = vorname
        self.geschlecht = "weiblich"
        self.wohnort = wohnort
        self.beruf = beruf

    def sprechen(self, satz):
        print satz

    def laufen(self):
        pass

    def essen(self):
        pass

    def trinken(self):
        pass

    def schlafen(self):
        pass
