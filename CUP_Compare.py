# This program outputs a CUP file called "missing_cup_data.cup" in which the user can copy and past the results into
# another CUP file.

# The primary/secondary CUP files need to be specified below. The program will check if there are any CUP data entries
# that are in the secondary but not in the primary. The check is based on GPS location and there is an error limit
# of 2000ft. For example, if there is an airport listing in the primary and in the secondary with a GPS location that is
# within 2000ft, then the program moves on. If an airport in the  secondary doesn't match a GPS location in the primary
# then it is added to the file "missing_cup_data.cup"

import csv
import geopy.distance

secondary_cup_file = "Merlin2021r0.cup"
primary_cup_file = "TIM_CUP.cup"

field_names = ["name",
               "code",
               "country",
               "lat",
               "lon",
               "elev",
               "style",
               "rwdir",
               "rwlen",
               "rwwidth",
               "freq",
               "desc"]


def open_cup(filename):
    temp_file = open(filename)
    reader = csv.DictReader(temp_file)
    list_of_dictionaries = []

    for line in reader:
        if "Related Tasks" not in line['name']:
            list_of_dictionaries.append(line)
    temp_file.close()
    return list_of_dictionaries


def gps_distance_check(lat_0, long_0, lat_1, long_1):
    location_0 = [lat_0, long_0]
    location_1 = [lat_1, long_1]
    return geopy.distance.geodesic(location_0, location_1).nm


def convert_latitude_longitude_to_dd(latitude, longitude):
    # Example Bhanson (43NC): 3601.250N,08030.983W
    # CUP File Latitude Format (AABB.CCCN: AA = Degrees, BB.CCC = Decimal Minute, N = North
    # CUP File Longitude Format (AAABB.CCCW: AAA = Degrees, BB.CCC = Decimal Minute, W = West

    # Strip the North and West
    if latitude.count("N") == 1 and longitude.count("W") == 1:
        latitude = latitude.replace("N", "")
        longitude = longitude.replace("W", "")
    else:
        print("FATAL ERROR: Lat/Long out of range")

    # Convert latitude to Decimal Degrees
    if len(latitude.split(".")[0]) == 4 and len(latitude.split(".")[1]) == 3:
        latitude_degrees = int(latitude[:2])
        latitude_decimal_minutes = float(latitude[-6:])
        latitude = latitude_degrees + latitude_decimal_minutes / 60
        latitude = round(latitude, 7)
    else:
        print("FATAL ERROR: Latitude bad format")

    # Convert longitude to Decimal Degrees
    if len(longitude.split(".")[0]) == 5 and len(longitude.split(".")[1]) == 3:
        longitude_degrees = int(longitude[:3])
        longitude_decimal_minutes = float(longitude[-6:])
        longitude = longitude_degrees + longitude_decimal_minutes / 60
        longitude *= -1
        longitude = round(longitude, 7)
    else:
        print("FATAL ERROR: Longitude bad format")
    return [latitude,longitude]


if __name__ == "__main__":
    list_of_dictionaries_primary = open_cup(primary_cup_file)
    list_of_dictionaries_secondary = open_cup(secondary_cup_file)
    list_of_dictionaries_missing = []

    counter = 0
    for item_secondary in list_of_dictionaries_secondary:
        matched = False
        for item_primary in list_of_dictionaries_primary:
            # Check if a GPS location exists in the secondary that matches the
            gps_primary = convert_latitude_longitude_to_dd(item_primary['lat'], item_primary['lon'])
            gps_secondary = convert_latitude_longitude_to_dd(item_secondary['lat'], item_secondary['lon'])
            # GPS locations are the same, and the secondary cup file has matched with something in the primary
            if geopy.distance.geodesic(gps_primary, gps_secondary).ft < 2000:
                matched = True

                # Confirm that the airport codes are the same
                if item_secondary['code'] != item_primary['code']:
                    print("ERROR: GPS Match but airport code doesn't match [primary/secondary]:")
                    print(item_primary['name'], item_secondary['name'])
                    print(item_primary['code'],item_secondary['code'])
        if not matched:
            print("Primary Missing:", item_secondary['name'],"(", item_secondary['code'],")")
            print(gps_secondary[0],",",gps_secondary[1])
            # Add missing airport to list
            list_of_dictionaries_missing.append(item_secondary)

    if list_of_dictionaries_missing:
        new_cup_file = open("missing_cup_data.cup", "w", newline='')
        writer = csv.DictWriter(new_cup_file, fieldnames=field_names, delimiter=",")
        writer.writeheader()
        for line in list_of_dictionaries_missing:
            writer.writerow(line)
        new_cup_file.close()
