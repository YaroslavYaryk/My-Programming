from pythonsayhello import __version__
from pythonsayhello import hello


def test_version():
    assert __version__ == "0.1.0"
    assert hello.say_hello() == "hello"
