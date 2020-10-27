# Vicente Saraos 001090322


from csvreader import get_hash_table
from packages import total_distance
import datetime



class Main:
    # prints total mileage of 3 trucks
    print("Total miles", "{0:.2f}".format(total_distance(), 2), 'miles.')
    # display message for user to 'lookup' a package by id_number or 'timestamp' to view packge status list
    start = input(" 'lookup' to find a package or 'timestamp' to see status of  all packages ")
    # Space-time complexity O(N)
    # program termination condition
    while start != 'exit':
        # if HH:MM:SS entered, display all package statuses
        # O(N)
        if start == 'timestamp':
            try:
                time_input = input()
                (h, m, s) = time_input.split(':')
                search_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # Space-time complexity O(N^2)
                for idn in range(1,41):
                    try:
                        # obtaining times at location[9] and status[10] of each package
                        loc_time = get_hash_table().search(str(idn))[9]
                        status_time = get_hash_table().search(str(idn))[10]
                        (h, m, s) = loc_time.split(':')
                        convert_loc_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                        (h, m, s) = status_time.split(':')
                        convert_status_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                    except ValueError:
                        pass
                        #  Comparison for which packages (trucks) have departed
                        # data map for [0-10] in csvreader.py
                    if convert_loc_time >= search_time:
                        get_hash_table().search(str(idn))[10] = 'At Hub'
                        get_hash_table().search(str(idn))[9] = 'Leaves at ' + loc_time
                        print('Package ID:', get_hash_table().search(str(idn))[0], ' Street address:',
                        get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                        get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                        ' Required delivery time:', get_hash_table().search(str(idn))[5],
                        ' Package weight:', get_hash_table().search(str(idn))[6], ' Truck:',
                        get_hash_table().search(str(idn))[9], ' Delivery status:',
                        get_hash_table().search(str(idn))[10])
                    elif convert_loc_time <= search_time:
                         # Packages en route (not yet delivered and not at hub)
                        if search_time < convert_status_time:
                            get_hash_table().search(str(idn))[10] = 'En Route'
                            get_hash_table().search(str(idn))[9] = 'Departed at ' + loc_time
                            print('Package ID:', get_hash_table().search(str(idn))[0], ' Street address:',
                            get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                            get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                            ' To be delivered before:', get_hash_table().search(str(idn))[5],
                            ' Package weight:', get_hash_table().search(str(idn))[6], '  Truck:',
                            get_hash_table().search(str(idn))[9], '  Delivery status:',
                            get_hash_table().search(str(idn))[10])
                            # else case for delivered packages and time of delivery by package
                        else:
                            get_hash_table().search(str(idn))[10] = 'Delivered at ' + status_time
                            get_hash_table().search(str(idn))[9] = 'Departed at ' + loc_time
                            print('Package ID:', get_hash_table().search(str(idn))[0], '   Street address:',
                            get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                            get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                            ' To be delivered before:', get_hash_table().search(str(idn))[5],
                            ' Package weight:', get_hash_table().search(str(idn))[6],' Truck:',
                            get_hash_table().search(str(idn))[9],' Delivery status:',
                            get_hash_table().search(str(idn))[10])
            except IndexError:
                print('error')
                exit()
            except ValueError:
                print('error')
                exit()
        # else if user types 'lookup' and id_number
        # display package and status of package (time of delivery or status 'at hub' or 'en route')
        elif start == 'lookup':
            try:
                idn = input('package ID: ')
                loc_time = get_hash_table().search(str(idn))[9]
                status_time = get_hash_table().search(str(idn))[10]
                package_status_time = input('Please enter a time in the HH:MM:SS format: ')
                (h, m, s) = package_status_time.split(':')
                search_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = loc_time.split(':')
                convert_loc_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                (h, m, s) = status_time.split(':')
                convert_status_time = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
                # If package is at hub
                if convert_loc_time >= search_time:
                    get_hash_table().search(str(idn))[10] = 'At Hub'
                    get_hash_table().search(str(idn))[9] = 'Departs at ' + loc_time
                    print('Package ID:', get_hash_table().search(str(idn))[0], '   Street address:',
                        get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                        get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                        '  To be delivered before:', get_hash_table().search(str(idn))[5],
                        ' Package weight:', get_hash_table().search(str(idn))[6], '  Truck:',
                        get_hash_table().search(str(idn))[9], '  Delivery status:',
                        get_hash_table().search(str(idn))[10])
                elif convert_loc_time <= search_time:
                    # if the package is en route (departed hub, not yet delivered)
                    if search_time < convert_status_time:
                        get_hash_table().search(str(idn))[10] = 'En Route'
                        get_hash_table().search(str(idn))[9] = 'Departs at ' + loc_time
                        print('Package ID:', get_hash_table().search(str(idn))[0], ' Street address:',
                            get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                            get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                            ' To be delivered before:', get_hash_table().search(str(idn))[5],
                            ' Package weight:', get_hash_table().search(str(idn))[6], ' Truck:',
                            get_hash_table().search(str(idn))[9], ' Delivery status:',
                            get_hash_table().search(str(idn))[10])
                    # else if package is delivered, show user delivery time and package info
                    else:
                        get_hash_table().search(str(idn))[10] = 'Delivered at ' + status_time
                        get_hash_table().search(str(idn))[9] = 'Departs at ' + loc_time
                        print('Package ID:', get_hash_table().search(str(idn))[0], ' Street address:',
                            get_hash_table().search(str(idn))[1], get_hash_table().search(str(idn))[2],
                            get_hash_table().search(str(idn))[3], get_hash_table().search(str(idn))[4],
                            ' To be delivered before:', get_hash_table().search(str(idn))[5],
                            ' Package weight:', get_hash_table().search(str(idn))[6], ' Truck:',
                            get_hash_table().search(str(idn))[9], ' Delivery status:',
                            get_hash_table().search(str(idn))[10])
            except ValueError:
                print('error')
                exit()
        elif start == 'exit':
            exit()
        else:
            print('error')
            exit()


