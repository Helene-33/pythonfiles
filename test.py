import unittest
from item import item
from client import client

class itemtest(unitest.TestCase):
    def setUp(self):
        self.item=item('apple', '0.70')
    
    def test_itemstring(self):
        self.assertEqual(str(self.item), 'apple')

    def test_getitemname(self):
        self.assertEqual(self.item.getitemname(), 'apple')

    def test_setitemname(self):
        self.item.setitemname('apple')
        self.assertEqual(self.item.getitemname(), 'apple')
    
    def test_getitemprice(self):
        self.assertEqual(self.item.getitemprice(), '0.70')

    def test_setitemprice(self):
        self.item.setitemprice('0.70')
        self.assertEqual(self.item.getitemprice(), '0.70')

class clienttest(unittest.TestCase):
    def setUp(self):
        self.client=client('jackson', 'jackson@live.com')

    def test_clientstring(self):
        self.assertEqual(str(client.item), 'jackson')

    def test_getclientname(self):
        self.assertEqual(self.client.getclientname(), 'jackson')

    def test_setclientname(self):
        self.item.setitemname('jackson')
        self.assertEqual(self.client.getclientname(), 'jackson')
    
    def test_getemail(self):
        self.assertEqual(self.client.getemail(), 'jackson@live.com')

    def test_setemail(self):
        self.client.setemail('jackson@live.com')
        self.assertEqual(self.client.getemail(), 'jackson@live.com')
