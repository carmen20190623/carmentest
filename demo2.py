# -*- coding: utf-8 -*-
"""
@Time : 2021/3/20 13:52
@Author : Carmen
@file: demo2.py
"""


class Employee:
    '所有员工的基类'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
