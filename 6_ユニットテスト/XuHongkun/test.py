from Sample import Count
import unittest

class TestAdd(unittest.TestCase):
    def setUp(self):
        print('test start')

    def test_add(self):
        j = Count(2, 3)
        self.assertEqual(j.add(), 5, 'error！')

    def tearDown(self):
        print('test end')


if __name__ == '__main__':
     suite = unittest.TestSuite()
     suite.addTest(TestAdd('test_add'))

     runner = unittest.TextTestRunner()
     runner.run(suite)
     print('Finish!')
