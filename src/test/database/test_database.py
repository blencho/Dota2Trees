import unittest
from dota2.database.dota_db import update

class TestUpdate(unittest.TestCase):

	def test_load_heroes(self):
		Jeff = update()