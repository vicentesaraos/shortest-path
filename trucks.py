# Vicente Saraos 001090322

import datetime
import csv

# parse and read in .csv of address distances between two addresses
with open('WGUPS Distance Data.csv') as distance_data_input:
    distance_data = list(csv.reader(distance_data_input, delimiter=','))

    # Space-time complexity O(1)
    # calculate distance between two addresses
    # try row,col index mismatch ('') try inverse
    def distances_list(row, column, sumtotal):
        distance = distance_data[row][column]
        if distance == '':
            distance = distance_data[column][row]
        sumtotal += float(distance)
        return sumtotal

    # Space-time complexity O(1)
    # calculate current location
    # try row,col index mismatch ('') try inverse
    def get_location(row, column):
        distance = distance_data[row][column]
        if distance == '':
            distance = distance_data[column][row]
        return float(distance)

# parse and read in .csv of delivery addresses
with open('WGUPS AddressLocation Data.csv') as address_input:
    addresses = list(csv.reader(address_input, skipinitialspace=True, delimiter=','))

    # Space-time complexity O(1)
    # returns the list of addresses
    # called in packages.py to compare address indices (distances)
    def address():
        return addresses

# time of delivery trucks departure from WGU Hub
timelist1 = ['8:00:00']
timelist2 = ['9:10:00']
timelist3 = ['11:00:00']

# lists of optimized trucks and list indices
truck1_o = []
truck1_oindex = []
truck2_o = []
truck2_oindex = []
truck3_o = []
truck3_oindex = []


# Space-time O(1)
# str format of truck travel average of 18mph
def distance_min(distance):
    distance_time = '{0:02.0f}:{1:02.0f}'.format(*divmod(distance / 18 * 60, 60)) + ':00'
    return distance_time


# Space-time O(N)
# creates datetime timedelta of distance_time
# calculates distance travelled by truck1 by comparing the datetime timestamps
def first_truck_time(distance):
    timelist1.append(distance_min(distance))
    sumtotal = datetime.timedelta()
    for x in timelist1:
        (h, m, s) = x.split(':')
        times = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sumtotal += times
    return sumtotal


# Space-time O(N)
# creates datetime timedelta of distance_time
# calculates distance travelled by truck2 by comparing the datetime timestamps
def second_truck_time(distance):
    timelist2.append(distance_min(distance))
    sumtotal = datetime.timedelta()
    for x in timelist2:
        (h, m, s) = x.split(':')
        times = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sumtotal += times
    return sumtotal


# Space-time O(N)
# creates datetime timedelta of distance_time
# calculates distance travelled by truck1 trip2(third truck) by comparing the datetime timestamps
def third_truck_time(distance):
    timelist3.append(distance_min(distance))
    sumtotal = datetime.timedelta()
    for x in timelist3:
        (h, m, s) = x.split(':')
        times = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
        sumtotal += times
    return sumtotal


# Space-time complexity O(N^2)
# attempt at optimization algorithm of a greedy-type
# Params (unsorted)package list, (1,2,3)truck number, (initially from hub, updates at each delivery)location of truck
# First comparison checks if truck is empty (if all packages have been delivered, the truck can return)
# x variable is a smallest distance from the distance wgu file and get_location returns a distance from the file
# (from the csv reader). if the distance is smaller than x, it is set to the current/new location, until the end of the
# distance list passed to the function. The smallest distance is popped from the list, and short_dist recursively executes
def shortest_distance(distance_list, truck, current_location):
    if len(distance_list) == 0:
        return distance_list
    else:
        try:

            x = 15.0 # (smallest distance)
            new_location = 0
            for n in distance_list:
                if get_location(current_location, int(n[1])) <= x:
                    x = get_location(current_location, int(n[1]))
                    new_location = int(n[1])
            for n in distance_list:
                if get_location(current_location, int(n[1])) == x:
                    if truck == 1:
                        truck1_o.append(n)
                        truck1_oindex.append(n[1])
                        y = distance_list.index(n)
                        distance_list.pop(y)
                        current_location = new_location
                        shortest_distance(distance_list, 1, current_location)
                    elif truck == 2:
                        truck2_o.append(n)
                        truck2_oindex.append(n[1])
                        y = distance_list.index(n)
                        distance_list.pop(y)
                        current_location = new_location
                        shortest_distance(distance_list, 2, current_location)
                    elif truck == 3:
                        truck3_o.append(n)
                        truck3_oindex.append(n[1])
                        y = distance_list.index(n)
                        distance_list.pop(y)
                        current_location = new_location
                        shortest_distance(distance_list, 3, current_location)
        except IndexError:
            pass

# 0 is inserted as the first value in truck1 optimized index
# 0 allows for the first comparison
# number of packages is calculated by subtracting 1 for this index val
truck1_oindex.insert(0, '0')


# Space-time complexity O(1)
# returns truck1 optimized index list
def first_truck_index():
    return truck1_oindex


# Space-time complexity O(1)
def first_truck_optimized():
    return truck1_o


# 0 is inserted as the first value in truck1\2 optimized index
# 0 allows for the first comparison
# number of packages is calculated by subtracting 1 for this index val
truck2_oindex.insert(0, '0')


# Space-time complexity O(1)
# returns truck2 optimized index list
def second_truck_index():
    return truck2_oindex


# Space-time complexity O(1)
def second_truck_optimized():
    return truck2_o


# 0 is inserted as the first value in truck3 optimized index
# 0 allows for the first comparison
# number of packages is calculated by subtracting 1 for this index val
truck3_oindex.insert(0, '0')


# Space-time complexity O(1)
def third_truck_index():
    return truck3_oindex


# Space-time complexity O(1)
# returns truck3 optimized index list
def third_truck_optimized():
    return truck3_o
