"""
Name: Devon Lee

Course: CS1430, Section 00,  Fall 2021

Assignment: Assignment 4

Purpose: Provide statistics about delivery routes to make the fleet more aware
         of how efficient each driver's choices are.
         
Description: This program takes in location data for deliveries on a fleet of
         FedEx trucks and calculates statistics about the delivery routes.
         These statistics are reported so that the efficiency of each route
         can be easily accessed.

Input:   Number of deliveries in a route followed by the location of each in
         Cartesian coordinates, each on a new line. This cycle repeats for each
         delivery in the system.

Output:  An echo of the input, statistics for each route, and statistics about
         the entire set of routes.
"""


"""
CONSTANTS
"""
ADENINE_MASS = 135.128
THYMINE_MASS = 125.107
GUANINE_MASS = 151.128
CYTOSINE_MASS = 111.103
JUNK_MASS = 100.000

MIN_NUM_CODONS = 5
MIN_PERCENTAGE_CG = 30
NUM_UNIQUE_NUCLEOTIDES = 4
NUCLEOTIDES_PER_CODON = 3


def get_file_names():
    
    input_file_name = input("Input file name? ")
    output_file_name = input("Output file name? ")

    input_file = open(input_file_name, 'r')
    output_file = open(output_file_name, 'w')
    
    return input_file, output_file


def search_for_start(input_file):
    for line in input_file:
        for ch in line:
            x = 5

    
    
    


#  Start: ATG
#  Stop: TAA, TAG, or TGA

def main():
    files = get_file_names()
    search_for_start(files[0])
    
    


    
if __name__ == "__main__":
    main()
    