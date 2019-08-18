from brian_calculator import app


def test_add():
    expect = 5
    actual = app.add(2, 3)
    assert expect == actual
