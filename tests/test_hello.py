from hello import add_strings

def test_add_strings():
    assert add_strings("Hello", " World!") == "Hello World!"