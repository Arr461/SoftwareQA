# Austin Rowell, arr461
# QA Assignment 2
# Due: Thursday, March 4th 2021
# Unit testing BMI and Retirement functions

# Imports
import unittest
from unittest.mock import MagicMock, patch
from QA_Assignment import retirement, BMI

# Test Class
class Test_Function_QA_Assignment(unittest.TestCase):

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["45", "100000", "500000", "15"])
  def test_retirement_function_pass(self, mock_input):
      # Mocking parameter within retirement and asserting
      mock_object = MagicMock()
      asserted = retirement(mock_object)
      expected = 70
      self.assertEqual(asserted,expected)

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["15", "100000", "500000", "1"])
  def test_retirement_function_fail(self, mock_input):
      # Mocking parameter within retirement and asserting
      mock_object = MagicMock()
      asserted = retirement(mock_object)
      expected = 385
      self.assertEqual(asserted,expected)

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["5 3", "100"])
  def test_BMI_function_pass_underweight(self, mock_input):
      # Mocking parameter within BMI and asserting
      mock_object = MagicMock()
      asserted = BMI(mock_object)
      expected = 18
      self.assertEqual(asserted,expected)

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["5 3", "125"])
  def test_BMI_function_pass_normal(self, mock_input):
      # Mocking parameter within BMI and asserting
      mock_object = MagicMock()
      asserted = BMI(mock_object)
      expected = 23
      self.assertEqual(asserted,expected)

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["5 3", "160"])
  def test_BMI_function_pass_overweight(self, mock_input):
      # Mocking parameter within BMI and asserting
      mock_object = MagicMock()
      asserted = BMI(mock_object)
      expected = 29
      self.assertEqual(asserted,expected)

  # Patching the inputs 
  @patch("builtins.input", side_effect = ["5 3", "200"])
  def test_BMI_function_pass_obese(self, mock_input):
      # Mocking parameter within BMI and asserting
      mock_object = MagicMock()
      asserted = BMI(mock_object)
      expected = 36
      self.assertEqual(asserted,expected)
    

if __name__ == '__main__':
    unittest.main()
