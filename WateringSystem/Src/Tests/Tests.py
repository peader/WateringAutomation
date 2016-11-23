'''
Created on 15Nov.,2016

@author: kilta
'''
import unittest
from Src.DbConnection import Models
from Src.DbConnection.Models import WateringLog


class Test(unittest.TestCase):


    def setUp(self):
        #WateringLog.create_table()
        temp = WateringLog.create()

    def testQuery1(self):
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.QueryTest1']
    unittest.main()