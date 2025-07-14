def get_num_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    text = text.lower()
    letter_count = {}
    for letter in text:
        if letter.isalpha():
            letter_count[letter] = letter_count.get(letter, 0) + 1
    return letter_count

def get_letter_report(text):
    letter_count = count_letters(text)
    return "\n".join([f"{letter}: {count}" for letter, count in letter_count.items() if count > 0])

def sort_letter_count(letter_count):
    sorted_count = sorted(letter_count.items(), key=lambda x: x[1], reverse=True)
    return "\n".join([f"{letter}: {count}" for letter, count in sorted_count])