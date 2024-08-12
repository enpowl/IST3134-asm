#Mapper
#!/usr/bin/env python3
import sys
import re

def tokenize(text):
    # Simple word tokenization
    words = re.findall(r'\w+', text.lower())  # Convert to lowercase and find all word-like tokens
    return words

for line in sys.stdin:
    # Assuming the input format is CSV, with the review body as the last field
    fields = line.strip().split(',')
    if len(fields) < 3:
        continue  # Skip lines that don't have the correct format

    review_body = fields[2]  # The review body is the third field
    words = tokenize(review_body)

    for word in words:
        print(f'{word}\t1')

#Reducer
#!/usr/bin/env python3
import sys
from collections import defaultdict

word_counts = defaultdict(int)

# Aggregate word counts
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
        word_counts[word] += count
    except ValueError:
        continue

# Sort words by count and take the top 50
top_50_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:50]

# Output the top 50 words with their counts
for word, count in top_50_words:
    print(f'{word}\t{count}')

#Mapred Streaming in Hadoop
mapred streaming \
   -files /home/hadoop/workspace/mapper.py,/home/hadoop/workspace/reducer.py \
   -input /user/hadoop/input/train.csv \
   -output /user/hadoop/output/top50words \
   -mapper "python3 mapper.py" \
   -reducer "python3 reducer.py"

#output
hdfs dfs -cat /user/hadoop/output/top50words/part-00000

