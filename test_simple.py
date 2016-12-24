from unittest import TestCase
import maxSharpe

class TestSimple(TestCase):
  def test_func1(self):
    self.fail()


if __name__ == "__main":
  ts = TestSimple()
  ts.test_func1()