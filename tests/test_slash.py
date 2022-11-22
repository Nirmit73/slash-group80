"""
Copyright (C) 2021 SE Slash - All Rights Reserved
You may use, distribute and modify this code under the
terms of the MIT license.
You should have received a copy of the MIT license with
this file. If not, please write to: secheaper@gmail.com

"""
import slash


def test_main():
    results = slash.main("apple computer", 20, "price",
                         "Ascending", "cmriggs@ncsu.edu")
    assert results.__len__ < 100
