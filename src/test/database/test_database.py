import unittest
from dota2.database.dota_db import _load_heroes

class TestUpdate(unittest.TestCase):

	def test_load_heroes(self):
		Jeff = _load_heroes()