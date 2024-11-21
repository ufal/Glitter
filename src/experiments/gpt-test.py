#!/usr/bin/env python3

from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
import torch.nn.functional as F

# Load a pre-trained GPT-2 model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")
model.eval()  # Set the model to evaluation mode

def predict_next_token_probabilities(text, top_k=10):
    # Tokenize the input text and convert to tensor
    inputs = tokenizer(text, return_tensors="pt")
    
    # Forward pass through the model to get logits
    with torch.no_grad():  # Disable gradient calculation for faster inference
        outputs = model(**inputs)
    
    # Get logits for the last token in the sequence
    next_token_logits = outputs.logits[:, -1, :]
    
    # Apply softmax to get probabilities
    probabilities = F.softmax(next_token_logits, dim=-1)
    
    # Get the top k token probabilities and their indices
    top_k_probs, top_k_indices = torch.topk(probabilities, top_k)
    
    # Convert indices to actual tokens and store with probabilities
    tokens_with_probs = [
        {"token": tokenizer.decode([idx]), "probability": prob.item()}
        for idx, prob in zip(top_k_indices[0], top_k_probs[0])
    ]
    
    return tokens_with_probs

# Example usage
text = "Today is "
predictions = predict_next_token_probabilities(text, top_k=5)
print(predictions)
for pred in predictions:
    print(f"Token: {pred['token']}, Probability: {pred['probability']}")


