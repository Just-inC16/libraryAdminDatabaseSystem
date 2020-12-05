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
    def test_gender(self):
        #Test for multiple characters
        self.assertRaises(ValueError,self.implInstance.set_gender,"ms" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"0123456" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"msfsf" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"0" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"A" )
        self.assertRaises(ValueError,self.implInstance.set_gender," ")
        self.assertRaises(ValueError,self.implInstance.set_gender, "None" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"f" )
        self.assertRaises(ValueError,self.implInstance.set_gender,"0" )
        self.assertEqual(self.implInstance.set_gender("M"), None )
        self.assertEqual(self.implInstance.set_gender("F"), None )
    def test_date(self):
        self.assertRaises(ValueError,self.implInstance.set_date,"" )
        self.assertRaises(ValueError,self.implInstance.set_date,"A" )
        self.assertRaises(ValueError,self.implInstance.set_date, "None" )
        self.assertRaises(ValueError,self.implInstance.set_date,"---------" )
        self.assertRaises(ValueError,self.implInstance.set_date,"msfsf" )
        self.assertRaises(ValueError,self.implInstance.set_date,"0123456" )

        self.assertRaises(ValueError,self.implInstance.set_date,"03-04999?9" )
        self.assertRaises(ValueError,self.implInstance.set_date,"0A-1B-2003")
        self.assertRaises(ValueError,self.implInstance.set_date,"03-04?2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"03-04 2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"03-0499999" )
        self.assertRaises(ValueError,self.implInstance.set_date,"32-11-2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"11-32-2010" )
        self.assertRaises(ValueError,self.implInstance.set_date,"13-49-9999" )
        self.assertRaises(ValueError,self.implInstance.set_date,"31-25-2012" )
        self.assertRaises(ValueError,self.implInstance.set_date,"-1-4-2010" )

        self.assertEqual(self.implInstance.set_date("1-4-2010"), None )
        self.assertEqual(self.implInstance.set_date("11-31-2004"), None )
        self.assertEqual(self.implInstance.set_date("10-31-2020"), None )
        self.assertEqual(self.implInstance.set_date("31-10-2010"), None )
        self.assertEqual(self.implInstance.set_date("1-1-2000"), None )
        self.assertEqual(self.implInstance.set_date("01-01-2000"), None )
        self.assertEqual(self.implInstance.set_date("001-001-02020" ), None )

    def test_height(self):
        self.assertRaises(ValueError,self.implInstance.set_height,0 )
        self.assertRaises(ValueError,self.implInstance.set_height,-1 )
        self.assertRaises(ValueError,self.implInstance.set_height,-100 )
        self.assertRaises(ValueError,self.implInstance.set_height,100 )
        self.assertRaises(ValueError,self.implInstance.set_height,5 )
        self.assertRaises(ValueError, self.implInstance.set_height, -49)
        self.assertRaises(ValueError,self.implInstance.set_height,16)
        self.assertRaises(ValueError,self.implInstance.set_height,85)
        self.assertEqual(self.implInstance.set_height(17), None )
        self.assertEqual(self.implInstance.set_height(84), None )
        self.assertEqual(self.implInstance.set_height(40), None )
 
    def test_temperature(self):
        self.assertRaises(ValueError,self.implInstance.set_temperature,0.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,-1.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,-100.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,150.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,5.0 )
        self.assertRaises(ValueError,self.implInstance.set_temperature,104.01)
        self.assertRaises(ValueError, self.implInstance.set_temperature, -49)
        self.assertRaises(ValueError,self.implInstance.set_temperature,94.9999999)
        self.assertEqual(self.implInstance.set_temperature(95.0), None )
        self.assertEqual(self.implInstance.set_temperature(104.0), None )
        self.assertEqual(self.implInstance.set_temperature(97.3), None )
    def test_name(self):
        self.assertRaises(ValueError,self.implInstance.set_name,0.0 )
        self.assertRaises(ValueError,self.implInstance.set_name,-1.0 )
        self.assertRaises(ValueError,self.implInstance.set_name,-100.0 )
        self.assertRaises(ValueError,self.implInstance.set_name,150.0 )
        self.assertRaises(ValueError,self.implInstance.set_name,5.0 )
        self.assertRaises(ValueError,self.implInstance.set_name,104.01)
        self.assertRaises(ValueError,self.implInstance.set_name,94.9999999)
        self.assertEqual(self.implInstance.set_name("ab0987"), None )
        self.assertEqual(self.implInstance.set_name("ab-"), None )
        self.assertEqual(self.implInstance.set_name("ABC - 7 - ZYX"), None )
if __name__=='__main__':
    unittest.main()
