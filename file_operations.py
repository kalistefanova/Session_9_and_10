open("text.txt", "r") # this is open for reading
print(fp.read()) #read() method gets the entire file content
fp.close() # this is good practice, not really necessary

# same thing using a context manager!
with open("text.txt", "r") as f:
    print(f.read())
# no need to close it

# read the file line by line
print("Now we read it line by line")
with open("text.txt", "r") as f:
    for line in f: # f is iterable and we get each individual line
        # print(line, end = "")
        print(line.rstrip())

