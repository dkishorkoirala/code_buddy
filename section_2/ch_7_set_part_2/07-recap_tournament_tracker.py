"""
Recap - Tournament Tracker


Challenge

In a competitive gaming tournament, players participate in different matches. Your task is to analyze player participation across three matches using Python sets.

You'll be given three sets of players:

match1: Players who participated in Match 1
match2: Players who participated in Match 2
match3: Players who participated in Match 3
Your task is to:

Find players who participated in all three matches
Identify players who participated in exactly two matches
Determine players who participated in only one match
Count the total number of unique players in the tournament
Find players who participated in Match 1 but not in Match 2 or Match 3
Print the results in the following format:

Use sorted(list(set_name)) to display players in alphabetical order
Print the exact output format shown in the example
Example Input:
{"Alice", "Bob", "Charlie", "Diana"}
{"Charlie", "Diana", "Eve", "Frank"}
{"Alice", "Diana", "Frank", "George"}
Example Output:
Players in all matches: ['Diana']
Players in exactly two matches: ['Alice', 'Charlie', 'Frank']
Players in only one match: ['Bob', 'Eve', 'George']
Total unique players: 7
Players in Match 1 only: ['Bob']

"""

# Read input for the three matches
match1 = eval(input())
match2 = eval(input())
match3 = eval(input())

# 1. Find players who participated in all three matches
all_three = match1 & match2 & match3

# 2. Find players who participated in exactly two matches
match1_2 = match1 & match2
match2_3 = match2 & match3
match1_3 = match1 & match3

exact_two = (match1_2 | match1_3 | match2_3) - all_three


# 3. Find players who participated in only one match

one_match = (
    (match1 - match2 - match3) | (match2 - match1 - match3) | (match3 - match1 - match2)
)

# 4. Count total unique players
total_uniq = match1 | match2 | match3


# 5. Find players in Match 1 only
only_on_match1 = match1 - match2 - match3

# Print results in the specified format
print(f"Players in all matches: {sorted(list(all_three))}")
print(f"Players in exactly two matches: {sorted(list(exact_two))}")
print(f"Players in only one match: {sorted(list(one_match))}")
print(f"Total unique players: {len(total_uniq)}")
print(f"Players in Match 1 only: {sorted(list(only_on_match1))}")
