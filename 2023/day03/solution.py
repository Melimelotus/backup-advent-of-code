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

def execute():
    """Find all occurrences of numbers and asterisks on each line; then analyze
    the neighbourhood of each match to determine if they are a part number or a
    gear.
    """
    symbols_list=['=','+','-','*','%','#','&','@','/','$']
    part_numbers_sum=int() # Result of part 1
    gear_ratios_sum=int() # Result of part 2

    # Iterate over all the lines with a previous-current-next lines triplet ----
    input_file_path=build_path_to_input()
    with open(input_file_path, "r") as f:
        previous_line=None
        for current_raw, next_raw in pairwise(f):
            # Clean lines
            current_line=current_raw.strip()
            next_line=next_raw.strip()

            # Find all occurrences of numbers (first half of the puzzle)
            numbers_matches=re.finditer('\d+', current_line)
            for match in numbers_matches:
                # Search for symbols adjacent to the number
                adjacent_chars_list=list_adjacent_chars(
                    match,
                    match_line=current_line,
                    previous_line=previous_line,
                    next_line=next_line
                )

                # Add the number to part_numbers_sum if there is a symbol
                adjacent_chars=''.join(chars for chars in adjacent_chars_list)
                for char in adjacent_chars:
                    if char in symbols_list:
                        part_numbers_sum+=int(match.group(0))
                        break

            # Find all occurrences of asterisks (second half of the puzzle)
            asterisks_matches=re.finditer('\*+', current_line)
            # TODO

            # Prepare next iteration
            previous_line=current_line

        # Study last line ------------------------------------------------------
        current_line=next_line

        # Find all occurrences of numbers (first half of the puzzle)
        numbers_matches=re.finditer('\d+', current_line)
        for match in numbers_matches:
            # Search for symbols adjacent to the number
            adjacent_chars_list=list_adjacent_chars(
                match,
                match_line=current_line,
                previous_line=previous_line,
                next_line=None
            )

            # Add the number to part_numbers_sum if there is a symbol
            adjacent_chars=''.join(chars for chars in adjacent_chars_list)
            for char in adjacent_chars:
                if char in symbols_list:
                    part_numbers_sum+=int(match.group(0))
                    break

    # Results ------------------------------------------------------------------
    print(part_numbers_sum)
    print(gear_ratios_sum)
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

def list_adjacent_chars(match, match_line, previous_line=None, next_line=None, line_length=140):
    """Build a list of the characters adjacent to the given match object.

        The characters are grouped by line. This function assumes that all lines
        are of the same length.

        Returns:
            - adjacent_chars_list: list of str.
            ['previous_line_chars', 'current_line_chars', 'next_line_chars']
    """
    # Build min_index and max_index
    min_index=match.start(0)-1 if match.start(0)>0 else 0
    max_index=match.end(0)+1 if match.end(0)<line_length else line_length

    # For each line, fetch characters from min_index to max_index
    previous_line_chars=str()
    current_line_chars=str()
    next_line_chars=str()

    if previous_line:
        previous_line_chars=previous_line[min_index:max_index]
    if next_line:
        next_line_chars=next_line[min_index:max_index]
    current_line_chars=match_line[min_index]+match_line[max_index-1]
    
    adjacent_chars_list=[
        previous_line_chars,
        current_line_chars,
        next_line_chars
    ]

    return adjacent_chars_list

execute()
#