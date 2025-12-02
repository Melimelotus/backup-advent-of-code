# Day 03
"""
PUZZLE:
    The engineer explains that an engine part seems to be missing from the
    engine, but nobody can figure out which one. If you can add up all the part
    numbers in the engine schematic, it should be easy to work out which part is
    missing.

    The engine schematic (your puzzle input) consists of a visual representation
    of the engine. There are lots of numbers and symbols you don't really
    understand, but apparently any number adjacent to a symbol, even diagonally,
    is a "part number" and should be included in your sum. Periods (.) do not
    count as a symbol.

    What is the sum of all of the part numbers in the engine schematic?

    A gear is any * symbol that is adjacent to exactly two part numbers.
    Its gear ratio is the result of multiplying those two numbers together.

    What is the sum of all of the gear ratios in your engine schematic?
"""

from collections import OrderedDict
import os

def execute(): # TODO WIP
    """For each line, seek numbers and build a dictionary of their coordinates.
    Then, find the coordinates of all symbols and gears. Compare to the numbers
    coordinates dictionary of the previous, current and next line to determine
    how many numbers they are adjacent to.
    """
    numbers_coords_dict=OrderedDict() # Line number:(value,[coord min:coord max])
    symbols_coords_dict=OrderedDict() # Line number: coord
    gears_coords_dict=OrderedDict() # Line number: coord

    part_numbers_list=list() # Result of part 1
    ratio_list=list() # Result of part 2

    # Regular expressions to isolate numbers, symbols, asterisks
    symbols_list=list()
    # TODO

    # Iterate over all the lines once to build dictionaries
    input_file_path=build_path_to_input()
    with open(input_file_path, "r") as f:
        for line in f:
            '''Probs use regex to isolate numbers, symbols, asterisks and get
            their coords'''
            # Update numbers_coords_dict
            # Update symbols_coords_dict
            # Update gears_coords_dict
            pass

    # Analyze contents of dictionaries
    '''
    index=0
    for current_line in len(any dictionary):
        previous_line=index-1 (if not index==0)
        net_line=index+1 (if not index==len(any dictionary))
        for symbol in symbols_coords_dict:
            compare coords to coords of numbers in previous, current and next line.
            Are there adjacent numbers? If yes, add the value of this number to
            part_numbers_list
        for gear in gears_coords_dict:
            compare coords to coords of numbers in previous, current and next line.
            Are there exactly two adjacent numbers? If yes, ratio, then add the
            value to ratio_list
    '''
    # TODO

    # Results
    # TODO
    return

def build_path_to_input():
    """Build and return the path to the input file."""
    input_file_name='input.txt'
    current_dir_path=os.path.dirname(__file__)
    input_file_path='{path}/{name}'.format(
        path=current_dir_path,
        name=input_file_name
    )
    return input_file_path

execute()
#