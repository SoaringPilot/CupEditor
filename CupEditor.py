# class for airport
# variables that define the main parameters of the airport
# runway dimensions
# radio frequency
# location coordinates
# runway directions
# airport elevation

import os
import re
import sys
import time

import requests
import csv
from prettytable import PrettyTable
import geopy.distance
from PIL import Image
from CupEditor_GUI import Ui_MainWindow
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

# from PyQt5.QtGui import QPixmap

DIRECTION_ERR = 20  # Units: Degrees, acceptable error for differences in runway direction
ELEV_ERR = 50  # Units: Feet, acceptable error for elevation differences
LENGTH_ERR = 100  # Units: Feet, acceptable error for runway length differences
WIDTH_ERR = 10  # Units: Feet, acceptable error for runway width differences
LOCATION_ERR = 1000  # Units: Fee t, acceptable error for lat/long differences
INPUT = "BALLr21.cup"
OUTPUT = "BALLr22.cup"


# Calculate the distance between GPS coordinates, return the difference in nautical miles
def gps_distance_check(lat_0, long_0, lat_1, long_1):
    location_0 = [lat_0, long_0]
    location_1 = [lat_1, long_1]
    return geopy.distance.geodesic(location_0, location_1).nm


# Type and order of data listed in CUP file
field_names = ["Waypoint Name",
               "Code",
               "Country",
               "Latitude",
               "Longitude",
               "Elevation",
               "Waypoint Style",
               "Runway Direction",
               "Runway Length",
               "Runway Width",
               "Airport Frequency",
               "Description",
               "User Data",
               "pics"]


# TODO, need to add in code that scrapes websites data

class AirportFromFile:
    airport_count = 0
    airport_count_with_comms = 0
    airports_with_no_data = []

    def __init__(self, input_airport_filename: str):
        self.iata = input_airport_filename.split('.')[0]
        self.airport_name = ""
        self.ctaf = False
        self.unicom = False
        self.multicom = False
        self.coordinates = ["lat", "long"]
        self.runway_directions = []
        self.surface = []
        self.runway_length = []
        self.runway_width = []
        self.elevation_ft = 0
        self.airport_file_path = "./Airports/"
        self.website_text = ""
        self.is_file_empty = True
        self.is_data_missing_from_file = False
        AirportFromFile.airport_count += 1

        # Call Init Methods
        self.init_website_text()
        self.find_airport_name()
        self.find_airport_frequencies()
        self.find_airport_coordinates()
        self.find_runway_directions()
        self.find_elevation()
        self.find_surface_type()
        self.find_runway_dimensions()
        self.check_if_data_is_missing()

    def check_if_data_is_missing(self):
        if not self.get_airport_comm_frequency():
            self.is_data_missing_from_file = True
        if self.coordinates == ["lat", "long"]:
            self.is_data_missing_from_file = True
        if not self.runway_directions:
            self.is_data_missing_from_file = True
        if not self.surface:
            self.is_data_missing_from_file = True
        if not self.runway_length:
            self.is_data_missing_from_file = True
        if not self.runway_width:
            self.is_data_missing_from_file = True
        if self.elevation_ft == 0:
            self.is_data_missing_from_file = True

    def print_attributes(self):
        print("==========================================")
        print("  ", self.iata, "\t", self.airport_name)
        print("==========================================")
        print("Lat/Long:", self.coordinates)
        print("Elevation (ft): ", self.elevation_ft)
        print("Type: ")
        print("Runway: ", self.runway_directions)
        print("Frequency: ", self.ctaf)
        print("Description:")
        print("User Data:")

    def init_website_text(self):
        f = open(self.airport_file_path + self.iata + '.txt')
        data = f.read()
        # If lat/long is not listed, then the airport information doesn't exist on AirNav website
        if data.count('Lat/Long:'):
            self.website_text = data
            self.is_file_empty = False
        else:
            AirportFromFile.airports_with_no_data.append(self.iata)
        f.close()

    # Find the CTAF and/or UNICOM
    def find_airport_frequencies(self):
        keys = ['CTAF:', 'UNICOM:', 'CTAF/UNICOM:', 'MULTICOM - ']

        for key in keys:

            if self.website_text.count(key) > 0:
                # Iterate airport_count_with_comms if this is the first time finding a match
                if not self.ctaf and not self.unicom and not self.multicom:
                    AirportFromFile.airport_count_with_comms += 1
                extracted_frequency = self.website_text.split(key)[1].split("\n")[0]
                # Assign frequency
                if key == keys[0]:
                    self.ctaf = extracted_frequency
                elif key == keys[1]:
                    self.unicom = extracted_frequency
                elif key == keys[3]:
                    self.multicom = extracted_frequency
                else:
                    self.ctaf = extracted_frequency
                    self.unicom = extracted_frequency

    def find_airport_coordinates(self):
        # Pull out the decimal degree version:
        # Lat/Long:36-01-15.0000N 080-30-59.0000W36-01.250000N 080-30.983333W36.0208333,-80.5163889(estimated)
        # End Result = 36.0208333,-80.5163889
        key = 'Lat/Long:'
        if self.website_text.count(key) == 1:
            temp = self.website_text.split(key)[1].split('\n')[0]
            temp = temp.split("W")[2]
            temp = temp.replace("(estimated)", "")
            temp = temp.split(",")
            self.coordinates = temp

    def find_runway_directions(self):
        pattern_runway_numbers = re.compile("Runway [0-9]{1,2}/[0-9]{1,2}")  # i.e. 1/19
        pattern_runway_letters = re.compile("Runway [a-zA-Z]{1,2}/[a-zA-Z]{1,2}")  # i.e. E/W or NE/SW
        pattern_runway_parallel = re.compile("Runway [0-9]{1,2}[RL]{1}/[0-9]{1,2}[RL]{1}")  # i.e. 2R/20L
        pattern_runway_water = re.compile("Runway [0-9]{1,2}[W]{1}/[0-9]{1,2}[W]{1}")  # i.e. 5W/23W (Water)
        listed_number_runways = pattern_runway_numbers.findall(self.website_text)
        listed_letter_runways = pattern_runway_letters.findall(self.website_text)
        listed_parallel_runways = pattern_runway_parallel.findall(self.website_text)
        listed_water_runways = pattern_runway_water.findall(self.website_text)

        # If the website data is valid, exclude heliports, and then combine all runways listed
        if self.website_text and self.website_text.count("Heliport") == 0:
            # Remove the text "Runway " from the result if applicable
            for i in range(len(listed_number_runways)):
                if listed_number_runways[i].count("Runway "):
                    listed_number_runways[i] = listed_number_runways[i].replace("Runway ", "")
            for i in range(len(listed_letter_runways)):
                if listed_letter_runways[i].count("Runway "):
                    listed_letter_runways[i] = listed_letter_runways[i].replace("Runway ", "")
            for i in range(len(listed_parallel_runways)):
                if listed_parallel_runways[i].count("Runway "):
                    listed_parallel_runways[i] = listed_parallel_runways[i].replace("Runway ", "")
            # Add all the lists together
            self.runway_directions = listed_number_runways + listed_letter_runways + listed_parallel_runways

    def find_runway_dimensions(self):
        pattern_runway_dimensions = re.compile("Dimensions:[0-9]{1,5} x [0-9]{1,4}")  # i.e. Dimensions:2250 x 150 ft.
        listed_runway_dimensions = pattern_runway_dimensions.findall(self.website_text)
        # Remove the text "Dimensions:"
        for i in range(len(listed_runway_dimensions)):
            if listed_runway_dimensions[i].count("Dimensions:"):
                listed_runway_dimensions[i] = listed_runway_dimensions[i].replace("Dimensions:", "")
                # Remove Spaces
                if listed_runway_dimensions[i].count(" "):
                    listed_runway_dimensions[i] = listed_runway_dimensions[i].replace(" ", "")

        # Split dimensions into length and width
        for i in range(len(listed_runway_dimensions)):
            if listed_runway_dimensions[i].count("x") == 1:
                self.runway_length.append(listed_runway_dimensions[i].split("x")[0])
                self.runway_width.append(listed_runway_dimensions[i].split("x")[1])

    def find_elevation(self):
        key = 'Elevation:'
        if self.website_text.count(key) >= 1:
            self.elevation_ft = self.website_text.split(key)[1].split(" ")[0]

    def get_airport_comm_frequency(self):
        if self.ctaf:
            return self.ctaf
        elif self.unicom:
            return self.unicom
        elif self.multicom:
            return self.multicom
        else:
            return ""

    def find_surface_type(self):
        pattern_surface = re.compile("Surface:.+")
        listed_surface = pattern_surface.findall(self.website_text)

        for i in range(len(listed_surface)):
            listed_surface[i] = listed_surface[i].replace("Surface:", "")
            self.surface.append(listed_surface[i])

    def find_airport_name(self):
        key = '- '
        if self.website_text.count(key):
            temp = self.website_text.split(key)[1].split("\n")[0]
            self.airport_name = temp


