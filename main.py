# Japanese Learning Tool made by Wings Purple
# Answers are not case sensitive
# Will extend to kanji in the future

import List
import random
# list[0] is the hiragana/katana
# list[1] is the romaji
def japanese_to_romaji(shuffled_list):
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

# list[0] is the hiragana/katana
# list[1] is the romaji
def romaji_to_japanese(shuffled_list):
    count = 0
    for letter in shuffled_list:
        print(letter[1], "Write the appropriate character on paper.")
        # halt until user is ready
        input()
        # show answer
        print(letter[0])
        answer = input("If you got it right type Y: ")
        if answer.casefold() == "y":
            count += 1
    print(count, "/", len(shuffled_list))

# list[0] is the kanji
# list[1] is the hiragana/katakana
# list[2] is the romaji
def kanji_to_romaji(shuffled_list):
    count = 0
    flag = False
    for letter in shuffled_list:
        print(letter[0])
        answer = input("Type 'Hint' to show the Hiragana/Katakana: ")
        if answer.casefold() == "hint":
            print(letter[1])
            flag = True
        if answer.casefold() == letter[2].casefold():
            if flag:
                count += 0.5
            else:
                count += 1
            print("Correct")
        else:
            print("Incorrect. Correct Answer: ", letter[2])
    print(count, "/", len(shuffled_list))

    # list[0] is the kanji
    # list[1] is the hiragana/katakana
    # list[2] is the romaji
def kanji_to_japanese(shuffled_list):
    count = 0
    flag = False
    for letter in shuffled_list:
        print(letter[0])
        answer = input("Type 'Hint' to show the romaji: ")
        if answer.casefold() == "hint":
            print(letter[2])
            flag = True
        if answer.casefold() == letter[1].casefold():
            if flag:
                count += 0.5
            else:
                count += 1
            print("Correct")
        else:
            print("Incorrect. Correct Answer: ", letter[1])
    print(count, "/", len(shuffled_list))

# list[0] is the kanji
# list[1] is the hiragana/katakana
# list[2] is the romaji
def romaji_to_kanji(shuffled_list):
    count = 0
    for letter in shuffled_list:
        print(letter[2], "Write the appropriate character on paper.")
        # halt until user is ready
        input()
        # show answer
        print(letter[0])
        answer = input("If you got it right type Y: ")
        if answer.casefold() == "y":
            count += 1
    print(count, "/", len(shuffled_list))

# list[0] is the kanji
# list[1] is the hiragana/katakana
# list[2] is the romaji
def japanese_to_kanji(shuffled_list):
    count = 0
    for letter in shuffled_list:
        print(letter[1], "Write the appropriate character on paper.")
        # halt until user is ready
        answer = input()
        # show answer
        print(letter[0])
        answer = input("If you got it right type Y: ")
        if answer.casefold() == "y":
            count += 1
    print(count, "/", len(shuffled_list))

# main function equivalent
loop = True
shuffled = []
while loop:
    choice1 = input("From Hiragana, Katakana, Both, Romaji, Kanji, or Stop: ")
    if choice1.casefold() == "stop":
        break
    choice2 = input("To Hiragana, Katakana, Romaji, Both, Kanji: ")
    if choice1 == "kanji" or choice2 == "kanji" or choice1 == "both" or choice2 == "both":
        choice3 = input("Pick a set: Vowels, B, D, G, H, K, M, N, P, R, S, T, W, Y, Z, All: ")
    if choice1.casefold() == "hiragana" or (choice1.casefold() == "romaji" and choice2.casefold() == "hiragana"):
        match choice3.casefold():
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
            match choice2.casefold():
                case "romaji":
                    japanese_to_romaji(shuffled)
                case "hiragana":
                    romaji_to_japanese(shuffled)
                case _:
                    print("Invalid Input. Try Again.")
    elif choice1.casefold() == "katakana" or (choice1.casefold() == "romaji" and choice2.casefold() == "katakana"):
        match choice3.casefold():
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
            match choice2.casefold():
                case "romaji":
                    japanese_to_romaji(shuffled)
                case "katakana":
                    romaji_to_japanese(shuffled)
                case _:
                    print("Invalid Input. Try Again.")
    elif (choice1.casefold() == "both" and choice2.casefold() == "romaji") or (choice2.casefold() == "both" and choice1.casefold() == "romaji"):
        shuffled = random.sample(List.Japanese_All, len(List.Japanese_All))
        if len(shuffled) != 0:
            match choice2.casefold():
                case "romaji":
                    japanese_to_romaji(shuffled)
                case "all":
                    romaji_to_japanese(shuffled)
                case _:
                    print("Invalid Input. Try Again.")
    else:
        print("Invalid Input. Try Again.")

