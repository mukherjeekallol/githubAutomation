def word_count(text):
    words = text.split()
    return len(words)

if __name__ == "__main__":
    sample_text = "This is a simple word count program."
    count = word_count(sample_text)
    print(f"Number of words: {count}")