import sys
sys.path.append("path");
import unittest
import currency_convertor
class Test_Conventor(unittest.TestCase):
    def test_conventor(self):
        cur1="USD";
        cur2="EUR";
        c=float(10);
        url=(('https://currency-api.appspot.com/api/%s/%s.json')%(cur1,cur2));
        self.assertEqual(str(currency_convertor.convert(url,c)),str(9.251000));
if __name__=="__main__":
    unittest.main();
    
    
    
