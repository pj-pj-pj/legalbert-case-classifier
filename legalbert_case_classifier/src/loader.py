from transformers import AutoModelForSequenceClassification
from transformers import AutoTokenizer

# load lb tokenizer
tokenizer = AutoTokenizer.from_pretrained(
    "nlpaueb/legal-bert-base-uncased"
)


# load legalbert
model = AutoModelForSequenceClassification.from_pretrained(
    "nlpaueb/legal-bert-base-uncased",
    num_labels=3 # 2 for Bi-Classification, 3 otherwise (with legal fees)
)

