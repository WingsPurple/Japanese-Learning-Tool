import List
import random
def test(shuffled_list):
    count = 0
    for letter in shuffled_list:
        print(letter[0])
        answer = input()
        if answer.casefold() == letter[1].casefold():
            count += 1
            print("Correct")
        else:
            print("Incorrect. Correct Answer: ", letter[1])
    print(count, "/", len(shuffled_list))

loop = True
shuffled = []
while loop:
    choice1 = input("Hiragana, Katakana, All, or Stop: ")
    choice2 = input("Pick a set: Vowels, B, D, G, H, K, M, N, P, R, S, T, W, Y, Z, All: ")
    if choice1.casefold() == "hiragana":
        match choice2.casefold():
            case "b":
                shuffled = random.sample(List.Japanese_Hiragana_B, len(List.Japanese_Hiragana_B))
            case "d":
                shuffled = random.sample(List.Japanese_Hiragana_D, len(List.Japanese_Hiragana_D))
            case "g":
                shuffled = random.sample(List.Japanese_Hiragana_G, len(List.Japanese_Hiragana_G))
            case "h":
                shuffled = random.sample(List.Japanese_Hiragana_H, len(List.Japanese_Hiragana_H))
            case "k":
                shuffled = random.sample(List.Japanese_Hiragana_K, len(List.Japanese_Hiragana_K))
            case "m":
                shuffled = random.sample(List.Japanese_Hiragana_M, len(List.Japanese_Hiragana_M))
            case "n":
                shuffled = random.sample(List.Japanese_Hiragana_N, len(List.Japanese_Hiragana_N))
            case "p":
                shuffled = random.sample(List.Japanese_Hiragana_P, len(List.Japanese_Hiragana_P))
            case "r":
                shuffled = random.sample(List.Japanese_Hiragana_R, len(List.Japanese_Hiragana_R))
            case "s":
                shuffled = random.sample(List.Japanese_Hiragana_S, len(List.Japanese_Hiragana_S))
            case "t":
                shuffled = random.sample(List.Japanese_Hiragana_T, len(List.Japanese_Hiragana_T))
            case "w":
                shuffled = random.sample(List.Japanese_Hiragana_W, len(List.Japanese_Hiragana_W))
            case "y":
                shuffled = random.sample(List.Japanese_Hiragana_Y, len(List.Japanese_Hiragana_Y))
            case "z":
                shuffled = random.sample(List.Japanese_Hiragana_Z, len(List.Japanese_Hiragana_Z))
            case "all":
                shuffled = random.sample(List.Japanese_Hiragana_All, len(List.Japanese_Hiragana_All))
            case _:
                print("Invalid Input. Try Again.")
        if len(shuffled) != 0:
            test(shuffled)
    elif choice1.casefold() == "katakana":
        match choice2.casefold():
            case "b":
                shuffled = random.sample(List.Japanese_Katakana_B, len(List.Japanese_Katakana_B))
            case "d":
                shuffled = random.sample(List.Japanese_Katakana_D, len(List.Japanese_Katakana_D))
            case "g":
                shuffled = random.sample(List.Japanese_Katakana_G, len(List.Japanese_Katakana_G))
            case "h":
                shuffled = random.sample(List.Japanese_Katakana_H, len(List.Japanese_Katakana_H))
            case "k":
                shuffled = random.sample(List.Japanese_Katakana_K, len(List.Japanese_Katakana_K))
            case "m":
                shuffled = random.sample(List.Japanese_Katakana_M, len(List.Japanese_Katakana_M))
            case "n":
                shuffled = random.sample(List.Japanese_Katakana_N, len(List.Japanese_Katakana_N))
            case "p":
                shuffled = random.sample(List.Japanese_Katakana_P, len(List.Japanese_Katakana_P))
            case "r":
                shuffled = random.sample(List.Japanese_Katakana_R, len(List.Japanese_Katakana_R))
            case "s":
                shuffled = random.sample(List.Japanese_Katakana_S, len(List.Japanese_Katakana_S))
            case "t":
                shuffled = random.sample(List.Japanese_Katakana_T, len(List.Japanese_Katakana_T))
            case "w":
                shuffled = random.sample(List.Japanese_Katakana_W, len(List.Japanese_Katakana_W))
            case "y":
                shuffled = random.sample(List.Japanese_Katakana_Y, len(List.Japanese_Katakana_Y))
            case "z":
                shuffled = random.sample(List.Japanese_Katakana_Z, len(List.Japanese_Katakana_Z))
            case "all":
                shuffled = random.sample(List.Japanese_Katakana_All, len(List.Japanese_Katakana_All))
            case _:
                print("Invalid Input. Try Again.")
        if len(shuffled) != 0:
            test(shuffled)
    elif choice1.casefold() == "all":
        shuffled = random.sample(List.Japanese_All, len(List.Japanese_All))
        if len(shuffled) != 0:
            test(shuffled)
    elif choice1.casefold() == "stop":
        loop = False
    else:
        print("Invalid Input. Try Again.")