class AirportFromCup:
    airport_count = 0
    airport_count_with_comms = 0
    cup_code_list = []

    style_list = [
        "Unknown",
        "Waypoint",
        "Airfield with Grass Surface Runway",
        "Outlanding",
        "Gliding Airfield",
        "Airfield with Solid Surface Runway",
        "Mountain Pass",
        "Mountain Top",
        "Transmitter Mast",
        "VOR",
        "NDB",
        "Cooling Tower",
        "Dam",
        "Tunnel",
        "Bridge",
        "Power Plant",
        "Castle",
        "Intersection",
        "Marker",
        "Control/Reporting Point",
        "PG Take Off",
        "PG Landing Zone"
    ]

    def __init__(self, csv_dictionary: dict):
        self.original_cup_data = csv_dictionary.copy()  # Copy is required to separate link from calling function
        self.updated_cup_data = csv_dictionary.copy()  # Copy is required to separate link to original_cup_data
        self.waypoint_name = ""
        self.code = ""
        self.country = ""
        self.latitude = ""
        self.longitude = ""
        self.elevation = ""
        self.waypoint_style = ""
        self.runway_direction = ""
        self.runway_direction_standard = ""
        self.runway_length = ""
        self.runway_width = ""
        self.airport_frequency = ""
        self.description = ""
        self.user_data = ""
        self.pics = ""
        self.is_data_missing = False  # TODO: Check if this will catch
        self.missing_data = []
        self.set_class_variables()

    def set_class_variables(self):
        self.waypoint_name = self.original_cup_data.get("Waypoint Name")
        self.code = self.original_cup_data.get("Code")
        self.country = self.original_cup_data.get("Country")
        self.latitude = self.original_cup_data.get("Latitude")
        self.longitude = self.original_cup_data.get("Longitude")
        self.elevation = self.convert_to_feet(self.original_cup_data.get("Elevation"))
        self.waypoint_style = AirportFromCup.style_list[int(self.original_cup_data.get("Waypoint Style"))]
        self.runway_direction = self.original_cup_data.get("Runway Direction")
        # Convert self.runway_direction from 0-359 to 0 to 36
        self.convert_runway_to_standard()
        self.runway_length = self.convert_to_feet(self.original_cup_data.get("Runway Length"))
        self.runway_width = self.convert_to_feet(self.original_cup_data.get("Runway Width"))
        self.airport_frequency = self.original_cup_data.get("Airport Frequency")
        self.description = self.original_cup_data.get("Description")
        self.user_data = self.original_cup_data.get("User Data")
        self.pics = self.original_cup_data.get("pics")
        # Create a list of all the airport codes to make sure they are all unique
        AirportFromCup.cup_code_list.append(self.code)

        # Check what data is missing from the CUP
        for key in self.original_cup_data.keys():
            # Find out what is missing from the CUP file
            if self.original_cup_data.get(key) == "":
                self.missing_data.append(key)

        # Convert the CUP Lat/Long to Decimal Degrees
        if self.latitude and self.longitude:
            self.convert_latitude_longitude_to_dd()

        # TODO: need to boil up somewhere
        if AirportFromCup.cup_code_list.count(self.code) != 1:
            print("PROBLEM:")
            self.print_attributes()

    def convert_to_feet(self, input_string: str):
        if input_string.count("m"):
            to_convert = float(input_string.replace("m", ""))
            result = str(round(to_convert * 3.281))
        elif input_string.count("ft"):
            to_convert = float(input_string.replace("ft", ""))
            result = str(round(to_convert))
        else:
            result = ""
        return result

    def convert_runway_to_standard(self):
        to_convert = int(self.runway_direction)
        other_runway = (to_convert + 180) % 360
        to_convert /= 10
        other_runway /= 10
        to_convert = round(to_convert)
        other_runway = round(other_runway)
        self.runway_direction_standard = str(to_convert) + "/" + str(other_runway)

    # Convert to decimal degrees to compare if the Lat/Long matches file data
    def convert_latitude_longitude_to_dd(self):
        # Example Bhanson (43NC): 3601.250N,08030.983W
        # CUP File Latitude Format (AABB.CCCN: AA = Degrees, BB.CCC = Decimal Minute, N = North
        # CUP File Longitude Format (AAABB.CCCW: AAA = Degrees, BB.CCC = Decimal Minute, W = West

        # Strip the North and West
        if self.latitude.count("N") == 1 and self.longitude.count("W") == 1:
            self.latitude = self.latitude.replace("N", "")
            self.longitude = self.longitude.replace("W", "")
        else:
            print("FATAL ERROR: Lat/Long out of range")

        # Convert latitude to Decimal Degrees
        if len(self.latitude.split(".")[0]) == 4 and len(self.latitude.split(".")[1]) == 3:
            latitude_degrees = int(self.latitude[:2])
            latitude_decimal_minutes = float(self.latitude[-6:])
            self.latitude = latitude_degrees + latitude_decimal_minutes / 60
            self.latitude = round(self.latitude, 7)
        else:
            print("FATAL ERROR: Latitude bad format")

        # Convert longitude to Decimal Degrees
        if len(self.longitude.split(".")[0]) == 5 and len(self.longitude.split(".")[1]) == 3:
            longitude_degrees = int(self.longitude[:3])
            longitude_decimal_minutes = float(self.longitude[-6:])
            self.longitude = longitude_degrees + longitude_decimal_minutes / 60
            self.longitude *= -1
            self.longitude = round(self.longitude, 7)
        else:
            print("FATAL ERROR: Longitude bad format")

    def update_frequency(self, frequency):
        # Check if the new frequency is different from the data to be written to the new CUP file
        if frequency != self.updated_cup_data.get("Airport Frequency"):
            # Update the airport's frequency and the data to be written to the new CUP file
            self.airport_frequency = frequency
            self.updated_cup_data.update({"Airport Frequency": frequency})
            return True
        else:
            return False

    def update_elevation(self, elevation):
        # Check if the new elevation is different from the data to be written to the new CUP file
        # Note: sometimes the updated_cup_data is original which contains the elevation data in meters, so convert
        if elevation != self.convert_to_feet(self.updated_cup_data.get("Elevation")).replace("ft", ""):
            self.elevation = elevation
            self.updated_cup_data.update({"Elevation": elevation + "ft"})
            return True
        else:
            return False

    def update_length(self, length):
        # Check if the new length is different from the data to be written to the new CUP file
        # Note: sometimes the updated_cup_data is original which contains the length data in meters, so convert
        if length != self.convert_to_feet(self.updated_cup_data.get("Runway Length")).replace("ft", ""):
            self.runway_length = length
            self.updated_cup_data.update({"Runway Length": length + "ft"})
            return True
        else:
            return False

    def update_width(self, width):
        # Check if the new width is different from the data to be written to the new CUP file
        # Note: sometimes the updated_cup_data is original which contains the width data in meters, so convert
        if width != self.convert_to_feet(self.updated_cup_data.get("Runway Width")).replace("ft", ""):
            self.runway_width = width
            self.updated_cup_data.update({"Runway Width": width + "ft"})
            return True
        else:
            return False

    def update_waypoint_style(self, style):
        # Check if the new style is different from the data to be written to the new CUP file
        # Note: self.waypoint_style is the text equivalent, not the integer
        if str(AirportFromCup.style_list.index(style)) != self.updated_cup_data.get("Waypoint Style"):
            self.waypoint_style = style
            style_index = str(AirportFromCup.style_list.index(style))
            self.updated_cup_data.update({"Waypoint Style": style_index})
            return True
        else:
            return False

    def update_runway_direction(self, direction):
        # Check if the new direction is different from the data to be written to the new CUP file
        # Note: the direction has to be simplified from 18/36 to 180
        if direction.count("/"):
            temp = direction.split("/")[0]
            converted = str(int(temp) * 10)
            if converted != self.updated_cup_data.get("Runway Direction"):
                self.runway_direction = converted
                self.updated_cup_data.update({"Runway Direction": converted})
                return True
        else:
            return False

    def update_latitude(self, latitude):
        # Check if the new latitude is different from the data to be written to the new CUP file
        # Note: The incoming latitude is in decimal degrees, need to convert to DDM to compare
        latitude = float(latitude)
        degree = int(latitude)
        remainder = (latitude % degree)
        partial = remainder * 60
        converted = str(degree) + "%06.3f" % partial + "N"
        if converted != self.updated_cup_data.get("Latitude"):
            self.latitude = float(latitude)
            self.updated_cup_data.update({"Latitude": converted})
            return True
        else:
            return False

    def update_longitude(self, longitude):
        # Check if the new longitude is different from the data to be written to the new CUP file
        # Note: The incoming longitude is in decimal degrees, need to convert to DDM to compare
        longitude = float(longitude)
        temp = abs(int(longitude))
        remainder = (abs(longitude) % temp)
        new_number = remainder * 60
        converted = "%03.0f" % temp + "%06.3f" % new_number + "W"
        if converted != self.updated_cup_data.get("Longitude"):
            self.longitude = longitude
            self.updated_cup_data.update({"Longitude": converted})
            return True
        else:
            return False

    def update_waypoint_name(self, new_name):
        # Check if the new name is different from the data to be written to the new CUP file
        if new_name != self.updated_cup_data.get("Waypoint Name"):
            self.waypoint_name = new_name
            self.updated_cup_data.update({"Waypoint Name": new_name})
            return True
        else:
            return False

    def update_code(self, new_code):
        # Check if the new code is different from the data to be written to the new CUP file
        if new_code != self.updated_cup_data.get("Code"):
            self.code = new_code
            self.updated_cup_data.update({"Code": new_code})
            return True
        else:
            return False

    def print_attributes(self):
        print("==========================================")
        print("  ", self.code, "\t", self.waypoint_name)
        print("==========================================")
        print("Lat/Long:", self.latitude, self.longitude)
        print("Elevation (ft): ", self.elevation)
        print("Type: ", self.waypoint_style)
        print("Runway: ", self.runway_direction, " ", self.runway_length, "x", self.runway_width, "ft")
        print("Frequency: ", self.airport_frequency)
        print("Description:", self.description)
        print("User Data:", self.user_data)


