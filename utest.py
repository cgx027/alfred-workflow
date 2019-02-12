import os
import sys
import unittest

if __name__ == '__main__':
   loader = unittest.TestLoader()
   tests = loader.discover('./utest')
   testRunner = unittest.runner.TextTestRunner()
   testRunner.run(tests)
