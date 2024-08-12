# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:23:24 2024

@author: JM
"""

# Non-MapReduce (Word Count only)
from collections import Counter
import re
import pandas as pd
import time

def count_words(text_data):
    # Create a Counter object to count word occurrences
    word_count = Counter()

    # Iterate through the text data and update the word count
    for line in text_data:
        # Convert line to lowercase and split into words
        words = re.findall(r'\b\w+\b', line.lower())
        # Update the word count
        word_count.update(words)

    return word_count

def display_word_count(word_count):
    # Calculate the total word count
    total_word_count = sum(word_count.values())

    # Print the word count
    for word, count in word_count.items():
        print(f"{word}: {count}")
    print(f"\nTotal words: {total_word_count}")

def top_words_by_count(word_count, top_n=50):
    # Sort words by total count in descending order and get the top N
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)[:top_n]

    # Display top N words and their counts
    print(f"\nTop {top_n} words by count:")
    for word, count in sorted_words:
        print(f"{word}: {count}")

def main():
    # Measure the start time
    start_time = time.time()
    
    # File paths
    csv_file = r'C:\Users\khaiy\OneDrive\Documents\Big data in the cloud\train.csv\train.csv'
    column_name = 'This sound track was beautiful! It paints the senery in your mind so well I would recomend it even to people who hate vid. game music! I have played the game Chrono Cross but out of all of the games I have ever played it has the best music! It backs away from crude keyboarding and takes a fresher step with grate guitars and soulful orchestras. It would impress anyone who cares to listen! ^_^'  # Replace with the actual column name

    # Read the CSV file
    csv_data = pd.read_csv(csv_file)
    print(csv_data.columns)

    # Extract the selected column data and drop any NaN values
    text_data = csv_data[column_name].dropna().tolist()

    # Count words in the text data
    word_count = count_words(text_data)

    # Display the word count in the console
    display_word_count(word_count)

    # Display top 20 words by total count
    top_words_by_count(word_count)

    print("Word count has been displayed in the console.")
    
    # Measure the end time
    end_time = time.time()

    # Calculate the elapsed time
    elapsed_time = end_time - start_time
    print(f"Processing time: {elapsed_time} seconds")

if __name__ == '__main__':
    main()