class Airport:
    def __init__(self, cup_airport: AirportFromCup, file_airport: AirportFromFile):
        self.cup_airport = cup_airport
        self.file_airport = file_airport
        self.name = self.cup_airport.code

    def print_pair(self):
        table = []
        row2 = []
        row3 = []
        row4 = []
        row5 = []

        # Row of descriptors
        row0 = [self.name, 'Lat', 'Long', 'Elevation(ft)', 'Type', 'Runway', 'Length(ft)', 'Width(ft)', 'Frequency',
                'Description']
        # Row for CUP file data
        row1 = ['CUP', self.cup_airport.latitude, self.cup_airport.longitude, self.cup_airport.elevation,
                self.cup_airport.waypoint_style, self.cup_airport.runway_direction,
                self.cup_airport.runway_length,
                self.cup_airport.runway_width, self.cup_airport.airport_frequency, self.cup_airport.description]
        # If one runway is listed from file
        if len(self.file_airport.runway_directions) >= 1:
            row2 = ['Online', self.file_airport.coordinates[0], self.file_airport.coordinates[1],
                    self.file_airport.elevation_ft, self.file_airport.surface[0],
                    self.file_airport.runway_directions[0],
                    self.file_airport.runway_length[0], self.file_airport.runway_width[0],
                    self.file_airport.get_airport_comm_frequency(), self.file_airport.airport_name]
        # If there are more than one runway listed from file, add additional rows to the table for ease of reading
        if len(self.file_airport.runway_directions) >= 2:
            row3 = ['', '', '', '', self.file_airport.surface[1], self.file_airport.runway_directions[1],
                    self.file_airport.runway_length[1], self.file_airport.runway_width[1], '', '']
        if len(self.file_airport.runway_directions) >= 3:
            row4 = ['', '', '', '', self.file_airport.surface[2], self.file_airport.runway_directions[2],
                    self.file_airport.runway_length[2], self.file_airport.runway_width[2], '', '']
        if len(self.file_airport.runway_directions) >= 4:
            row5 = ['', '', '', '', self.file_airport.surface[3], self.file_airport.runway_directions[3],
                    self.file_airport.runway_length[3], self.file_airport.runway_width[3], '', '']
        if len(self.file_airport.runway_directions) == 0:
            table = [row0, row1]
        elif len(self.file_airport.runway_directions) == 1:
            table = [row0, row1, row2]
        elif len(self.file_airport.runway_directions) == 2:
            table = [row0, row1, row2, row3]
        elif len(self.file_airport.runway_directions) == 3:
            table = [row0, row1, row2, row3, row4]
        elif len(self.file_airport.runway_directions) == 4:
            table = [row0, row1, row2, row3, row4, row5]

        tab = PrettyTable(table[0])
        tab.add_rows(table[1:])
        print(tab)
        # return tab.get_string()


