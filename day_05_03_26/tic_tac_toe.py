"""
    3X3 MATRIX BOARD
    00 01 02
    10 11 12
    20 21 22

    WINING TEST CASES
    -> r = c
    -> r+c = (n-1) for NxN Board
    -> row number should be same for all 3 inputs
    -> col numbers should be same for all 3 inputs
"""
import random
from enum import Enum

class TurnType(Enum):
    USER = 1
    CPU = 0

class State:
    def __init__(self, r,c):
        self.r = r
        self.c = c

    def __repr__(self):              # DUNDER repr is simillar to toString of Java
        return f"{self.r},{self.c}"  # WE can define the string represntation of the object class


def matrix_board():
    """ GENERATES 3x3 MATRIX"""


    """
        bug_fix_1
        previous approach
            ->  matrix_inner = [ 0 for _ in range(3)]
            ->  matrix_b = [ matrix_inner for _ in range(3)]
                print(matrix_b)
            -> this will create shallow copy (ie., all rows refers to the same list
    """

    matrix_b = [[0 for _ in range(3)] for _ in range(3)]  #Deep Copy

    return matrix_b


def check_win(state_list):
    # CHECK IF TOTAL 3 STATES ARE THERE OR NOT IF NOT NO WIN
    if  (len(state_list) < 3):
        return False

    # LOOP TO CHECK r=c                         (DIAGONAL)
    for state in state_list:
        row = state.r
        col = state.c
        if not (row == col):
            return True

    # LOOP TO CHECK r+c = (n-1) for NxN Board   (ANTI-DIAGONAL)
    for state in state_list:
        row = state.r
        col = state.c
        if not (row + col == (3 - 1)):
            return False

    # -> row number should be same for all 3 inputs
    # Check col numbers should be same for all 3 inputs
    row_list = [s.r for s in state_list]
    clo_list = [s.c for s in state_list]
    if (len(set(row_list)) == 1):
            return True
    if (len(set(clo_list)) == 1):
            return True

    return True

if __name__ == "__main__":

    board= matrix_board() # OBTAING 3x3 MATRIX BOARD
    user_state_list = []
    cpu_state_list = []
    current_turn = TurnType.USER.name  # SETING INITIAL TURN
    count = 6
    while True:

        if (count == 0):
            print("Tie!")
            break
        if(current_turn == TurnType.USER.name):

            cell_val = input("Choose cell in (r,c) format -> ").split(",")
            row_num = int(cell_val[0]) - 1
            co_num = int(cell_val[1]) - 1

            # CHECK CELL AVAILABILITY
            if(board[row_num][co_num] == 0):
            # SET USER COORDINATES
                print(f"Cell Marked by user -> {row_num+1},{co_num+1}")
                board[row_num][co_num] = 1
                user_state = State(row_num,co_num)
                user_state_list.append(user_state)
                # SWITCHING TURN
                current_turn = TurnType.CPU.name
                count -= 1

            elif not (board[row_num][co_num] == 0):
                print("Cell already occupied")
                continue

            if(check_win(user_state_list)):
                print("you Won !")
                break

        if(current_turn == TurnType.CPU.name):
            # GENERATE RANDOM QARDINATES FROM CPU
            # CHECK IF QARDINATE IS ALREADY FILLED OR NOT
            # IF FILLED GENERATE RANDOM QUARDINATES TILL YOU FIND A QUARDINATE THAT IS NOT FILLED
            # MARk QUARDINATE ON THE BOARD AS 1(OCCUPIED/TRUE)
            # ADD QUARDINATE TO CPU STATE LIST
            # SWITCH TURN
            # PASS STATE TO WIN FINCTION

            cpu_row_num = random.randint(0,2)
            cpu_col_num = random.randint(0,2)

            while (board[cpu_row_num][cpu_col_num] == 1):
                cpu_row_num = random.randint(0,2)
                cpu_col_num = random.randint(0,2)

            print(f"cell marked by CPU -> {cpu_row_num+1},{cpu_col_num+1}")
            board[cpu_row_num][cpu_col_num] = 1 # MARKING QUARANTINES ON BOARD
            cpu_state = State(cpu_row_num,cpu_col_num)
            cpu_state_list.append(cpu_state)
            #SWITCHING TURN
            current_turn = TurnType.USER.name
            count -= 1

            if (check_win(cpu_state_list)):
                print("CPU Won !")
                break




