#import random module

import random

Subjects = [
    "Salman khan",
    "Ms dhoni",
    "Virat kohli",
    "Prime minister modi",
    "Rahul gandhi",
    "Ashish chanchlani",
    "Elon musk",
]

#funny actions 

Actions = [
    "to launch a rocket",
    "forgot toss again",
    "decided to playing after retirement",
    "sitting on a buffalo and roaming around the village",
    "decided to leave politics",
    "decided to leave youtube content",
    "like a thief",
]

Place_things = [
    "in mumbai local train",
    "a plote of samosa",
    "inside parliament",
    "at ganga ghat",
    "during ipl match",
    "during voting day",
    "at india gate",
]



while True:

    subjects = random.choice(Subjects)
    actions = random.choice(Actions)
    place_things = random.choice(Place_things)

    headline = f"BREAKING NEWS: {subjects} {actions} {place_things}"

    print("\n"+headline)

    user_input = input("\nDo you want another headline? (yes/no)").strip().lower()

    if user_input == "no":
        break

    #print a goodby message 

print("Thanks for using fake headline generator, this is only for fun")
