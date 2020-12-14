import unittest
import impl

class TestImpl(unittest.TestCase):
    def setUp(self):
        self.implInstance=impl.PhysicalInfo()
    def tearDown(self):
        self.implInstance=None
    #Check that the type matches
    def test_types(self):
        
        #Check type in set_date
        self.assertRaises(ValueError, self.implInstance.set_date, 3)
        self.assertRaises(ValueError, self.implInstance.set_date, True)
        self.assertRaises(ValueError, self.implInstance.set_date, 3.52)
        self.assertRaises(ValueError, self.implInstance.set_date, -49)
        self.assertRaises(ValueError, self.implInstance.set_date, None)
        #Check type in set_name 
        self.assertRaises(ValueError, self.implInstance.set_name, 3)
        self.assertRaises(ValueError, self.implInstance.set_name, True)
        self.assertRaises(ValueError, self.implInstance.set_name, 3.52)
        self.assertRaises(ValueError, self.implInstance.set_name, -49)
        self.assertRaises(ValueError, self.implInstance.set_name, None)
        #Check type in set_gender 
        self.assertRaises(ValueError, self.implInstance.set_gender, 3)
        self.assertRaises(ValueError, self.implInstance.set_gender, True)
        self.assertRaises(ValueError, self.implInstance.set_gender, 3.52)
        self.assertRaises(ValueError, self.implInstance.set_gender, -49)
        self.assertRaises(ValueError, self.implInstance.set_gender, None)
         #Check type in set_height 
        self.assertRaises(ValueError, self.implInstance.set_height, " ")
        self.assertRaises(ValueError, self.implInstance.set_height, "just")
        self.assertRaises(ValueError, self.implInstance.set_height, True)
        self.assertRaises(ValueError, self.implInstance.set_height, 3.0)
        self.assertRaises(ValueError, self.implInstance.set_height, 0.0)
        self.assertRaises(ValueError, self.implInstance.set_height, 45.67)
        self.assertRaises(ValueError, self.implInstance.set_height, None)
        #Check type in set_temperature 
        self.assertRaises(ValueError, self.implInstance.set_temperature, " ")
        self.assertRaises(ValueError, self.implInstance.set_temperature, "just")
        self.assertRaises(ValueError, self.implInstance.set_temperature, True)
        self.assertRaises(ValueError, self.implInstance.set_temperature, 3)
        self.assertRaises(ValueError, self.implInstance.set_temperature, 10)
        self.assertRaises(ValueError, self.implInstance.set_temperature, 0)
        self.assertRaises(ValueError, self.implInstance.set_temperature, None)
    def test_name(self):
        self.assertRaises(ValueError,self.implInstance.set_name,"a-" )
        self.assertRaises(ValueError,self.implInstance.set_name,"894916 -" )
        self.assertRaises(ValueError,self.implInstance.set_name,"         " )
        self.assertRaises(ValueError,self.implInstance.set_name,"- A B - ☺" )
        self.assertRaises(ValueError,self.implInstance.set_name,"I♥U" )
        self.assertRaises(ValueError,self.implInstance.set_name,"99" )
        self.assertRaises(ValueError,self.implInstance.set_name,"A" )
        self.assertEqual(None,self.implInstance.set_name("ab0987") )
        self.assertEqual(None,self.implInstance.set_name("ab-") )
        self.assertEqual(None,self.implInstance.set_name("ABC - 7 - ZYX") )
        self.assertEqual(None,self.implInstance.set_name("                 ab") )
        self.assertEqual(None,self.implInstance.set_name("          -       99a") )
    def test_gender(self):
        #Test for multiple characters
        self.assertRaises(ValueError,self.implInstance.set_gender,"ms" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"0123456" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"msfsf" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"0" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"A" )
        self.assertRaises(ValueError,self.implInstance.set_gender," ")
        self.assertRaises(ValueError,self.implInstance.set_gender, "None" )
        self.assertEqual( None,self.implInstance.set_gender("M"))
        self.assertEqual( None,self.implInstance.set_gender("F"))
    def test_height(self):
        self.assertRaises(ValueError,self.implInstance.set_height,0 )
        self.assertRaises(ValueError,self.implInstance.set_height,-1 )
        self.assertRaises(ValueError,self.implInstance.set_height,-100 )
        self.assertRaises(ValueError,self.implInstance.set_height,100 )
        self.assertRaises(ValueError,self.implInstance.set_height,5 )
        self.assertRaises(ValueError, self.implInstance.set_height, -49)
        self.assertRaises(ValueError,self.implInstance.set_height,16)
        self.assertRaises(ValueError,self.implInstance.set_height,85)
        self.assertEqual( None,self.implInstance.set_height(17) )
        self.assertEqual( None,self.implInstance.set_height(84) )
        self.assertEqual( None,self.implInstance.set_height(40) )
 
    def test_temperature(self):
        self.assertRaises(ValueError,self.implInstance.set_temperature,0.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,-1.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,-100.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,150.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,5.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,104.0111111111)
        self.assertRaises(ValueError, self.implInstance.set_temperature, -49)
        self.assertRaises(ValueError,self.implInstance.set_temperature,94.9999999)
        self.assertEqual( None,self.implInstance.set_temperature(95.000) )
        self.assertEqual( None,self.implInstance.set_temperature(95.001) )
        self.assertEqual( None,self.implInstance.set_temperature(103.99999999) )
        self.assertEqual( None,self.implInstance.set_temperature(104.0) )
        self.assertEqual( None,self.implInstance.set_temperature(97.3) )
    def test_date(self):
        self.assertRaises(ValueError,self.implInstance.set_date,"" )
        self.assertRaises(ValueError,self.implInstance.set_date,"A" )
        self.assertRaises(ValueError,self.implInstance.set_date, "None" )
        self.assertRaises(ValueError,self.implInstance.set_date,"---------" )
        self.assertRaises(ValueError,self.implInstance.set_date,"msfsf" )
        self.assertRaises(ValueError,self.implInstance.set_date,"0123456" )

        self.assertRaises(ValueError,self.implInstance.set_date,"03-04999?9" )
        self.assertRaises(ValueError,self.implInstance.set_date,"0A-1B-2003")
        self.assertRaises(ValueError,self.implInstance.set_date,"A-B-2003")
        self.assertRaises(ValueError,self.implInstance.set_date,"03-04?2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"03-04 2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"03-0499999" )
        self.assertRaises(ValueError,self.implInstance.set_date,"32-11-2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"11-32-2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"13-49-0109" )
        self.assertRaises(ValueError,self.implInstance.set_date,"31-25-2012" )
        self.assertRaises(ValueError,self.implInstance.set_date,"-1-4-0010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"1-4-21.00" )
        self.assertRaises(ValueError,self.implInstance.set_date,"1-4-2101" )
        self.assertRaises(ValueError,self.implInstance.set_date,"1-4-1899" )
        self.assertRaises(ValueError,self.implInstance.set_date,"1-4-210." )

        self.assertEqual( None, self.implInstance.set_date("1-4-1900"))
        self.assertEqual( None, self.implInstance.set_date("11-31-2004"))
        self.assertEqual( None, self.implInstance.set_date("10-31-2000"))
        self.assertEqual( None, self.implInstance.set_date("31-10-2010"))
        self.assertEqual( None, self.implInstance.set_date("1-1-2100"))
        self.assertEqual( None, self.implInstance.set_date("01-01-0001900"))
        self.assertEqual( None, self.implInstance.set_date("001-001-0002020" ))
if __name__=='__main__':
    unittest.main()
