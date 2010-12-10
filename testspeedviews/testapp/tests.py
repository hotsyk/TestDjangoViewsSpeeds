from django.test import TestCase
from django.test.client import Client

import timeit

class TestFunctionViews(TestCase):


    def test_function_based(self):
    
        code ='''\
        from django.test.client import Client
        c = Client()
        response = c.get('/function_based_view/')
        '''        
        t = timeit.Timer(stmt=code)
        print "Function based view >>>"
        print t.timeit(number=10000)
    
class TestClassBasedViews(TestCase):
    
    def test_class_based(self):
        
        code ='''\
        from django.test.client import Client
        c = Client()
        response = c.get('/class_based_view/')
        '''        
        
        t = timeit.Timer(stmt=code)
        print "Class based view >>>"
        print t.timeit(number=10000)
