def test_passing():  # sourcery skip: equality-identity, remove-assert-true
    assert (1, 2, 3) == (1, 2, 3)
    assert 1 in [1, 2, 3]
    assert 1 < 2
    assert "fizz" not in "fizzbuzz"
