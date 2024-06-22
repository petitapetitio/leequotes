from leequotes import leequotes


def test_get_quote():
    q = leequotes.random()
    print(q)
