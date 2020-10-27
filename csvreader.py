# Vicente Saraos 001090322

import csv
from chaininghashtable import ChainingHashTable

# reader object of provided package data
# for loop places packages on truck by comparing conditions and relevant package notes, address, etc
with open('WGUPS Package Information.csv') as csv3:
    csv_reader3 = csv.reader(csv3, skipinitialspace=True, delimiter=',')

    # stores package data as a chained hash table, implemented as linked lists
    insert_package_data = ChainingHashTable()
    # each list is the package cargo per delivery
    first_truck = []
    second_truck = []
    first_truck2 = []

    # Space-time complexity O(N)
    # parase and read from 'WGUPS Package Information.csv'
    # assign and insert each cell(attribute) of a row(package)
    for row in csv_reader3:
        id_number = row[0]
        address = row[1]
        city = row[2]
        state = row[3]
        zip = row[4]
        deadline = row[5]
        weight = row[6]
        note = row[7]
        delivery_start = ''
        location = ''
        status = 'Hub'
        package_data = [id_number, address, city, state, zip, deadline, weight, note, delivery_start, location, status]

        key = id_number
        package_data1 = package_data
        # attempts to optimize cargo load per truck by necessary conditions
        if '3575' in package_data1[1]:
            first_truck.append(package_data1)
        if package_data[5] != 'EOD':
            if 'Must' in package_data1[7] or 'None' in package_data1[7]:
                first_truck.append(package_data1)
        if 'Can' in package_data1[7]:
            second_truck.append(package_data1)
        if 'Delayed' in package_data[7]:
            second_truck.append(package_data1)
        if '84104' in package_data1[4] and '10:30' not in package_data1[5]:
            first_truck2.append(package_data1)
        if 'Wrong' in package_data1[7]:
            package_data1[1] = '410 S State St'
            package_data1[4] = '84111'
        # less restrictive condition comparison, if a package is not already on a truck
        # put it on another truck
        if package_data1 not in first_truck and package_data1 not in second_truck and package_data1 not in first_truck2:
            if len(second_truck) > len(first_truck2):
                first_truck2.append(package_data1)
            else:
                second_truck.append(package_data1)
        insert_package_data.insert(key, package_data1)


# Space-time complexity O(1)
# returns the hash map created
# is a chained hash table of packages
def get_hash_table():
    return insert_package_data


# Space-time complexity O(1)
# returns first truck cargo manifest
def first_truck_trip1():
    return first_truck


# Space-time complexity O(1)
# returns second truck cargo manifest
def second_truck_trip1():
    return second_truck


# Space-time complexity O(1)
# returns first truck's second trip cargo manifest
def first_truck_trip2():
    return first_truck2
