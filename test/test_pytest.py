import library.finc_dec as finc_dec    # The code to test

def test_increment():
    assert finc_dec.increment(3) == 4

##si no esta este test no detecta los otros.. ignorarlo