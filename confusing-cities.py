#!/usr/bin/python3
# Based on customer research, we know that our guests get confused when they are searching for accommodation and they found multiple hotels with the same name in the same city.
# To avoid this, we want to create a tool to identify "confusing" cities: cities with at least 3 hotels with the same name.
# Given a list of tuples (hotel_id, hotel_name, city) return a list of all "confusing" cities.

# Output: [ "Buenos Aires" ]

# PS: the task is found here https://www.glassdoor.com/Interview/Booking-com-Site-Reliability-Engineer-Interview-Questions-EI_IE256653.0,11_KO12,37.htm

input_data = [
["hotel_1234", "Sheraton", "Amsterdam"] ,
["hotel_1000", "Sheraton", "Buenos Aires"] ,
["hotel_1001", "Hilton", "Amsterdam"] ,
["hotel_1002", "Royal Palace", "Bogota"] ,
["hotel_1003", "Hilton", "Amsterdam"] ,
["hotel_1004", "Sheraton", "Buenos Aires"] ,
["hotel_1005", "Sheraton", "Buenos Aires"]
]
import copy
input_data2 = copy.deepcopy(input_data)

# first sol
helper = {}
ret = {}
for i in range(len(input_data)): # O(n), we need to check all elements
    city = input_data[i].pop()
    hotel = input_data[i].pop()
    if city+hotel in helper: # O(n). 
        helper[city+hotel] += 1
    else:
        helper[city+hotel] = 1
    if helper[city+hotel] > 2 and city not in ret: # O(2n)
        ret[city] = True
print(ret.keys())

# second sol
helper = {}
ret = {}
for i in range(len(input_data2)):
    city = input_data2[i].pop()
    if city in ret:
        continue
    hotel = input_data2[i].pop()
    if city+hotel in helper and helper[city+hotel] > 1:
        ret[city] = True
        continue
    elif city+hotel in helper:
        helper[city+hotel] += 1
    else:
        helper[city+hotel] = 1
print(ret.keys())