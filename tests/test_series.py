from math_series.series import fibonacci, lucas, sum_series
from math_series import __version__


def test_version():
  assert __version__=='0.1.0'


######## fibonacci ########

def test_fibonacci_2():
  expected=1
  actual=fibonacci(2)
  assert expected==actual

def test_fibonacci_5():
  expected=5
  actual=fibonacci(5)
  assert expected==actual


###### Lucas #########

def test_lucas_2():
  expected=3
  actual=lucas(2)
  assert expected==actual

def test_lucas_5():
  expected=11
  actual=lucas(5)
  assert expected==actual


######## sum series #######

def test_sum_series_3():
  expected=11
  actual=sum_series(3,5,3)
  assert expected==actual

def test_sum_series_7():
  expected=79
  actual=sum_series(7,5,3)
  assert expected==actual