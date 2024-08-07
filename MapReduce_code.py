# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 00:12:50 2024

@author: JM
"""

import pandas as pd
import time

# Measure the start time
start_time = time.time()

# Read CSV files
reviews_df = pd.read_csv(r"C:\Users\junmi\Downloads\archive\Books_rating.csv")

# Print column names to verify
print("Columns in reviews_df:", reviews_df.columns)

# Display the first 10 rows of the DataFrame
print("First 10 rows of reviews_df:")
print(reviews_df.head(10))

# Calculate word count for review/text
reviews_df['word_count'] = reviews_df['review/text'].apply(lambda x: len(str(x).split()))

# Perform MapReduce operations using pandas

# 1. Count the number of reviews per book and calculate the total review score
review_counts = reviews_df.groupby('Id').size().reset_index(name='review_count')
total_scores = reviews_df.groupby('Id')['review/score'].sum().reset_index(name='total_score')

# 2. Merge the counts and total scores
aggregated_data = pd.merge(review_counts, total_scores, on='Id')

# 3. Calculate the average review score for each book
aggregated_data['average_score'] = aggregated_data['total_score'] / aggregated_data['review_count']

# Calculate total word count for each book
word_counts = reviews_df.groupby('Id')['word_count'].sum().reset_index(name='word_count')

# Merge word counts with aggregated data
final_data = pd.merge(aggregated_data, word_counts, on='Id')

# Select relevant columns for output
final_output = final_data[['Id', 'review_count', 'average_score', 'word_count']]

# Save the result to a CSV file
final_output.to_csv(r"C:\Users\junmi\Downloads\archive\aggregated_book_reviews.csv", index=False)

print("Aggregation complete. The results have been saved to 'aggregated_book_reviews.csv'.")

# Display the first 10 rows of the final output
print("First 10 rows of the final output:")
print(final_output.head(10))

# Calculate total word count
total_word_count = final_output['word_count'].sum()
print(f"Total word count: {total_word_count}")

# Measure the end time
end_time = time.time()

# Calculate the elapsed time
elapsed_time = end_time - start_time
print(f"Processing time: {elapsed_time} seconds")
