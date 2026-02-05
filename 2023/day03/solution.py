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

from itertools import pairwise
import os
import re

def execute(): # TODO day 2
    """TODO
    """

    part_numbers_sum=int() # Result of part 1
    ratio_list=list() # Result of part 2
    symbols_list=['=','+','-','*','%','#','&','@','/','$']
    line_length=140

    # Iterate over all the lines
    input_file_path=build_path_to_input()

    with open(input_file_path, "r") as f:
        # Iterate all over the lines in pairs and analyze the numbers on current
        previous_line=None
        for current_raw, next_raw in pairwise(f):
            current_line=current_raw.strip()
            next_line=next_raw.strip()

            # Get all numbers in current line and their coordinates
            numbers_matches=re.finditer('\d+', current_line)

            for match in numbers_matches:
                # Build a list of all adjacent characters
                min_adjacent_index=match.start(0)-1 if match.start(0)>0 else 0
                max_adjacent_index=match.end(0)+1 if match.end(0)<=line_length else line_length

                adjacent_chars=str()
                if previous_line:
                    adjacent_chars=previous_line[min_adjacent_index:max_adjacent_index]
                
                adjacent_chars+=current_line[min_adjacent_index:max_adjacent_index]
                adjacent_chars+=next_line[min_adjacent_index:max_adjacent_index]

                # Append to part_numbers_list if there is an adjacent symbol
                for char in adjacent_chars:
                    if char in symbols_list:
                        part_numbers_sum+=int(match.group(0))
                        break

            # Prepare next iteration
            previous_line=current_line

        # Analyze last line
        current_line=next_line

        numbers_matches=re.finditer('\d+', current_line)
        for match in numbers_matches:
            # Build a list of all adjacent characters
            min_adjacent_index=match.start(0)-1 if match.start(0)>0 else 0
            max_adjacent_index=match.end(0)+1 if match.end(0)<line_length else line_length

            adjacent_chars=str()
            adjacent_chars=previous_line[min_adjacent_index:max_adjacent_index]
            adjacent_chars+=current_line[min_adjacent_index:max_adjacent_index]

            # Append to part_numbers_list if there is an adjacent symbol
            for char in adjacent_chars:
                if char in symbols_list:
                    part_numbers_sum+=int(match.group(0))
                    break

    # Results
    print(part_numbers_sum)
    result_2=sum(ratio_list) # TODO
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