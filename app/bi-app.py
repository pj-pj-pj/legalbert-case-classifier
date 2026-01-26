import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

MODEL_PATH = "./models/binary_legalbert_model_20260124_152458"

# Load tokenizer and model
tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_PATH)

# Put model in eval mode
model.eval()

# Label mapping 
LABEL_MAP = {
    0: "CIVIL",
    1: "CRIMINAL",
    # 2: "LEGAL FEES"
}

print("LegalBERT Binary Classifier")
print("Type 'exit' to quit\n")

while True:
    text = input("Enter legal text: ").strip()

    if text.lower() == "exit":
        break

    # Tokenize input
    inputs = tokenizer(
        text,
        return_tensors="pt",
        truncation=True,
        padding=True,
        max_length=512
    )

    # Inference (no gradients needed)
    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class = torch.argmax(logits, dim=1).item()

    print(f"Prediction: {LABEL_MAP[predicted_class]}\n")
