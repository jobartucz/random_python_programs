# https://www.codewars.com/kata/5550d638a99ddb113e0000a2/train/python

import unittest

def josephus(items,k):

    toreturn = []

    start = k
    while len(items) > 0:
        while start > len(items):
             start -= len(items)
        
        toreturn.append(items.pop(start-1))

        start += k - 1

    return toreturn

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_dotests(self):
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],1),[1,2,3,4,5,6,7,8,9,10])
        self.assertEquals(josephus([1,2,3,4,5,6,7,8,9,10],2),[2, 4, 6, 8, 10, 3, 7, 1, 9, 5])
        self.assertEquals(josephus(["C","o","d","e","W","a","r","s"],4),['e', 's', 'W', 'o', 'C', 'd', 'r', 'a'])
        self.assertEquals(josephus([1,2,3,4,5,6,7],3),[3, 6, 2, 7, 5, 1, 4])
        self.assertEquals(josephus([],3),[])
        
if __name__ == '__main__':
    unittest.main()

