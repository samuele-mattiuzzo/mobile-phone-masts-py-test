# -*- coding: utf-8 -*-
import pytest
from datetime import date
from main import (
    task_1,
    task_2,
    task_3,
    task_4
)
from utils import (
    get_header_index,
    get_masts_as_list,
    is_date_string_in_range
)


def test_task_1():
    # first 5 items ordered by current rent in ascending order
    res = task_1()
    rent_header = 'Current Rent'
    rent_header_index = get_header_index(rent_header)

    assert len(res) == 5
    assert res[0][rent_header_index] >= res[1][rent_header_index]


def test_task_2():
    # list of masts whose Leas Years == 25
    # total rent sum
    res = task_2()
    lease_header = 'Lease Years'
    lease_header_index = get_header_index(lease_header)

    rent_header = 'Current Rent'
    rent_header_index = get_header_index(rent_header)

    assert len(res) > 0
    assert all([int(item[lease_header_index]) == 25 for item in res[0]])
    assert sum([float(item[rent_header_index]) for item in res[0]]) == res[1]


def test_task_3():
    # sum of masts per tenant
    res = task_3()
    
    all_rows = get_masts_as_list()
    total_count = len(list(all_rows)[1:])

    assert sum(res.values()) == total_count


def test_task_4():
    # list data for rentals with 01/0699 <= lease start date <= 31/08/09
    res = task_4()
    
    lease_start_header = 'Lease Start Date'
    lease_start_header_index = get_header_index(lease_start_header)

    lease_start = date(1999, 6, 1)
    lease_end = date(2007, 8, 31)

    date_in_format = '%d/%m/%Y'

    assert all(
        [
            is_date_string_in_range(item[lease_start_header_index], lease_start, lease_end, date_in_format) 
            for item in res
        ]
    )
    