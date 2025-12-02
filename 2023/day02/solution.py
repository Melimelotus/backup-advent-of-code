# Day 01
"""
PUZZLE:
    As you walk, the Elf shows you a small bag and some cubes which are either
    red, green, or blue. Each time you play this game, he will hide a secret
    number of cubes of each color in the bag, and your goal is to figure out
    information about the number of cubes.

    [...] the Elf will reach into the bag, grab a handful of random cubes, show
    them to you, and then put them back in the bag. He'll do this a few times
    per game.

    You play several games and record the information from each game (your
    puzzle input). Each game is listed with its ID number followed by a
    semicolon-separated list of subsets of cubes that were revealed from the bag
    (like 3 red, 5 green, 4 blue).

    ---- PART1
    Determine which games would have been possible if the bag had been loaded
    with only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum
    of the IDs of those games?

    ---- PART2
    In each game you played, what is the fewest number of cubes of each color
    that could have been in the bag to make the game possible?

    The power of a set of cubes is equal to the numbers of red, green, and blue
    cubes multiplied together.

    For each game, find the minimum set of cubes that must have been present.
    What is the sum of the power of these sets?

"""

import os
import re

def execute():
    """TODO
    """
    colors_list=['blue', 'green', 'red']

    # Main variables for the first half of the puzzle:
    colors_max_allowed_dict={
        'blue':14,
        'green':13,
        'red':12,
    }
    allowed_games_id_list=list()
    sum_of_allowed_games_id=int()

    # Main variables for the second half of the puzzle:
    # TODO

    # Regular expressions required to parse lines
    id_regex='^Game (?P<id>[0-9]+)'
    color_amount_regex='(?P<amount>[0-9]+) (?P<color>[a-z]+)'

    # Iterate over lines
    input_file_path=build_path_to_input()
    with open(input_file_path, "r") as f:
        for line in f:
            stripped_line=line.strip()
            ''' TODO DELETE THIS LATER
            Part2:
                for each game, find max amount pulled for each color. This is
                the minimum amount of cubes of one color in a given game. Put in
                color_minimum_amount_dict
            '''

            # Split lines to prepare  for regular expressions
            '''
            Format of lines: "Game {id}: {subset}; {subset}"
            Format of subsets: "{amount} {color}, {amount} {color}, ..."
            '''
            splitted=line.split(':')
            game_id_split_line=splitted[0]
            game_subsets_split_line=splitted[1]

            # Get game id
            id_str=re.search(id_regex, game_id_split_line).group('id')
            id=int(id_str)
            print('# Game id: '+ id_str)

            # Build game data
            game_subsets_list=game_subsets_split_line.split(';')
            colors_min_dict={
                color:0
                for color in colors_list
            } # "There is at least {min_amount} {color} cubes in game {id}."
            
            for game_subset in game_subsets_list:
                # Build colors_min_dict
                print('Subset: '+game_subset)
                matches=re.finditer(color_amount_regex, game_subset)
                for match in matches:
                    color=match.group('color')
                    amount=int(match.group('amount'))
                    if colors_min_dict[color]<amount:
                        colors_min_dict[color]=amount

            # Does this game respect the prompt's max amount per color?
            game_respects_prompt=True
            for color in colors_list:
                if colors_min_dict[color]>colors_max_allowed_dict[color]:
                    game_respects_prompt=False
            if game_respects_prompt:
                allowed_games_id_list.append(id)
            
            print(colors_min_dict)
            print(game_respects_prompt)
            # ...Lines iteration (for)
        # ...Opened file context (with)
    # Build and print results
    print('#### RESULTS')
    sum_of_allowed_games_id=sum(allowed_games_id_list)
    prompt_1_result_message=[
        "# Sum of the ID of games that are possible if the bag is loaded ",
        "with only 12 red cubes, 13 green cubes, and 14 blue cubes: ",
        "{sum_of_allowed_games_id}".format(
            sum_of_allowed_games_id=sum_of_allowed_games_id),
    ]
    print(''.join(prompt_1_result_message))
    prompt_2_result_message=[] # sum of the power of each game
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