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

import os

def execute(): # TODO WIP
    """For each line, seek numbers and build a dictionary of their coordinates.
    Then, find the coordinates of all symbols and gears. Compare to the numbers
    coordinates dictionary of the previous, current and next line to determine
    how many numbers they are adjacent to.
    """
    max_index=0 # Number of lines in the file
    numbers_coords_dict=dict() # Line number:(value,[coord min:coord max])
    symbols_coords_dict=dict() # Line number: coord
    gears_coords_dict=dict() # Line number: coord

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
            # TODO
            # Update symbols_coords_dict
            # TODO
            # Update gears_coords_dict
            # TODO
            max_index+=1
            pass

    # Analyze contents of dictionaries
    '''
    index=0
    for current_line_index in len(any dictionary):
        # Fetch numbers coordinates for the prev, current, next lines
        previous_line_index=index-1 (if not index==0)
        net_line_index=index+1 (if not index==len(any dictionary))
        ...

    for symbol_line_index in symbols_coords_dict:
        # Fetch numbers coordinates for the prev, current, next lines
        has_previous_line=False
        has_next_line=False

        if not symbol_line_index==0
            previous_line_index=symbol_line_index-1
            has_previous_line=True
            ...
        if not symbol_line_index==max_index:
            net_line_index=symbol_line_index+1
            has_next_line=True
            ...

        if symbol_line_index in numbers_coords_dict:
            # There are numbers on the symbol's line
            current_line_numbers_coords=numbers_coords_dict[symbol_line_index]
            ...

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