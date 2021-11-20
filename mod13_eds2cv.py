import unittest
import datetime

class TestSuccessClass(unittest.TestCase):

  def test_stock_symbol(get_user_input):
    get_user_input.assertLessEqual(len("GOOGL"), 7)
    get_user_input.assertGreaterEqual(len("GOOGL"), 1)
    get_user_input.assertTrue("GOOGL".isupper() and "GOOGL".isalpha())

  def test_chart_type(get_user_input):
    get_user_input.assertLessEqual(1, 2)
    get_user_input.assertGreaterEqual(1, 1)
    get_user_input.assertTrue(type(1) == int)

  def test_time_series(get_user_input):
    get_user_input.assertLessEqual(2, 4)
    get_user_input.assertGreaterEqual(2, 1)
    get_user_input.assertTrue(type(1) == int)

  def test_start_date(get_user_input):
    some_date = datetime.datetime.strptime("2000-07-03","%Y-%m-%d").date()
    get_user_input.assertIsInstance(some_date, datetime.date)

  def test_end_date(get_user_input):
    some_date = datetime.datetime.strptime("2000-07-03","%Y-%m-%d").date()
    get_user_input.assertIsInstance(some_date, datetime.date)

class TestFailClass(unittest.TestCase):

  def test_stock_symbol(get_user_input):
    get_user_input.assertLessEqual(len("GOOGLEHASNONOSE"), 7, "\n\nThis is meant to fail")
    get_user_input.assertGreaterEqual(len(""), 1, "\n\nThis is meant to fail")
    get_user_input.assertTrue("GOogl".isupper() and "g**gl".isalpha(), "\n\nThis is meant to fail")

  def test_chart_type(get_user_input):
    get_user_input.assertLessEqual(3, 2, "\n\nThis is meant to fail")
    get_user_input.assertGreaterEqual(0, 1, "\n\nThis is meant to fail")
    get_user_input.assertTrue(type("a") == int, "\n\nThis is meant to fail")

  def test_time_series(get_user_input):
    get_user_input.assertLessEqual(5, 4, "\n\nThis is meant to fail")
    get_user_input.assertGreaterEqual(0, 1, "\n\nThis is meant to fail")
    get_user_input.assertTrue(type("a") == int, "\n\nThis is meant to fail")

  def test_start_date(get_user_input):
    some_date = "2000-07-03"
    get_user_input.assertIsInstance(some_date, datetime.date, "\n\nThis is meant to fail")

  def test_end_date(get_user_input):
    some_date = "2000-07-03"
    get_user_input.assertIsInstance(some_date, datetime.date, "\n\nThis is meant to fail")

if __name__ == "__main__":
  unittest.main()