class AirportValidation(Airport):

    def __init__(self, cup_airport, file_airport):
        super().__init__(cup_airport, file_airport)
        self.error_count = None
        self.flag_frequency_has_error = None
        self.flag_elevation_has_error = None
        self.flag_runway_direction_has_error = None
        self.flag_runway_direction_validated = None
        self.flag_runway_length_has_error = None
        self.flag_runway_length_validated = None
        self.flag_runway_width_has_error = None
        self.flag_runway_width_validated = None
        self.flag_runway_surface_has_error = None
        self.flag_runway_surface_validated = None
        self.flag_runway_coordinates_have_error = None
        self.flag_runway_coordinates_validated = None

        self.run_validation()

    def run_validation(self):
        self.error_count = 0
        self.flag_frequency_has_error = False
        self.flag_elevation_has_error = False
        self.flag_runway_direction_has_error = True  # Easier to start with True and prove otherwise
        self.flag_runway_direction_validated = False
        self.flag_runway_length_has_error = True  # Easier to start with True and prove otherwise
        self.flag_runway_length_validated = False
        self.flag_runway_width_has_error = True
        self.flag_runway_width_validated = False
        self.flag_runway_surface_has_error = True
        self.flag_runway_surface_validated = False
        self.flag_runway_coordinates_have_error = True
        self.flag_runway_coordinates_validated = False

        self.validate_frequency()
        self.validate_elevation()
        self.validate_runway_directions()
        self.validate_latitude_longitude()

    def validate_frequency(self):
        # If the frequency is missing from the CUP
        if not self.cup_airport.airport_frequency:
            # If there is a frequency listed in the file then there is a CUP error
            if self.file_airport.get_airport_comm_frequency():
                self.error_count += 1
                self.flag_frequency_has_error = True
        # Check if the frequency listed matches data in the files
        else:
            check1 = self.file_airport.get_airport_comm_frequency()
            check2 = self.cup_airport.airport_frequency
            # Only compare file airports with frequency data and count an error if the frequencies are different
            if check1 and float(check1) != float(check2):
                self.error_count += 1
                self.flag_frequency_has_error = True

    def validate_elevation(self):
        diff = int(abs((float(self.cup_airport.elevation) - float(self.file_airport.elevation_ft))))
        # Flag if the difference in reported elevation is greater than ELEV_ERR
        if (diff > ELEV_ERR) and airports_from_file[index_for_file].website_text:
            self.error_count += 1
            self.flag_elevation_has_error = True

    def validate_runway_directions(self):
        if self.file_airport.runway_directions:
            for i in range(len(self.file_airport.runway_directions)):
                file_runway_a_extracted = self.file_airport.runway_directions[i].split("/")[0]
                file_runway_b_extracted = self.file_airport.runway_directions[i].split("/")[1]
                runway_a = False
                runway_b = False

                # Check if Left and Right runways exist and delete the reference
                if file_runway_a_extracted.count("L"):
                    file_runway_a_extracted = file_runway_a_extracted.replace("L", "")
                if file_runway_a_extracted.count("R"):
                    file_runway_a_extracted = file_runway_a_extracted.replace("R", "")
                if file_runway_b_extracted.count("L"):
                    file_runway_b_extracted = file_runway_b_extracted.replace("L", "")
                if file_runway_b_extracted.count("R"):
                    file_runway_b_extracted = file_runway_b_extracted.replace("R", "")
                # Number Runway, convert to integer and then multiply by 10 i.e. 1/19 to 10/190 for comparison with CUP
                if file_runway_a_extracted.isdigit() and file_runway_b_extracted.isdigit():
                    runway_a = int(file_runway_a_extracted) * 10
                    runway_b = int(file_runway_b_extracted) * 10

                # Lettered Runway, convert to magnetic 1-360, i.e. E/W -> 90/270
                elif file_runway_a_extracted.isalpha() and file_runway_b_extracted.isalpha():
                    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']
                    numbers = [360, 45, 90, 135, 180, 225, 270, 315]

                    for j in range(len(directions)):
                        if file_runway_a_extracted == directions[j]:
                            runway_a = numbers[j]
                        if file_runway_b_extracted == directions[j]:
                            runway_b = numbers[j]

                # This should never happen, but just in case
                else:
                    print("Fatal Error")

                # Convert CUP runway to a number, and filter out bad data
                if self.cup_airport.runway_direction != "":
                    converted = int(self.cup_airport.runway_direction)
                    if converted == 0:
                        converted = 360
                    if 0 < converted <= 360:
                        cup_runway_number = converted
                    else:
                        print("Error CUP Rwy Dir, ", self.name, converted)
                        cup_runway_number = False
                else:
                    cup_runway_number = False

                # Compare results if all are valid
                if cup_runway_number and runway_a and runway_b:
                    lower_bounds = (cup_runway_number - DIRECTION_ERR) % 360
                    upper_bounds = (cup_runway_number + DIRECTION_ERR) % 360
                    checks = [runway_a, runway_b]

                    # Check if runway direction from file is within +/- DIRECTION_ERR from CUP direction
                    if lower_bounds < upper_bounds:
                        for check in checks:
                            # Check if the runway matches i.e. runway 1 of 1/19 or runway 19 of 1/19
                            if lower_bounds <= check <= upper_bounds:
                                self.flag_runway_direction_has_error = False
                                self.flag_runway_direction_validated = True
                                # Validate the runway i of the iteration, i.e. the second runway in the list of runways
                                self.validate_runway_length(i)
                                self.validate_runway_width(i)
                                self.validate_runway_surface(i)
                            elif not self.flag_runway_direction_validated:
                                self.flag_runway_direction_has_error = True

                    # Complicated Case: acceptable runway range spans over 360 degrees
                    elif lower_bounds > upper_bounds:
                        for check in checks:
                            # Check if airport between the upper bounds and 360 (0 after mod)
                            if 0 <= (check % 360) <= upper_bounds:
                                self.flag_runway_direction_has_error = False
                                self.flag_runway_direction_validated = True
                                # Validate the runway i of the iteration, i.e. the second runway in the list of runways
                                self.validate_runway_length(i)
                                self.validate_runway_width(i)
                                self.validate_runway_surface(i)
                            elif 359 >= check >= lower_bounds:
                                self.flag_runway_direction_has_error = False
                                self.flag_runway_direction_validated = True
                                # Validate the runway i of the iteration, i.e. the second runway in the list of runways
                                self.validate_runway_length(i)
                                self.validate_runway_width(i)
                                self.validate_runway_surface(i)
                            elif not self.flag_runway_direction_validated:
                                self.flag_runway_direction_has_error = True

            # All possible runways from the file have been compared, increment the error counter if no direction match
            if self.flag_runway_direction_has_error:
                self.error_count += 1
                print("\n")
                self.print_pair()
                print("ERROR: DIRECTION")

                # With no matched runway directions, the length, width, and surface conditions were not compared yet.
                #   If the airport is a single runway, these parameters can be validated. Multiple runway parameter
                #   validation doesn't make sense since there is no way to know which CUP parameter relates which of the
                #   multiple runways
                if len(self.file_airport.runway_directions) == 1:
                    self.validate_runway_length(0)
                    self.validate_runway_width(0)
                    self.validate_runway_surface(0)
                    # Check the length/width/surface. Count errors and print results
                    self.was_error_found_for_length_width_surface_frequency()
                else:
                    print("VALIDATION HALTED: Multiple runways with no matched direction")
            # The runway direction was validated which invoked the automatic checking of length, width, surface
            elif self.flag_runway_direction_validated:
                if self.any_error_flags_set():
                    print("\n")
                    self.print_pair()
                    # Check the length/width/surface. Count errors and print results
                    self.was_error_found_for_length_width_surface_frequency()
        # No runway information was in the file, indicate that there is not error but also no validation
        else:
            self.flag_runway_direction_has_error = False
            self.flag_runway_direction_validated = False
            self.flag_runway_length_has_error = False
            self.flag_runway_length_validated = False
            self.flag_runway_width_has_error = False
            self.flag_runway_width_validated = False
            self.flag_runway_surface_has_error = False
            self.flag_runway_surface_validated = False

    def was_error_found_for_length_width_surface_frequency(self):
        if self.flag_runway_length_has_error:
            self.error_count += 1
            print("ERROR: LENGTH")
        if self.flag_runway_width_has_error:
            self.error_count += 1
            print("ERROR: WIDTH")
        if self.flag_runway_surface_has_error:
            self.error_count += 1
            print("ERROR: SURFACE")
        if self.flag_frequency_has_error:
            # Frequency error already counted
            print("ERROR: FREQUENCY")

    # Return true if any error flags were set
    def any_error_flags_set(self):
        if self.flag_runway_length_has_error:
            return True
        elif self.flag_runway_width_has_error:
            return True
        elif self.flag_runway_surface_has_error:
            return True
        elif self.flag_frequency_has_error:
            return True
        else:
            return False

    def validate_runway_length(self, runway_index):
        check1 = False
        check2 = False
        if self.cup_airport.runway_length:
            check1 = int(self.cup_airport.runway_length)
        if self.file_airport.runway_length:
            check2 = int(self.file_airport.runway_length[runway_index])
        if check1 and check2:
            # Check if the runway lengths are within an acceptable length error
            if abs(check1 - check2) <= LENGTH_ERR:
                self.flag_runway_length_validated = True
                self.flag_runway_length_has_error = False
            elif not self.flag_runway_length_validated:
                self.flag_runway_length_has_error = True

    def validate_runway_width(self, runway_index):
        self.flag_runway_width_validated = False
        self.flag_runway_width_has_error = True
        check1 = False
        check2 = False
        if self.cup_airport.runway_width:
            check1 = int(self.cup_airport.runway_width)
        if self.file_airport.runway_width:
            check2 = int(self.file_airport.runway_width[runway_index])
        if check1 and check2:
            # Check if the runway widths are within an acceptable width error
            if abs(check1 - check2) <= WIDTH_ERR:
                self.flag_runway_width_validated = True
                self.flag_runway_width_has_error = False
            elif not self.flag_runway_width_validated:
                self.flag_runway_width_has_error = True

    def validate_runway_surface(self, runway_index):
        check1 = False
        check2 = False
        if self.cup_airport.waypoint_style:
            if self.cup_airport.waypoint_style.count("Grass"):
                check1 = "Grass"
            elif self.cup_airport.waypoint_style.count("Solid"):
                check1 = "Solid"
        if self.file_airport.surface:
            # Confirm there is only mention of turf and no mention of asphalt
            if self.file_airport.surface[runway_index].count("turf") and not self.file_airport.surface[
                runway_index].count("asphalt"):
                check2 = "Grass"
            elif self.file_airport.surface[runway_index].count("asphalt") or self.file_airport.surface[
                runway_index].count("concrete"):
                check2 = "Solid"
        if check1 and check2:
            # Check if the runway surfaces are the same
            if check1 == check2:
                self.flag_runway_surface_validated = True
                self.flag_runway_surface_has_error = False
            elif not self.flag_runway_surface_validated:
                self.flag_runway_surface_has_error = True

    def validate_latitude_longitude(self):
        coord_cup = [self.cup_airport.latitude, self.cup_airport.longitude]
        coord_file = self.file_airport.coordinates
        # Confirm coordinates exist
        if coord_file != ["lat", "long"] and coord_cup:
            distance_btw_pts = geopy.distance.geodesic(coord_file, coord_cup).feet
            # Check if the distance between the CUP and file reported position differ by more than LOCATION_ERR
            if distance_btw_pts > LOCATION_ERR and not self.flag_runway_coordinates_validated:
                print("ERROR: COORDINATES AT", self.file_airport.iata, self.file_airport.coordinates,
                      self.cup_airport.latitude, self.cup_airport.longitude)
                self.error_count += 1
                self.flag_runway_coordinates_have_error = True
            elif distance_btw_pts < LOCATION_ERR:
                self.flag_runway_coordinates_have_error = False
                self.flag_runway_coordinates_validated = True


