# -*- coding: utf-8 -*-
"""
city_by_zip.py: returns the cities listed under a given zipcode

@author: Jonah
"""

from uszipcode import SearchEngine

search = SearchEngine(simple_zipcode=False)

def return_cities():
    zipcode = input("Please enter a zipcode: ")
    result = search.by_zipcode(zipcode)
    for city in result.common_city_list:
        print("\n"+city)

if __name__ == "__main__":
    return_cities()

