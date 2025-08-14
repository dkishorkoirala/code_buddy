"""
Word Analytics


Challenge

Create a function named analyze_text that analyzes words in a text string.

Your function should:

Count unique words (case-insensitive)
Find all words that appear more than once
Identify all palindrome words (words that read the same forwards and backwards, like "level")
Return a dictionary with three keys:

unique_count: the number of unique words (count also repeated words once each)
repeated_words: a sorted list of words appearing more than once
palindromes: a sorted list of palindrome words
Notes:

Treat words as case-insensitive (e.g., "Hello" and "hello" are the same word)
Remove any punctuation (.,!?:;"()) from words
Sort both the repeated_words and palindromes lists alphabetically
Example Input:
"Madam saw a racecar. Dad said hello hello to mom."

Expected Output:
{
    'unique_count': 9,
    'repeated_words': ['hello'],
    'palindromes': ['a', 'dad', 'madam', 'mom', 'racecar']
}"""


def analyze_text(text):
    # Step 1: remove punctuation manually and lowercase
    punctuation = '.,!?:;"()'
    for p in punctuation:
        text = text.replace(p, "")
    words = text.lower().split()

    # Step 2: count word occurrences
    word_count = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1

    # Step 3: unique word count
    unique_count = len(word_count)

    # Step 4: repeated words (appearing more than once)
    repeated_words = sorted([word for word, count in word_count.items() if count > 1])

    # Step 5: palindrome words
    palindromes = sorted([word for word in word_count if word == word[::-1]])

    # Step 6: return results
    return {
        "unique_count": unique_count,
        "repeated_words": repeated_words,
        "palindromes": palindromes,
    }


t = "Wow! Did Hannah see that Race car? Mom was there too. Hannah did see it!"

print(analyze_text(t))