def read_cup_file(filename):
    file = open(filename)
    reader = csv.DictReader(file, fieldnames=field_names)
    list_of_dictionaries = []
    for line in reader:
        list_of_dictionaries.append(line)

    file.close()

    return list_of_dictionaries


# Use an api key to get an image of the airport
def get_airport_image(lat, long, airport_code, input_type):
    string0 = "http://maps.googleapis.com/maps/api/staticmap?center="
    string1 = "&size=2000x2000&zoom=16&markers="
    string2 = "&scale=2&key=AIzaSyCKlgfABXh7dYM3gZG3CLBcoW0nT9NaL9M&maptype=satellite"
    lat = str(lat)
    long = str(long)

    # TODO, need to update this so that when I adjust the CUP location, the image will update
    path = "./Images/" + airport_code + "_" + input_type + ".png"

    # Check if the image file exits
    if not os.path.isfile(path):
        if input_type == "cup":
            print("Getting CUP image of:", airport_code)
        elif input_type == "file":
            print("Getting File image of:", airport_code)
        else:
            return

        # Utilize google API to retrieve image
        r = requests.get(string0 + lat + "," + long + string1 + lat + "," + long + string2)

        # Make the image directory if it does not exist
        if not os.path.exists("./Images"):
            os.mkdir("./Images")

        # Write binary the png image data
        file = open(path, 'wb')
        file.write(r.content)
        file.close()


