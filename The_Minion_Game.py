def minion_game(string):
    kevin = 0
    stuart = 0

    for i in range(len(string)):
        if string[i] in "AEIOU":
            kevin += len(string) - i
        else:
            stuart += len(string) - i

    if kevin > stuart:
        print("Kevin",kevin)
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart",stuart)

if __name__ == '__main__':
    s = input()
    minion_game(s)
    
    
    # Caner Dabakoglu
    # GitHub: https://github.com/cdabakoglu
