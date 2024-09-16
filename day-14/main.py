""" main module """
import os
import random
from art import logo,vs
from game_data import data


def get_random_item():
    """get random item from data

    Returns:
        return a random item
    """
    return random.choice(data)

def print_contest(first, curr_score):
    """print the game 

    Args:
        first (dict): first item
        curr_score (int): current score

    Returns:
        _type_: _description_
    """
    os.system('clear')
    random_first=first
    random_b=get_random_item()
    while random_first == random_b:
        random_b=get_random_item()
    # print(f"A:{random_first['follower_count']}")
    # print(f"B:{random_b['follower_count']}")
    print(logo)
    if curr_score>0:
        print(f"Your score is: {curr_score}")
    compare_a=f"Compare A: {random_first["name"]}, a {random_first['description']}, from {random_first['country']}"
    compare_b=f"Compare B: {random_b["name"]}, a {random_b['description']}, from {random_b['country']}"

    print(compare_a)
    print(vs)
    print(compare_b)


    choice= input("Who has more follower_count? Type 'A' or 'B': ").lower()
    return analyse_result(choice,curr_score,random_a,random_b)

def analyse_result(choice,prev_score,random_first,random_b):
    """analyse game result

    Args:
        choice (str): user choice
        prev_score (int): previous score
        random_first (dict): first random item
        random_b (dict): second random item

    Returns:
        tuple: more follower dict, new score
    """
    new_score=prev_score+1
    if choice=="a" and random_first['follower_count']>=random_b['follower_count']:
        return random_first,new_score
    if choice=="b" and random_b['follower_count']>random_first['follower_count']:
        return random_b,new_score
    return None, prev_score

SCORE=0
random_a=get_random_item()
CONTINUE_PLAYING=True

while CONTINUE_PLAYING:
    random_a,SCORE=print_contest(random_a,SCORE)
    if random_a is None:
        CONTINUE_PLAYING=False
        print(f"You lose, Your final score is: {SCORE}")