# Return the index for the airport of interest: CUP
def find_airport_from_cup(list_to_search: [AirportFromCup], lookup_value: str):
    for i in range(len(list_to_search)):
        if list_to_search[i].code == lookup_value:
            return i


# Return the index for the airport of interest: File
def find_airport_from_file(list_to_search: [AirportFromFile], lookup_airport_code: str):
    # I sometimes use "43NC (CLOSED)" or just "CLOSED" in my airport code
    if " (CLOSED)" not in lookup_airport_code:
        for i in range(len(list_to_search)):
            if list_to_search[i].iata == lookup_airport_code:
                return i
    # Format "43NC (CLOSED)"
    elif " (CLOSED)" in lookup_airport_code:
        lookup_airport_code = lookup_airport_code.split()[0]
        for i in range(len(list_to_search)):
            if list_to_search[i].iata == lookup_airport_code:
                return i
    return -1


# Unused TODO: Delete
class LineEdit:
    DictEdits = {}

    def __init__(self, edit: qtw.QLineEdit, key):
        self.edit = edit
        LineEdit.DictEdits[key] = self.edit

    def set_text(self, input_data):
        # If intput is a list
        if isinstance(input_data, list):
            # If the list is longer than 1, separate with commas
            if len(input_data) > 1:
                new_string = ""
                for i in range(len(input_data)):
                    new_string += str(input_data[i]) + ", "
                # Remove the last space and comma
                new_string = new_string[:-2]
            # Get single item from list
            elif len(input_data) == 1:
                new_string = str(input_data[0])
            else:
                new_string = ""
        else:
            new_string = str(input_data)

        # Write the output to the actual lineEdit
        self.edit.setText(new_string)


def show_apply(edit_box):
    edit_box.setStyleSheet("background-color: green")
    qtc.QTimer.singleShot(500, lambda: edit_box.setStyleSheet(""))


