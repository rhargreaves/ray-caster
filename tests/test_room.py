import unittest
import room as r

class RoomTests(unittest.TestCase):

    def test_centre(self):
        room = r.Room()
        self.assertEqual(room.centre(), (212.5, 212.5))
