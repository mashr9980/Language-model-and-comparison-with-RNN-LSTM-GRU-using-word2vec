import pandas as pd

# Load the dataset from a TSV file
file_path = "amazon_reviews_us_Office_Products_v1_00.tsv"  
df = pd.read_csv(file_path, sep='\t', error_bad_lines=False, dtype='str')

# Convert 'star_rating' column to integers after cleaning
df['star_rating'] = df['star_rating'].str.extract('(\d+)').astype(float).fillna(0).astype(int)

# Randomly shuffle the dataset
df = df.sample(frac=1, random_state=42).reset_index(drop=True)

# Define the number of positive (high-rated) and negative (low-rated) reviews to include
sample_size = 1000000 // 2  # Balanced dataset with 50K positive and 500K negative reviews

# Select positive (4 and 5-star) and negative (1 and 2-star) reviews
positive_reviews = df[df['star_rating'] >= 4].sample(n=sample_size, random_state=42)
negative_reviews = df[df['star_rating'] <= 2].sample(n=sample_size, random_state=42)

# Concatenate positive and negative samples to create the balanced dataset
balanced_dataset = pd.concat([positive_reviews, negative_reviews], ignore_index=True)

# Shuffle the balanced dataset again (optional)
balanced_dataset = balanced_dataset.sample(frac=1, random_state=42).reset_index(drop=True)

# Save the balanced dataset to a new CSV file
balanced_dataset.to_csv("balanced_reviews.csv", index=False)

# Display the first few rows of the balanced dataset
print(balanced_dataset.head())