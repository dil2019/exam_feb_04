def find_substring(text, substring):
    if substring.lower() in text.lower():
        print("The subtring exists in the string.")
    else:
        print("The substring doesn't exist in the string.")


text1 = input("Enter the string: ")
text2 = input("Input the substring to search: ")

find_substring(text1, text2)