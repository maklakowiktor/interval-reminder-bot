import unittest

from intervalreminder import Reminders

class TestGetAllReminders(unittest.TestCase):
    def setUp(self):
        self.obj = Reminders()
    
    def test_get_all_reminders(self):
        (first, second) = self.obj.get_all_reminders()
        print(first.raw_text)
        print(second.raw_text)
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()