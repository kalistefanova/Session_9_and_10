with open("story.txt", "a") as f: # w for writing, a for adding new lines to the already written text
    while True:
        text = input("What do you want to write (press q to exit)")
        if text == "q":
            break
        f.write(text+"\n")
