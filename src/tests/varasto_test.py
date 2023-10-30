import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_tilavuus_nollataan(self):
        self.varasto = Varasto(-1)
        self.assertEqual(self.varasto.tilavuus, 0.0)

    def test_alku_saldo_virheellinen(self):
        self.varasto = Varasto(1, -1)
        self.assertEqual(self.varasto.saldo, 0.0)

    def test_lisaa_maara_negatiivinen(self):
        self.varasto.lisaa_varastoon(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_lisays_saldo_ei_ylity(self):
        self.varasto.lisaa_varastoon(11)
        self.assertEqual(self.varasto.saldo, 10)

    def test_ottaminen_jos_maara_negatiivinen(self):
        self.varasto.ota_varastosta(-1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_otetaan_kaikki_varastosta(self):
        self.varasto.ota_varastosta(1)
        self.assertEqual(self.varasto.saldo, 0)

    def test_tulostaa_tiedot_oikein(self):
        varasto = Varasto(10)
        odotettu_merkkijono = f"saldo = {varasto.saldo}, vielä tilaa {varasto.paljonko_mahtuu()}"
        self.assertEqual(str(varasto), odotettu_merkkijono)