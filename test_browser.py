from web import get_date


def test_get_date():
    next_thu = get_date(0, 4)
    print next_thu
    assert next_thu.isoweekday() == 4

    first_thu = get_date(1, 4)
    sec_thu = get_date(2, 4)
    print first_thu
    print sec_thu
    assert first_thu.isoweekday() == 4
    assert sec_thu.isoweekday() == 4
    assert (first_thu - sec_thu).days == -7

    next_fri = get_date(0, 5)
    assert next_fri.isoweekday() == 5
    assert ((next_fri - next_thu).days == 1) or ((next_fri - next_thu).days == -6 )
