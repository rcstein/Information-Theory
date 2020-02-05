import unittest
from InformationTheory import *

class MiscFuncsTests(unittest.TestCase):
    """Tests of MiscFuncs class"""

    def setUp(self):

        self.weather = np.array([.5,.25,.25]) #probability distribution of weather events


        def test_entropy(self):

            self.assertEqual(MiscFuncs.entropy(self.weather),1.5)

class HarmonicSeriesTests(unittest.TestCase):

        def setUp(self):

        self.series = HarmonicSeries(27)


            def test_add(self):

                self.assertEqual(,1.5)




if __name__ == "__main__":
    unittest.main()
        
