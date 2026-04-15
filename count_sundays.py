"""
Description
Jack loves Sundays and wants to count how many Sundays will occur within a given number of days from the start of the month, based on the starting day of the week.
====================================================================================================
Input Format
The first line contains a string indicating the start day of the month (e.g., 'mon' for Monday).
The second line contains an integer n, representing the number of days from the start of the month.
====================================================================================================
Output Format
Print the number of Sundays within the given number of days.
====================================================================================================
Explanation:
The month start with mon(Monday). So the upcoming sunday will arrive in next 6 days. And then next Sunday in next 7 days and so on.
Now total number of days are 13. It means 6 days to first sunday and then remaining 7 days will end up in another sunday. Total 2 sundays may fall within 13 days.

Sample Case 1
Input: mon 13       Output: 1
===============================
Sample Case 2
Input: wed 10       Output: 1
===============================
Constraints
1 <= n <= 31
"""

def solve(input_data):
    day_name, days = input_data.strip().split()
    days = int(days)

    valid_day_nums = {
        'sun': 0,
        'mon': 1,
        'tue': 2,
        'wed': 3,
        'thu': 4,
        'fri': 5,
        'sat': 6
    }

    current_day = valid_day_nums[day_name]
    offset = (7 - current_day) % 7   # days until next Sunday

    if offset >= days:
        print(0)
    else:
        sundays = 1 + (days - offset - 1) // 7
        print(sundays)

if __name__=="__main__":
    data = input()
    solve(data)
