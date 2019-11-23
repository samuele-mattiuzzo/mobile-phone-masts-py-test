# -*- coding: utf-8 -*-
from datetime import date
from utils import (
    string_to_date,
    date_to_string,
    is_date_string_in_range
)


def test_string_to_date():
    # testing with the default input format
    test_str_date = '23 Nov 2019'
    tester_output = date(2019, 11, 23)

    assert string_to_date(test_str_date) == tester_output


def test_date_to_string():
    # testing with the default output format
    test_date = date(2019, 11, 23)
    tester_output = '23/11/2019'

    assert date_to_string(test_date) == tester_output


def test_is_date_string_in_range():
    # testing with the default input format
    test_str_date = '23 Nov 2019'
    tester_start = date(2019, 11, 1)
    tester_end = date(2019, 11, 24)

    assert is_date_string_in_range(test_str_date, tester_start, tester_end)