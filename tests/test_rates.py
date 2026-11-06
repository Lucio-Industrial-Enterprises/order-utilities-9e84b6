import unittest

from warehouse.rates import shipping_quote


class StandardRateTests(unittest.TestCase):
    def test_standard_rates(self):
        self.assertEqual(shipping_quote(2, "local"), 8.0)
        self.assertEqual(shipping_quote(2, "regional"), 11.0)

    def test_standard_explicit_service(self):
        self.assertEqual(shipping_quote(2, "local", service="standard"), 8.0)
        self.assertEqual(shipping_quote(2, "regional", service="standard"), 11.0)

    def test_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local")

    def test_invalid_zone(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "intergalactic")


class ExpressRateTests(unittest.TestCase):
    def test_express_local(self):
        # express = standard + $7 surcharge
        self.assertEqual(shipping_quote(2, "local", service="express"), 15.0)

    def test_express_regional(self):
        self.assertEqual(shipping_quote(2, "regional", service="express"), 18.0)

    def test_express_fractional_weight(self):
        # 5.0 + 1.5*1.5 + 7.0 = 14.25
        self.assertEqual(shipping_quote(1.5, "local", service="express"), 14.25)

    def test_express_invalid_weight(self):
        with self.assertRaises(ValueError):
            shipping_quote(0, "local", service="express")

    def test_unknown_service(self):
        with self.assertRaises(ValueError):
            shipping_quote(1, "local", service="overnight")
