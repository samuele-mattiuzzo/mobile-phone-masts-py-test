# -*- coding: utf-8 -*-
import utils
from datetime import date


def task_1(sort_by='Current Rent', reverse=True, max_items=5):
    '''
    Return the first 5 items of the mast list sorted by rent (ascending order).
    '''
    reader = utils.get_masts_as_list()

    sort_by_index = utils.get_header_index(sort_by)

    return sorted(
        [row for row in reader], key=lambda x: x[sort_by_index],
        reverse=reverse
    )[:max_items]


def task_2(compare_by='Lease Years', compare_value=25):
    '''
    Return a tuple (list of all mast data with Lease Years = 25, sum of all rents)
    '''
    reader = utils.get_masts_as_list()

    compare_header_index = utils.get_header_index(compare_by)
    rent_header_index = utils.get_header_index('Current Rent')

    lease_years_list = [mast for mast in reader if int(mast[compare_header_index]) == compare_value]
    lease_years_rent_aggregate = sum([float(item[rent_header_index]) for item in lease_years_list])

    return (lease_years_list, lease_years_rent_aggregate)


def task_3(group_by='Tenant Name'):
    '''
    Return a dict object {tenant_name: count_of_masts}.
    '''
    reader = utils.get_masts_as_list()
    group_by_index = utils.get_header_index(group_by)

    res = {}
    for item in reader:
        tenant = item[group_by_index].strip()

        # treating very similar names as different, although some contain what could be considered a typo
        # eg LtD, ltd, LTD, lTD etc: the tenant name could be lowercased for this comparison
        # ignoring as per requirements
        if  tenant not in res.keys():
            res[tenant] = 0
        res[tenant] += 1
    return res


def task_4():
    '''
    Return the data for rentals with 01/06/1999 <= lease start date <= 31/08/2007
    '''
    reader = utils.get_masts_as_list()

    lease_start_header = 'Lease Start Date'
    lease_start_header_index = utils.get_header_index(lease_start_header)
    
    range_start = date(1999, 6, 1)
    range_end = date(2007, 8, 31)

    res = []
    for item in reader:
        lease_start_date_str = item[lease_start_header_index]
        if utils.is_date_string_in_range(lease_start_date_str, range_start, range_end):
            item[lease_start_header_index] = utils.date_to_string(
                utils.string_to_date(lease_start_date_str)
            )
            res.append(item)

    return res