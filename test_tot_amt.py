import unittest
from tot_amt import tot_amt

class TestToltal(unittest.TestCase):
    def test_eqamt(self):
        """
        test correct output
        """        
        self.assertEqual(tot_amt({"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}),275)
        self.assertEqual(tot_amt({"sam": 83, "sasi": -48}),35)
        
        #testing exception case
        with self.assertRaises(TypeError):
            tot_amt([12,13,5])
        with self.assertRaises(TypeError):
            tot_amt({"siva": 50, "kumar": 48.8})
            tot_amt({"siva": '50', "kumar": 48})       
            
if __name__=="__main__":
    unittest.main()

        
