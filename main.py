def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        wordCount = 0
        for word in words:
            wordCount += 1

        return f"{wordCount} words found in the document"
    
def countLetters():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        lower_file_contents = file_contents.lower()
        countDict = {"a" : 0, 
                    "b" : 0,
                    "c" : 0,
                    "d" : 0,
                    "e" : 0,
                    "f" : 0,
                    "g" : 0,
                    "h" : 0,
                    "i" : 0,
                    "j" : 0,
                    "k" : 0,
                    "l" : 0,
                    "m" : 0,
                    "n" : 0,
                    "o" : 0,
                    "p" : 0,
                    "q" : 0,
                    "r" : 0,
                    "s" : 0,
                    "t" : 0,
                    "y" : 0,
                    "v" : 0,
                    "w" : 0,
                    "x" : 0,
                    "y" : 0,
                    "z" : 0}
        for char in lower_file_contents:
            if char in countDict:
                countDict[char] += 1

        for key in countDict:
            print(f"The '{key}' character was found {countDict[key]} times")

wordCount = main()

print("--- Begin report of books/frankenstein.txt ---")
print(wordCount)
print("")
countLetters()
print("--- End report ---")