class UserWindow(qtw.QMainWindow, Ui_MainWindow):
    def __init__(self, data: list[AirportValidation]):
        super().__init__()
        self.setupUi(self)
        self.cb = qtw.QApplication.clipboard()
        self.data = data

        # Active index for when switching through airports
        self.active_index = 0
        # Active discrepancy index and list which holds the indices of the discrepancy aiports
        self.discrepancies_index = 0
        self.discrepancies_list = []

        # Connect button press events
        self.pushButton_next.pressed.connect(self.display_next_airport)
        self.pushButton_previous.pressed.connect(self.display_previous_airport)
        self.pushButton_discrepancies.pressed.connect(self.find_discrepancy_airport_indices)
        self.pushButton_open_cup_image.pressed.connect(lambda: self.open_image("cup"))
        self.pushButton_open_file_image.pressed.connect(lambda: self.open_image("file"))
        self.pushButton_open_cup_image.pressed.connect(lambda: self.open_image("cup"))
        self.pushButton_open_file_image.pressed.connect(lambda: self.open_image("file"))
        self.pushButton_cup_print_attributes.pressed.connect(
            lambda: self.data[self.active_index].cup_airport.print_attributes())
        self.pushButton_file_print_attributes.pressed.connect(
            lambda: self.data[self.active_index].file_airport.print_attributes())
        self.pushButton_apply.pressed.connect(self.process_apply)
        self.pushButton_write_changes.pressed.connect(self.process_write_changes)

        # Copy button actions
        self.pushButton_copy_location.pressed.connect(self.copy_location)
        self.pushButton_copy_elevation.pressed.connect(
            lambda: self.lineEdit_cup_elevation.setText(self.lineEdit_file_elevation.text()))
        self.pushButton_copy_frequency.pressed.connect(
            lambda: self.lineEdit_cup_frequency.setText(self.lineEdit_file_frequency.text()))
        self.pushButton_copy_runway.pressed.connect(
            lambda: self.lineEdit_cup_runway.setText(self.lineEdit_file_runway.text()))
        self.pushButton_copy_length.pressed.connect(
            lambda: self.lineEdit_cup_length.setText(self.lineEdit_file_length.text()))
        self.pushButton_copy_width.pressed.connect(
            lambda: self.lineEdit_cup_width.setText(self.lineEdit_file_width.text()))

        self.pushButton_lookup.pressed.connect(self.lookup_airport)
        self.pushButton_copy_coordinates.pressed.connect(self.process_copy_coordinates)

        # Populate the cup combination box with all the possible options
        self.comboBox_cup_wayport_style.addItems(AirportFromCup.style_list)

    def process_copy_coordinates(self):
        self.cb.setText(self.lineEdit_cup_latitude.text() + ", " + self.lineEdit_cup_longitude.text(),
                        mode=self.cb.Clipboard)

    def lookup_airport(self):
        lookup = self.lineEdit_lookup.text()
        for i in range(len(self.data)):
            if self.data[i].name == lookup:
                break
        self.active_index = i
        self.update_gui_data()

    def copy_location(self):
        self.lineEdit_cup_latitude.setText(self.lineEdit_file_latitude.text())
        self.lineEdit_cup_longitude.setText(self.lineEdit_file_longitude.text())

    def display_airport_faults(self):
        # Check if Location has error
        if self.data[self.active_index].flag_runway_coordinates_have_error:
            self.radioButton_location.setChecked(True)
        else:
            self.radioButton_location.setChecked(False)

        # Check if Elevation has error
        if self.data[self.active_index].flag_elevation_has_error:
            self.radioButton_elevation.setChecked(True)
        else:
            self.radioButton_elevation.setChecked(False)

        # Check if Frequency has error
        if self.data[self.active_index].flag_frequency_has_error:
            self.radioButton_frequency.setChecked(True)
        else:
            self.radioButton_frequency.setChecked(False)

        # Check if Runway Direction has error
        if self.data[self.active_index].flag_runway_direction_has_error:
            self.radioButton_direction.setChecked(True)
        else:
            self.radioButton_direction.setChecked(False)

        # Check if Runway Length has error
        if self.data[self.active_index].flag_runway_length_has_error:
            self.radioButton_length.setChecked(True)
        else:
            self.radioButton_length.setChecked(False)

        # Check if Runway Width has error
        if self.data[self.active_index].flag_runway_width_has_error:
            self.radioButton_width.setChecked(True)
        else:
            self.radioButton_width.setChecked(False)

        # Check if Runway Surface has error
        if self.data[self.active_index].flag_runway_surface_has_error:
            self.radioButton_surface.setChecked(True)
        else:
            self.radioButton_surface.setChecked(False)

    def find_discrepancy_airport_indices(self):
        # Check button text to find state indices
        button_state = self.pushButton_discrepancies.text()
        # If "Show Only Discrepancies", then All Airports are being shown, run check
        if button_state == "Show Only Discrepancies":
            self.discrepancies_list = []
            # Run check for errors TODO: I deleted the check if CUP file is missing data:
            for i in range(len(self.data)):
                if self.data[i].error_count or self.data[i].file_airport.is_file_empty:
                    # TIMC TODO add distance filter check here
                    # Check if user wants to filter discrepancy list based on proximity to a target airport
                    if self.checkBox_filter.isChecked():
                        # If there is text listed in the line edit
                        if self.lineEdit_lookup.text():
                            airport_of_interest = self.lineEdit_lookup.text()
                            for a in self.data:
                                if a.cup_airport.code == airport_of_interest:
                                    check_distance = gps_distance_check(self.data[i].cup_airport.latitude,
                                                                        self.data[i].cup_airport.longitude,
                                                                        a.cup_airport.latitude,
                                                                        a.cup_airport.longitude)
                                    # Check if the airport associated with self.data[i] is within the specified range to the AOI
                                    if check_distance < float(self.comboBox_filter_distance.currentText()):
                                        self.discrepancies_list.append(i)

                    # Append to discrepancy list if there is an error but no filter is checked
                    else:
                        self.discrepancies_list.append(i)

            # If list has length then discrepancies exist, change button text, update discrepancy variables
            if len(self.discrepancies_list):
                self.pushButton_discrepancies.setText("Show All Airports")
                self.discrepancies_index = 0
        # Elif "Show All Airports", discrepancy list is being shown. Change button text, update discrepancy variables
        elif button_state == "Show All Airports":
            self.pushButton_discrepancies.setText("Show Only Discrepancies")
            self.discrepancies_list = []
            self.discrepancies_index = 0

    def open_image(self, requestor):
        if requestor == "cup":
            path = "./Images/" + self.data[self.active_index].cup_airport.code + "_cup.png"
            if os.path.isfile(path):
                im = Image.open(path)
                im.show()
        elif requestor == "file":
            path = "./Images/" + self.data[self.active_index].file_airport.iata + "_file.png"
            if os.path.isfile(path):
                im = Image.open(path)
                im.show()

    def process_apply(self):
        if self.data[self.active_index].cup_airport.update_frequency(self.lineEdit_cup_frequency.text()):
            show_apply(self.lineEdit_cup_frequency)
        if self.data[self.active_index].cup_airport.update_elevation(self.lineEdit_cup_elevation.text()):
            show_apply(self.lineEdit_cup_elevation)
        if self.data[self.active_index].cup_airport.update_length(self.lineEdit_cup_length.text()):
            show_apply(self.lineEdit_cup_length)
        if self.data[self.active_index].cup_airport.update_width(self.lineEdit_cup_width.text()):
            show_apply(self.lineEdit_cup_width)
        if self.data[self.active_index].cup_airport.update_waypoint_style(
                self.comboBox_cup_wayport_style.currentText()):
            show_apply(self.comboBox_cup_wayport_style)
        if self.data[self.active_index].cup_airport.update_runway_direction(self.lineEdit_cup_runway.text()):
            show_apply(self.lineEdit_cup_runway)
        if self.data[self.active_index].cup_airport.update_latitude(self.lineEdit_cup_latitude.text()):
            show_apply(self.lineEdit_cup_latitude)
        if self.data[self.active_index].cup_airport.update_longitude(self.lineEdit_cup_longitude.text()):
            show_apply(self.lineEdit_cup_longitude)
        if self.data[self.active_index].cup_airport.update_waypoint_name(self.lineEdit_cup_waypoint_name.text()):
            show_apply(self.lineEdit_cup_waypoint_name)
        if self.data[self.active_index].cup_airport.update_code(self.lineEdit_cup_code.text()):
            show_apply(self.lineEdit_cup_code)

        self.data[self.active_index].run_validation()

    def process_write_changes(self):
        new_cup_file = open(OUTPUT, "w", newline='')
        writer = csv.DictWriter(new_cup_file, fieldnames=field_names, delimiter=",")

        # Transfer all the updated data to the new CSV file
        for line in self.data:
            writer.writerow(line.cup_airport.updated_cup_data)
            # If there is a GPS location change, rename the image file, so it can't be used again
            new_lat = line.cup_airport.updated_cup_data.get("Latitude")
            old_lat = line.cup_airport.original_cup_data.get("Latitude")
            new_long = line.cup_airport.updated_cup_data.get("Longitude")
            old_long = line.cup_airport.original_cup_data.get("Longitude")
            if new_lat != old_lat or new_long != old_long:
                image_path = "./Images/" + line.cup_airport.code + "_cup.png"
                if os.path.isfile(image_path):
                    print("Deleting Image for Airport:", line.cup_airport.code)
                    new_image_path = image_path.split(".png")[0] + "_" + time.strftime("%Y%m%d-%H%M%S") + ".png"
                    os.rename(image_path, new_image_path)

        # # Assume there is a r3
        # file_output = open(OUTPUT, 'r+')
        # cup_data = file_output.readlines()
        # for i in range(len(cup_data)):
        #     if self.data[self.active_index].name == cup_data[i].split(",")[1]:
        #         # Insert frequency
        #         temp = cup_data[i].split(",")
        #         temp[10] = "\"" + self.lineEdit_cup_frequency.text() + "\""
        #         newline = ""
        #         for ii in range(len(temp)):
        #             newline += temp[ii] + ","
        #
        #         newline = newline[:-1]
        #         cup_data[i] = newline
        #
        # file_output.writelines(cup_data)
        # file_output.close()

    def update_gui_data(self):
        # List the data from the CUP file
        self.lineEdit_cup_latitude.setText(str(self.data[self.active_index].cup_airport.latitude))
        self.lineEdit_cup_longitude.setText(str(self.data[self.active_index].cup_airport.longitude))
        self.lineEdit_cup_elevation.setText(self.data[self.active_index].cup_airport.elevation)
        self.lineEdit_cup_frequency.setText(self.data[self.active_index].cup_airport.airport_frequency)
        self.lineEdit_cup_runway.setText(self.data[self.active_index].cup_airport.runway_direction_standard)
        self.lineEdit_cup_length.setText(self.data[self.active_index].cup_airport.runway_length)
        self.lineEdit_cup_width.setText(self.data[self.active_index].cup_airport.runway_width)
        self.comboBox_cup_wayport_style.setCurrentText(self.data[self.active_index].cup_airport.waypoint_style)
        self.label_airport_name_cup.setText(self.data[self.active_index].cup_airport.waypoint_name)
        self.label_airport_name_cup.adjustSize()
        self.label_airport_code_cup.setText(self.data[self.active_index].cup_airport.code)
        self.label_airport_code_cup.adjustSize()
        pixmap = qtg.QPixmap('./Images/' + self.data[self.active_index].cup_airport.code + '_cup.png')
        self.cup_image.setPixmap(pixmap.scaled(400, 400))
        self.lineEdit_cup_code.setText(self.data[self.active_index].cup_airport.code)
        self.lineEdit_cup_waypoint_name.setText(self.data[self.active_index].cup_airport.waypoint_name)

        # List the data from the file
        if not self.data[self.active_index].file_airport.is_file_empty:
            self.lineEdit_file_latitude.setText(str(self.data[self.active_index].file_airport.coordinates[0]))
            self.lineEdit_file_longitude.setText(str(self.data[self.active_index].file_airport.coordinates[1]))
            self.lineEdit_file_elevation.setText(self.data[self.active_index].file_airport.elevation_ft)
            self.lineEdit_file_frequency.setText(
                str(self.data[self.active_index].file_airport.get_airport_comm_frequency()))
            # Check if there is a single runways
            if len(self.data[self.active_index].file_airport.runway_directions) == 1:
                self.lineEdit_file_runway.setText(str(self.data[self.active_index].file_airport.runway_directions[0]))
                self.lineEdit_file_length.setText(str(self.data[self.active_index].file_airport.runway_length[0]))
                self.lineEdit_file_width.setText(str(self.data[self.active_index].file_airport.runway_width[0]))
                self.label_file_surface.setText(str(self.data[self.active_index].file_airport.surface[0]))
            # List the multiple runway information separated by commas
            else:
                runway_text = ""
                length_text = ""
                width_text = ""
                surface_text = ""
                for i in range(len(self.data[self.active_index].file_airport.runway_directions)):
                    runway_text += runway_text + str(
                        self.data[self.active_index].file_airport.runway_directions[i]) + ", "
                    length_text += str(self.data[self.active_index].file_airport.runway_length[i]) + ", "
                    width_text += str(self.data[self.active_index].file_airport.runway_width[i]) + ", "
                    surface_text += str(self.data[self.active_index].file_airport.surface[i]) + ", "

                # Remove the space and last comma
                runway_text = runway_text[:-2]
                length_text = length_text[:-2]
                width_text = width_text[:-2]
                surface_text = surface_text[:-2]
                self.lineEdit_file_runway.setText(runway_text)
                self.lineEdit_file_length.setText(length_text)
                self.lineEdit_file_width.setText(width_text)
                self.label_file_surface.setText(surface_text)

            self.label_airport_name_file.setText(self.data[self.active_index].file_airport.airport_name)
            self.label_airport_name_file.adjustSize()
            self.label_airport_code_file.setText(self.data[self.active_index].file_airport.iata)
            self.label_airport_code_file.adjustSize()
            pixmap = qtg.QPixmap('./Images/' + self.data[self.active_index].file_airport.iata + '_file.png')
            self.file_image.setPixmap(pixmap.scaled(400, 400))
        else:
            self.clear_file_entries()
        # Update the fault information
        self.display_airport_faults()

    def display_next_airport(self):
        if len(self.discrepancies_list) == 0:
            self.active_index = (self.active_index + 1) % len(self.data)
        else:
            self.discrepancies_index = (self.discrepancies_index + 1) % len(self.discrepancies_list)
            self.active_index = self.discrepancies_list[self.discrepancies_index]
        self.update_gui_data()

    def display_previous_airport(self):
        if len(self.discrepancies_list) == 0:
            self.active_index = (self.active_index - 1) % len(self.data)
        else:
            self.discrepancies_index = (self.discrepancies_index - 1) % len(self.discrepancies_list)
            self.active_index = self.discrepancies_list[self.discrepancies_index]
        self.update_gui_data()

    # In the GUI sometimes the entries need to be clearead when the CUP has data but there isn't anything on the internet
    def clear_file_entries(self):
        clear_text = "N/A"
        self.lineEdit_file_latitude.setText(clear_text)
        self.lineEdit_file_longitude.setText(clear_text)
        self.lineEdit_file_elevation.setText(clear_text)
        self.lineEdit_file_frequency.setText(clear_text)
        self.lineEdit_file_runway.setText(clear_text)
        self.lineEdit_file_length.setText(clear_text)
        self.lineEdit_file_width.setText(clear_text)
        self.label_file_surface.setText(clear_text)
        self.label_airport_name_file.setText(clear_text)
        self.label_airport_name_file.adjustSize()
        self.label_airport_code_file.setText(clear_text)
        self.label_airport_code_file.adjustSize()
        self.file_image.clear()

    def apply_changes(self):
        self.statusbar.showMessage("Ready to apply changes")
        # TODO add more to this


