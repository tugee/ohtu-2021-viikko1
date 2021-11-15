"""
Runs unit tests on the inventory management software
"""

import unittest
from varasto import Varasto


class TestVarasto(unittest.TestCase):
    """
    Class containing all tests to run
    """
    def setUp(self):
        """
        Initializes the test inventory
        """
        self.varasto = Varasto(10)

    def test_konstruktori_luo_tyhjan_varaston(self):
        """
        Tests constructor
        """
        # https://docs.python.org/3/library/unittest.html#unittest.TestCase.assertAlmostEqual
        self.assertAlmostEqual(self.varasto.saldo, 0)

    def test_uudella_varastolla_oikea_tilavuus(self):
        """
        Tests correct volume
        """
        self.assertAlmostEqual(self.varasto.tilavuus, 10)

    def test_lisays_lisaa_saldoa(self):
        """
        Tests adding to inventory
        """
        self.varasto.lisaa_varastoon(8)

        self.assertAlmostEqual(self.varasto.saldo, 8)

    def test_lisays_lisaa_pienentaa_vapaata_tilaa(self):
        """
        Tests that adding to inventory correctly reduces amount available
        """
        self.varasto.lisaa_varastoon(8)

        # vapaata tilaa pitäisi vielä olla tilavuus-lisättävä määrä eli 2
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 2)

    def test_ottaminen_palauttaa_oikean_maaran(self):
        """
        Tests removing from inventory works
        """
        self.varasto.lisaa_varastoon(8)

        saatu_maara = self.varasto.ota_varastosta(2)

        self.assertAlmostEqual(saatu_maara, 2)

    def test_ottaminen_lisaa_tilaa(self):
        """
        Tests taking from inventory adds space
        """
        self.varasto.lisaa_varastoon(8)

        self.varasto.ota_varastosta(2)

        # varastossa pitäisi olla tilaa 10 - 8 + 2 eli 4
        self.assertAlmostEqual(self.varasto.paljonko_mahtuu(), 4)

    def test_not_add_overamount2(self):
        """
        Tests that inventory doesnt overflow
        """
        self.varasto.lisaa_varastoon(1222)
        self.assertAlmostEqual(self.varasto.saldo,self.varasto.tilavuus)

    def test_not_take_overamount(self):
        """
        Tests that cannot take more than is available
        """
        self.varasto.ota_varastosta(12)
        self.assertAlmostEqual(self.varasto.saldo,0)

    def test_valid_volume(self):
        """
        Tests that cannot initialize negative volume
        """
        self.varasto = Varasto(-1)
    def test_valid_saldo(self):
        """
        Tests that no negative space can be initialized
        """
        self.varasto = Varasto(2,-1)

    def test_not_negative_add(self):
        """
        Tests that user cant add negative amount
        """
        self.varasto.lisaa_varastoon(-1)
    def test_not_negative_take(self):
        """
        Tests cannot take negative amount
        """
        self.varasto.ota_varastosta(-1)

    def test_print(self):
        """
        Tests printing works
        """
        self.assertEqual(str(self.varasto),"saldo = 0, vielä tilaa 10")
