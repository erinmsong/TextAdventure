def verse():
    print("There was a farmer had a dog,")
    print("and Bingo was his name-o.")
    
verse()
print("B-I-N-G-O")
print("and Bingo was his name-o.\n")

count = 0

for i in range(1,6):
    verse()

    count = count + 1
    for i in range(0, count):
        print("(clap)")
    
    print("and Bingo was his name-o.\n")
    

