answer = input("What is your age? ")

if int(answer) >= 18:
    answer = input("What country do you live in? ")
    if answer == "canada":
        print("Me as well!")
    else:
        print("Oh, I do not live there.")

