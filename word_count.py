def count_words(text):
    """Function to count the number of words in a given text."""
    words = text.split()
    return len(words)

def main():
    """Main function to take user input and display word count."""
    try:
        user_input = input("Enter a sentence or paragraph: ")
        word_count = count_words(user_input)
        print(f"Word Count: {word_count}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
