"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# TODO: Fix this!

"""
Rewrite the following program using the most efficient if, elif, else structure you can.
The intention is that the score must be between 0 and 100 inclusive; 90 or more is excellent; 50 or more is a pass; below 50 is bad.
Be very careful of your boundary conditions... and test systematically.

score = float(input("Enter score: "))
if score < 0:
    print("Invalid score")
else:
    if score > 100:
        print("Invalid score")
    if score > 50:
        print("Passable")
    if score > 90:
    print("Excellent")
if score < 50:
    print("Bad")
"""

score = float(input("Enter score: "))
if 0 <= score <= 100:
    if score >= 90:
        print("Excellent!")
    elif score >= 50:
        print('Well you know what they say: "Ps get degrees". You passed.')
    else:
        print("Bad. Go watch the lecture recordings.")
else:
    print("Invalid score")


