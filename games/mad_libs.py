def start():
    while True:
        noun = input("Choose a noun: ")
        p_noun = input("Choose a plural noun: ")
        sec_noun = input("Choose a noun: ")
        place = input("Name a place: ")
        adjective = input("Choose an adjective (Describing word): ")
        third_noun = input("Choose a noun: ")
        print("------------------------------------------")
        print("Be kind to your "+noun+"-footed "+p_noun+"\nFor a duck may be somebody's "+sec_noun+",\nBe kind to your "+p_noun," in "+place+"\nWhere the weather is always "+adjective+".\n\nYou may think that is this the "+third_noun+",\nWell it is.")
        print("------------------------------------------")
        stop = input("Do you want to stop? (enter \"y\" for stop or any other character to play again): ")
        if stop == "y":
            break

start()