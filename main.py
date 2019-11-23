# -*- coding: utf-8 -*-
import tasks
from utils import CSV_FILE_HEADERS_INDEX


# Helpers to print to console
def print_file_headers_to_list():
    print(list(CSV_FILE_HEADERS_INDEX.keys()))


def task_1_to_console():
    res = tasks.task_1()
    print_file_headers_to_list()
    print(res)


def task_2_to_console():
    res = tasks.task_2()
    print_file_headers_to_list()
    print(res[0])
    print('Sum of all rents:', res[1])


def task_3_to_console():
    res = tasks.task_3()
    for tenant, masts in res.items():
        print("{} rents {} masts".format(tenant, masts))


def task_4_to_console():
    res = tasks.task_4()
    print_file_headers_to_list()
    print(res)


def run_all():
    task_1_to_console()
    task_2_to_console()
    task_3_to_console()
    task_4_to_console()


if __name__ == '__main__':
    user_choice = input('Insert a number [1,2,3,4] to run a specific task or leave empty to run them all.')

    if not user_choice:
        run_all()
    else:
        user_choice = int(user_choice)
        if user_choice == 1:
            task_1_to_console()

        if user_choice == 2:
            task_2_to_console()

        if user_choice == 3:
            task_3_to_console()

        if user_choice == 4:
            task_4_to_console()
