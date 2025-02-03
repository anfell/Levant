import unittest


Funds = ['FIXED_INCOME', 'GOLD', 'AVA', 'AHANG']



class TestWorkflow(unittest.TestCase):
    def test_scenario_1(self):
        # Test Case 1
        self.assertTrue(self.execute_workflow(1, [1, 2, 3]))

    def test_scenario_2(self):
        # Test Case 2
        self.assertTrue(self.execute_workflow(1, [1, 3, 2]))

    def test_scenario_3(self):
        # Test Case 3
        self.assertTrue(self.execute_workflow(2, [1, 3]))

    def test_scenario_4(self):
        # Test Case 4
        self.assertTrue(self.execute_workflow(2, [3, 1]))

    def test_scenario_5(self):
        # Test Case 5
        self.assertTrue(self.execute_workflow(3, [1, 2]))

    def test_scenario_6(self):
        # Test Case 6
        self.assertTrue(self.execute_workflow(3, [2, 1]))

    # Define your workflow execution function
    def execute_workflow(self, start_test, steps):
        # Implement your workflow logic here
        # This is a simplified example; replace with your actual code
        current_test = start_test
        for step in steps:
            if step == 1:
                # Implement logic for step 1
                pass
            elif step == 2:
                # Implement logic for step 2
                pass
            elif step == 3:
                # Implement logic for step 3
                pass

        # Add any additional checks or return values as needed
        return True  # For demonstration purposes


if __name__ == '__main__':
    unittest.main()


















class TestWorkflow(unittest.TestCase):
    # Define the mapping dictionary
    fund_mapping = {
        1: 'FIXED_INCOME',
        2: 'GOLD',
        3: 'AVA',
        4: 'AHANG'
    }

    def test_scenario_1(self):
        # Test Case 1
        steps = [1, 2, 3]
        self.assertTrue(self.execute_workflow(steps))

    def test_scenario_2(self):
        # Test Case 2
        steps = [1, 3, 2]
        self.assertTrue(self.execute_workflow(steps))

    def test_scenario_3(self):
        # Test Case 3
        steps = [2, 1, 3]
        self.assertTrue(self.execute_workflow(steps))

    def test_scenario_4(self):
        # Test Case 4
        steps = [2, 3, 1]
        self.assertTrue(self.execute_workflow(steps))

    def test_scenario_5(self):
        # Test Case 5
        steps = [3, 1, 2]
        self.assertTrue(self.execute_workflow(steps))

    def test_scenario_6(self):
        # Test Case 6
        steps = [3, 2, 1]
        self.assertTrue(self.execute_workflow(steps))

    # Define your workflow execution function
    def execute_workflow(self, steps):
        current_funds = []  # Initialize an empty list for funds
        for step in steps:
            current_fund = self.fund_mapping.get(step)
            if current_fund:
                current_funds.append(current_fund)
            else:
                raise ValueError(f"Invalid fund number: {step}")

        # Add any workflow logic you need here
        return current_funds

if __name__ == '__main__':
    unittest.main()
