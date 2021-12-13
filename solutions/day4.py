import numpy as np
from itertools import product

# would not have gotten solution without extensive help. saving for future reference 

input = 'day4'

with open(f'input_data\\{input}.txt') as f:
    draws = list(map(int, f.readline().split(","))) # readline just reads first line. make a list of integers split by commas
    boards = [np.mat(board.replace('\n', ';')) for board in f.read()[1:].split('\n\n')] # read each line after the first. replaceing new lines with ; so that np.mat can make a matrix


def part1():     
    for draw, board in product(draws, [np.ma.masked_array(board) for board in boards]): # masked array allows for all values to be set to false. and then true upon some condition.
        board.mask |= board.data == draw  # this is the condition in which we change to true
        if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5):   # find any complete rows(0) or columns(1) in which all values(5) are True
            result = board.sum()*draw   # math to calculate winning row/column * final draw value
            break

    print(result)


part1()    # needed extensive help with np.mat and np.ma.masked_array()

def part2():
    won_boards = set()  # create a set for won board indexes to be placed

    for draw, (idx, board) in product(draws, enumerate([np.ma.masked_array(board) for board in boards])): # same as part one but enumerate in order to index boards
        board.mask |= board.data == draw # same as part 1
        if np.any(board.mask.sum(0) == 5) or np.any(board.mask.sum(1) == 5): # same as part 1
            if idx not in won_boards and len(won_boards) == len(boards)-1: # check to see if the winning board index is in the won_boards set and checks to make sure you have cycled through all boards by cross referencing length
                result = board.sum()*draw  # math to calc answer
                break
            won_boards.add(idx) # add winning board index to won_boards set
    print(result)

part2()
