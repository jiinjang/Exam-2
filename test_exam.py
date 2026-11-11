import os

import numpy as np

import problem4
from problem1 import filter_grades
from problem2 import print_line_sums
from problem3 import normalize_numbers


def test_filter_grades():
    result = filter_grades({"Abe": 100, "Beth": 62}, 95)
    assert result == None


def test_print_line_sums():
    f = open("test_numbers.csv", "w")
    f.write("1,2,3\n4.5,5.5\n")
    f.close()

    result = print_line_sums("test_numbers.csv")
    assert result == None

    os.remove("test_numbers.csv")


def test_normalize_numbers():
    values = np.array([[1, 2], [3, 4]])
    expected = np.array([[0.25, 0.5], [0.75, 1.0]])
    result = normalize_numbers(values)
    assert np.array_equal(result, expected)


def test_titanic_missing_values():
    assert round(problem4.age_missing_percent, 2) == 19.87
    assert round(problem4.cabin_missing_percent, 2) == 77.10
    assert problem4.df["Age"].isnull().sum() == 0
    assert problem4.df["Cabin"].isnull().sum() == 0


def test_titanic_averages():
    assert round(problem4.overall_average, 2) == 29.36
    assert round(problem4.survivor_average, 2) == 28.29
    assert round(problem4.survivor_average_class1, 2) == 34.61
    assert round(problem4.survivor_average_class2, 2) == 26.00
    assert round(problem4.survivor_average_class3, 2) == 22.75
