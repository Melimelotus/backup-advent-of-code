# Day 01
"""
PUZZLE:
    The newly-improved calibration document consists of lines of text; each line
    originally contained a specific calibration value [...]. On each line, the
    calibration value can be found by combining the first digit and the last
    digit (in that order) to form a single two-digit number.
    Some of the digits are actually spelled out with letters: one, two, three,
    four, five, six, seven, eight, and nine also count as valid "digits".
    What is the sum of all of the calibration values?
"""

import os
import re

def execute():
    """Iterate over each line of the file to find the first and last digits,
    combine them to form the calibration value, then add all calibration values
    together to get the result.
    """
    result=int()
    spelling_value_dict={
        'one':'1',
        'two':'2',
        'three':'3',
        'four':'4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    # Build regular expressions
    '''Instead of using re.findall() to build a list of matches and pick the
    first and last digit from there, the function uses re.search(), which
    returns only the first match. Each line is read twice: once as it is, then a
    second time reversed.'''
    regex='{spelling_alternates}|[1-9]'.format(
        spelling_alternates='|'.join(spelling_value_dict.keys())
    )

    reversed_spellings_list=[
        spelling[::-1]
        for spelling in spelling_value_dict.keys()
    ]
    reversed_regex='{reversed_spelling_alternates}|[1-9]'.format(
        reversed_spelling_alternates='|'.join(reversed_spellings_list)
    )

    # Iterate over lines to build the calibration values
    input_file_path=build_path_to_input()
    calibration_values_list=list()

    with open(input_file_path, "r") as f:
        for line in f:
            first_digit=str()
            second_digit=str()
            calibration_value=int()

            stripped_line=line.strip()

            # Search for first digit
            match=re.search(regex, stripped_line).group()
            if match in spelling_value_dict.keys():
                first_digit=spelling_value_dict[match]
            else:
                first_digit=match
            
            # Search for second digit
            reversed_line=stripped_line[::-1]
            match=re.search(reversed_regex, reversed_line).group()
            if match in reversed_spellings_list:
                second_digit=spelling_value_dict[match[::-1]]
            else:
                second_digit=match
            
            # Build calibration value and append
            calibration_value=int(first_digit+second_digit)
            calibration_values_list.append(calibration_value)
            #
        #
    # Build result
    result=sum(calibration_values_list)
    print("# execute(): result={result}".format(result=result))
    return result

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