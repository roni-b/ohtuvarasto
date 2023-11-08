class Varasto:
    """
    Luokka mallintaa varastoa ja tarjoaa metodit sen käsittelyyn.
    """
    def __init__(self, tilavuus, alku_saldo = 0):
        """
        Varaston konstruktori.

        Args:
            tilavuus (float): Varaston tilavuus.
            alku_saldo (float, optional): Alkusaldo varastolle.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = tilavuus

    def paljonko_mahtuu(self):
        """
        Palauttaa määrän, kuinka paljon tavaraa varastoon mahtuu.

        Returns:
            float: Määrä, kuinka paljon tavaraa mahtuu varastoon.
        """
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Lisää tavaraa varastoon.

        Args:
            maara (float): Määrä, joka lisätään varastoon.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Ottaa tavaraa varastosta.

        Args:
            maara (float): Määrä, joka otetaan varastosta.

        Returns:
            float: Palauttaa otetun määrän, tai 0.0.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """
        Palauttaa varaston tilan merkkijonona.

        Returns:
            str: Varaston tila muodossa "saldo = <saldo>, vielä tilaa <tila>".
        """
        return f"saldo = {self.saldo}, vielä tilaa {self.paljonko_mahtuu()}"
