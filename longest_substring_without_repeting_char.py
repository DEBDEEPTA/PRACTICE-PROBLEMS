"""
Input: "abcabcbb"
Output: 3  # "abc"
"""

# GENERATE SUBSTRING OF SUBSIZE
def get_substring(str_val,size):
    # generate substring of a specific size
    substring_list = []
    for i in range(len(str_val)-size +1):
        substring_list.append(str_val[i: i+size])

    return substring_list


# CHECK CHARACTER REPETATION FOR EACH SUB STRING
def check_char_repetation(substring):
    seen = set()
    for ch in substring:
        if ch in seen:
            return True
        seen.add(ch)
    return False


# LONGEST NON REPETATING CHAR SUBSTRING
def longest_substr(str_val):
    for i in range(len(str_val),0,-1):
        subsize = i
        substrings = get_substring(str_val,subsize)

        for substr in substrings:
            if not check_char_repetation(substr):
                return substr

if __name__=="__main__":

    # # GENERATE SUBSTRINGS OF SPECIFIC SIZE
    # substrings = get_substring("DEBDEEPTA",3)
    # print(substrings)
    #
    #
    # # CHECK IF SUBSTRIG HAVE REPEATED CHARACTER OR NOT
    # for substr in substrings:
    #     print(check_char_repetation(substr))

    print(longest_substr("DEBDEEPTASAMUI"))