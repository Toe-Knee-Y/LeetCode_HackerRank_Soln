from typing import *
from random import *

# read through the csv
# take in the list of participants and afterwards we construct secret santa

f = open("./input.csv", "r")

info = f.readlines()[1:]
shuffle(info)
'''
turner_it_around@hotmail.com -> spatel76@gmail.com   alex -> sahana
spatel76@gmail.com -> ahmed@live.ca    sahana -> ahmed
ahmed@live.ca -> turner_it_around@hotmail.com  ahmed -> alex 
'''


# alex -> sahana -> ahmed
class Node:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def clean_up(participants):

    for i in range(len(participants)):
        participants[i] = participants[i].strip().split(',')[-1]

def construct_list(participants):
    """

    :param participants: list of secret santa participants
    :return: the "head" of the node
    """
    result = ""
    first_participant = participants[0]

    for i in range(len(participants) - 1):
        result += f"{participants[i]} -> {participants[i+1]} \n"

    result += f"{participants[-1]} -> {first_participant}"

    return result


clean_up(info)
print(info)
print(construct_list(info))