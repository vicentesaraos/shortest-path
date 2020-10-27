# Vicente Saraos 001090322

# Chaining hash table
class ChainingHashTable:

    # Constructor to initialize chain hash table
    # size of 20 < 40 packages
    # Space-time complexity O(1),
    def __init__(self, length=20):
        # initialize an empty hash table
        self.table = [[] for _ in range(length)]

    # Space-time complexity O(1)
    # private hash function returns bucket_number (location/index of list of bucketlists)
    # not for use by user
    # use by chaininghashtable functions
    def __hash(self, id_number):
        bucket_number = int(id_number) % len(self.table)
        return bucket_number

    # Space-time complexity O(1)
    # inserts package to hash table either at 0th index (first location of a bucket list)
    # or by appending to the bucket_list if bucket_list has one packagedata
    def insert(self, id_number, package_data):
        bucket_list = self.__hash(id_number)
        package = [id_number, package_data]
        if self.table[bucket_list] == []:
            self.table[bucket_list] = list([package])
            return "Package inserted"
        else:
            self.table[bucket_list].append(package)
            return "Package added"

    # Space-time complexity O(N)
    # returns package information (id, address, city, zip, etc)
    def search(self, id_number):
        bucket_list = self.__hash(id_number)
        if self.table[bucket_list] != []:
            for sublist in self.table[bucket_list]:
                if sublist[0] == id_number:
                    return sublist[1]
        return None

    # Space-time complexity O(N)
    # Remove package from hash table
    def remove(self, id_number):
        bucket_list = self.__hash(id_number)
        if bucket_list == []:
            return "Not Found"
        for sublist in range(0, len(self.table[bucket_list])):
            if self.table[bucket_list][sublist][0] == id_number:
                del self.table[bucket_list][sublist][0]
                return "Package deleted"

    # Space-time complexity O(N)
    # update package data
    def update(self, id_number, package_data):
        bucket_list = self.__hash(id_number)
        if bucket_list == []:
            return "error"
        else:
            for index in self.table[bucket_list]:
                if index[0] == id_number:
                    index[1] = package_data
                    print(index[1])