if __name__ == '__main__':
    # Find airport files
    airport_file_list = os.listdir("./Airports")
    airports_from_file = []
    # Generate Airports from text file
    for airport in airport_file_list:
        airports_from_file.append(AirportFromFile(airport))

    # Read in cup file data
    list_data = read_cup_file(INPUT)
    airports_from_cup = []
    # Generate Airports from cup file, Note about 95%
    for item in list_data:
        airports_from_cup.append(AirportFromCup(item))

    # Combine cup airport with file airports
    airports = []
    for j in range(len(airports_from_cup)):

        # Find the matching airport data in the text files
        index_for_file = find_airport_from_file(airports_from_file, airports_from_cup[j].code)
        temp = airports_from_cup[j].code  # delete this line

        # Pair and compare two airport data sets
        airports.append(AirportValidation(airports_from_cup[j], airports_from_file[index_for_file]))

        # Get satellite image of airport
        get_airport_image(airports_from_cup[j].latitude, airports_from_cup[j].longitude, airports_from_cup[j].code,
                          "cup")
        # Only get airport images if the file is valid
        if not airports_from_file[index_for_file].is_file_empty:
            get_airport_image(airports_from_file[index_for_file].coordinates[0],
                              airports_from_file[index_for_file].coordinates[1],
                              airports_from_file[index_for_file].iata, "file")

    total_error_count = 0
    for i in range(len(airports)):
        total_error_count += airports[i].error_count

    print("Total Errors Found:", total_error_count)
    print("Total Airports Without Data", len(AirportFromFile.airports_with_no_data))

    # Open the window to View/Edit the CUP and website data
    app = qtw.QApplication(sys.argv)
    mw = UserWindow(airports)
    # Call method to populate the GUI with the first entry
    mw.update_gui_data()
    mw.show()
    app.exec_()
