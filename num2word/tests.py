import unittest
from django.test import TestCase
from selenium import webdriver

class TestCase(TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()

    def test_signup_fire(self):
        self.driver.get("http://127.0.0.1:8000/num2words/-3231.3454/de/")
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)

    def test_signup_fire2(self):
        self.driver.get("http://127.0.0.1:8000/num2words/-3231.3454/")
        self.assertIn("http://127.0.0.1:8000/", self.driver.current_url)

    def tearDown(self):
        self.driver.quit


if __name__ == '__main__':
    unittest.main()