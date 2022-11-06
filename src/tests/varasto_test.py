import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    def setUp(self):
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)
    
    def test_konstruktori_ei_luo_alle_tyhjaa_varastoa(self):    ##
        miinus_varasto = Varasto(10, -1)
        self.assertAlmostEqual(miinus_varasto.saldo, 0) 
    
    def test_konstruktori_ei_liian_pienta_varastoa(self):    ##!!?!??
        miinusvarasto = Varasto(0)                              
        self.assertAlmostEqual(miinusvarasto.saldo, 0)      ## jos alle esim.-10 --> 0??? 
                                                            ## koska tilavuus eikä self.tilavuus
    
    def test_ylimaarainen_hukkaan_luodessa(self):
        ylivarasto = Varasto(10, 12)
        self.assertAlmostEqual(ylivarasto.saldo, 10)

    def test_uudella_varastolla_oikea_tilavuus(self):       
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ei_lisata_negatiivista(self):
        self.varasto.lisaa_varastoon(-5)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 10)

    def test_ylimaarainen_lisays_tayttaa_varaston(self):
        self.varasto.lisaa_varastoon(15)
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 0)
        self.assertAlmostEqual(self.varasto.saldo, 10)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_ei_neg_ottamista(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(-3)
        # tila 10 - 5 ((-3)ei poisteta tai lisätä) = 5
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 5)

    def test_tyhjenna_varasto(self):
        self.varasto.lisaa_varastoon(5)
        self.varasto.ota_varastosta(8)
        # saldo 0 + 5 -(8)(kaikki mitä on) = 0
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_palauttaa_oikean_str(self):
        self.varasto.lisaa_varastoon(4)
        self.assertEqual(str(self.varasto), "saldo = 4, vielä tilaa 6")