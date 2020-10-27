# Vicente Saraos 001090322

import datetime
import trucks

from trucks import get_location
from trucks import first_truck_time
from trucks import second_truck_time
from trucks import third_truck_time
from trucks import first_truck_index
from trucks import first_truck_optimized
from trucks import second_truck_index
from trucks import second_truck_optimized
from trucks import third_truck_index
from trucks import third_truck_optimized
from trucks import shortest_distance
from trucks import distances_list
from csvreader import get_hash_table
from csvreader import first_truck_trip1
from csvreader import second_truck_trip1
from csvreader import first_truck_trip2

# delivery routes
first_trip = []
second_trip = []
third_trip = []

# cargo manifest
first_truck = []
second_truck = []
third_truck = []

# departure times of trucks from hub
# first truck departs at 8am at the earliest
# second truck departs 5 minutes after delayed packages arrive
# third truck departs after the first returns
departure1 = '8:00:00'
departure2 = '9:10:00'
departure3 = '11:00:00'

# str departure times to datetime
(h, m, s) = departure1.split(':')
time_extract = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure2.split(':')
time_extract2 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
(h, m, s) = departure3.split(':')
time_extract3 = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))

# iteration variable
x = 0
# Space-time complexity O(N)
# status of packages on truck 1 set to departure time
# and copies package list on truck to the triplist
for package in first_truck_trip1():
    first_truck_trip1()[x][9] = departure1
    first_trip.append(first_truck_trip1()[x])
    x += 1

# Space-time complexity O(N^2)
# truck 1 route is a list of each package delivery address index
# each package's delivery address index is obtained by checking for address equality
# then each index is stored with the package information and the delivery route list
try:
    # iteration variable
    y = 0
    for package in first_trip:
        for address in trucks.address():
            if package[1] == address[2]:
                first_truck.append(address[0])
                first_trip[y][1] = address[0]
        y += 1
except IndexError:
    pass

# sorting packages by delivery address index (distance)
# O(N^2)
shortest_distance(first_trip, 1, 0)

# total travelled distance of truck1
truck1_total_distance = 0
# iteration variable
package_id_number = 0
# Space-time complexity O(N)
# calculates total travel distance of truck1 by accessing the distance data
# retrieved by comparing the package delivery indices to WGUPS Distance Data
# updates package delivery time
for x in range(len(first_truck_index())):
    try:
        truck1_total_distance = distances_list(int(first_truck_index()[x]),
                                              int(first_truck_index()[x + 1]), truck1_total_distance)
        # checking package location
        deliver = first_truck_time(get_location(int(first_truck_index()[x]),
                                                int(first_truck_index()[x + 1])))
        # updating package status
        first_truck_optimized()[package_id_number][10] = (str(deliver))
        get_hash_table().update(int(first_truck_optimized()[package_id_number][0]), first_trip)
        package_id_number += 1
    except IndexError:
        pass

# iteration variable
x = 0
# Space-time complexity O(N)
# status of packages on truck 2 set to departure time
# and copies package list on truck to the triplist
for package in second_truck_trip1():
    second_truck_trip1()[x][9] = departure2
    second_trip.append(second_truck_trip1()[x])
    x += 1


try:
    # iteration variable initialization
    y = 0
    # Space-time complexity O(N^2)
    # truck 2 route is a list of each package delivery address index
    # each package's delivery address index is obtained by checking for address equality
    # then each index is stored with the package information and the delivery route list
    for package in second_trip:
        for address in trucks.address():
            if package[1] == address[2]:
                second_truck.append(address[0])
                second_trip[y][1] = address[0]
        y += 1
except IndexError:
    pass

# sorting packages by delivery address index (distance)
# O(N^2)
shortest_distance(second_trip, 2, 0)

# total travelled distance of truck2
truck2_total_distance = 0
# iteration variable
package_id_number = 0
# Space-time complexity O(N)
# calculates total travel distance of truck2 by accessing the distance data
# retrieved by comparing the package delivery indices to WGUPS Distance Data
# updates package delivery time
for x in range(len(second_truck_index())):
    try:
        truck2_total_distance = distances_list(int(second_truck_index()[x]),
                                          int(second_truck_index()[x + 1]), truck2_total_distance)
        # checking package location
        deliver = second_truck_time(get_location(int(second_truck_index()[x]), int(second_truck_index()[x + 1])))
        # updating package status
        second_truck_optimized()[package_id_number][10] = (str(deliver))
        get_hash_table().update(int(second_truck_optimized()[package_id_number][0]), second_trip)
        package_id_number += 1
    except IndexError:
        pass

# iteration variable initialization
x = 0
# Space-time complexity O(N)
# status of packages on truck 1 trip2 set to departure time
# and copies package list on truck to the triplist
for package in first_truck_trip2():
    first_truck_trip2()[x][9] = departure3
    third_trip.append(first_truck_trip2()[x])
    x += 1

try:
    # iteration variable initialization
    y = 0
    # Space-time complexity O(N^2)
    # truck1 trip2 route is a list of each package delivery address index
    # each package's delivery address index is obtained by checking for address equality
    # then each index is stored with the package information and the delivery route list
    for package in third_trip:
        for address in trucks.address():
            if package[1] == address[2]:
                third_truck.append(address[0])
                third_trip[y][1] = address[0]
        y += 1
except IndexError:
    pass

# sorting packages by delivery address index (distance)
# O(N^2)
shortest_distance(third_trip, 3, 0)

# total travelled distance of truck2
truck3_total_distance = 0
# iteration variable
package_id_number = 0
# Space-time complexity O(N)
# calculates total travel distance of truck2 by accessing the distance data
# retrieved by comparing the package delivery indices to WGUPS Distance Data
for x in range((len(third_truck_index()))):
    try:
        truck3_total_distance = distances_list(int(third_truck_index()[x]),
                                          int(third_truck_index()[x + 1]), truck3_total_distance)
        # checking package location
        deliver = third_truck_time(get_location(int(third_truck_index()[x]), int(third_truck_index()[x + 1])))
        # updating package status
        third_truck_optimized()[package_id_number][10] = (str(deliver))
        get_hash_table().update(int(third_truck_optimized()[package_id_number][0]), third_trip)
        package_id_number += 1
    except IndexError:
        pass

# Space-time complexity O(1)
# sums and returns the travel distance of each truck
def total_distance():
    sumtotal_distance = truck1_total_distance + truck2_total_distance + truck3_total_distance
    return sumtotal_distance


# print data for reviewer, prints each truck travel distance,
# how many packages on each truck (-1 for index 0),
# and total distance (sum of all trucks)
print("truck1_total_distance", truck1_total_distance)
print("truck1 has ", len(first_truck_index())-1, "packages")
print("truck2_total_distance", truck2_total_distance)
print("truck2 has ", len(second_truck_index())-1, "packages")
print("truck3_total_distance", truck3_total_distance)
print("truck3 has ", len(third_truck_index())-1, "packages")
print("sumtotal_distance", total_distance())