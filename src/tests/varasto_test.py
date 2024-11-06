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


# rikotaan tämä testi
# korjataan myös :)

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

    def test_tilaton_tilavuus(self):
        self.varasto = Varasto(-1.0)
        self.assertAlmostEqual(self.varasto.tilavuus, 0)

    def test_negatiivinen_saldo(self):
        self.varasto = Varasto(10, -1.0)
        self.assertAlmostEqual(self.varasto.saldo, 0.0)

    def test_void_varastoon(self):
        maara_varastossa = self.varasto.saldo
        self.varasto.lisaa_varastoon(-1)
        nyt = self.varasto.saldo
        self.assertAlmostEqual(maara_varastossa, nyt)

    def test_liian_iso(self):
        mahtuu = self.varasto.paljonko_mahtuu()
        self.varasto.lisaa_varastoon(mahtuu+1)
        self.assertAlmostEqual(self.varasto.saldo, mahtuu)

    def test_tyhjaa_ei_voi_ottaa(self):
        maara = self.varasto.ota_varastosta(-1)
        self.assertAlmostEqual(maara, 0.0)

    def test_voi_ottaa(self):
        saldo = self.varasto.saldo
        maara = self.varasto.ota_varastosta(saldo+1)
        self.assertAlmostEqual(maara, saldo)

    def test_sanoo_oikein(self):
        oikea = f"saldo = {self.varasto.saldo}, vielä tilaa {self.varasto.paljonko_mahtuu()}"
        self.assertEqual(str(self.varasto), oikea)
