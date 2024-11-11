with open("sample.txt", "r") as file:
    text = file.read()
    word_count = len(text.split())
    print("Word Count:", word_count)
