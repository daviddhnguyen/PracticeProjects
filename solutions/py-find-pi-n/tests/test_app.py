from src.py_find_pi_n.hello_world import say_hello
from src.py_find_pi_n.find_pi import find_pi

def test_say_hello():
    assert say_hello() == "Hello, World!"

def test_find_pi():
    assert find_pi(3) == '3.141'
    assert find_pi(6) == '3.141592'
    assert find_pi(99) == "Error to many digits; enter 50 or less!"