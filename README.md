# legalbert-case-classifier

google colab environment for training legalbert as a binary case classifier (criminal vs civil)

## Data Preprocessing/Cleaning

- line breaks and tabs are replaced with ' '
- removed dates and numbers
- legal punctuation are preserved, excessive special chars are removed
- normalize whitespace

-> saved to cases_cleaned.csv

## Dataset Splitting

The dataset was partitioned into training (70%) and testing (20%) sets. To ensure the model is evaluated on a realistic distribution of cases, we used stratified sampling based on the `label` column.
