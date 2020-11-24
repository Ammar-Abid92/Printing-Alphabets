# a = 10
# for row in range(7):
#     if row == 3:
#         print(a*" ", 9 * "^")
#     print(a*" ", "^", 5*" ", "^")
# List1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V",
#          "W", "X", "Y", "Z"]
# List2 = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
#          "w", "x", "y", "z"]
# for a in range(2):
#     letter = input("Write the letter: ")
#     if (letter in List1) or (letter in List2):
#         print("Its an Alphabet 😍", letter)
#     else:
#         print("its not an alphabet 😥")
no = input("enter letter: ")
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
for i in no:
    if i in alphabets:
        print(no, "is the alphabet")
    else:
        print("its not an alphabet")
