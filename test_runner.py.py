import importlib.util
import os
import sys
import unittest


def discover_and_run_tests():
    # Add the 'solutions' directory to the system path
    sys.path.insert(0, os.path.abspath(
        os.path.join(os.path.dirname(__file__), 'solutions')))

    # Discover all test files in the 'tests' directory
    test_loader = unittest.TestLoader()
    test_suite = test_loader.discover(start_dir='tests', pattern='test_*.py')

    # Run the test suite
    test_runner = unittest.TextTestRunner(verbosity=2)
    test_runner.run(test_suite)


if __name__ == '__main__':
    discover_and_run_tests()
