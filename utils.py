# -*- coding: utf-8 -*-
import csv
from datetime import datetime


CSV_FILE = 'Mobile Phone Masts.csv'

CSV_FILE_HEADERS_INDEX = {  # for convenience
    'Property Name': 0,
    'Property Address [1]': 1,
    'Property  Address [2]': 2,
    'Property Address [3]': 3,
    'Property Address [4]': 4,
    'Unit Name': 5, 
    'Tenant Name': 6,
    'Lease Start Date': 7,
    'Lease End Date': 8,
    'Lease Years': 9,
    'Current Rent': 10
}
DATE_IN_FORMAT = '%d %b %Y'
DATE_OUT_FORMAT = '%d/%m/%Y'


def string_to_date(date_string, in_format=DATE_IN_FORMAT):
    # converts a string formatted date to a date object
    # allows to specify the input format
    return datetime.strptime(date_string, in_format).date()


def date_to_string(date_object, out_format=DATE_OUT_FORMAT):
    # converts a date object to a string
    # allows to specify the output format
    return date_object.strftime(out_format)


def is_date_string_in_range(date_string, range_start, range_end, in_format=DATE_IN_FORMAT):
    # compares a string formatted date with two date objects
    # allows to specify the input format
    return (range_start <= string_to_date(date_string, in_format) <= range_end)


def get_header_index(header):
    # returns the list index for a header
    return CSV_FILE_HEADERS_INDEX.get(header)


def get_masts_as_list():
    mast_file = open(CSV_FILE, 'r', encoding='utf-8')
    reader = csv.reader(mast_file, delimiter=',')
    return list(reader)[1:]  # skips the header