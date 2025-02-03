import unittest

from Tools.scripts import run_tests


import subprocess
from TestOnboardingEsign import test_01_users_onboarding_esign, test_02_users_crm_esign


if __name__ == '__main__':
    test_loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()

    # Add your test classes to the test suite
    test_suite.addTest(test_loader.loadTestsFromTestCase(test_01_users_onboarding_esign.py))
    test_suite.addTest(test_loader.loadTestsFromTestCase(test_02_users_crm_esign.py))

    # Run the tests in a loop
    for _ in range(2):  # Change 3 to the number of times you want to run the tests
        test_runner = unittest.TextTestRunner(verbosity=2)  # Set verbosity level
        test_runner.run(test_suite)




# Specify the test files and number of times to run
test_files = ['test_file1.py', 'test_file2.py']
num_runs = 3



# Run each test file the specified number of times
for _ in range(num_runs):
    for test_file in test_files:
        subprocess.run(['python', test_file])

# bash code is python run_tests.py
