#!/usr/bin/env python3

from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import torch.nn.functional as F

# Load the model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("models/Czech-GPT-2-XL-133k")
model = AutoModelForCausalLM.from_pretrained("models/Czech-GPT-2-XL-133k").eval()

# Prompt
prompt = "Nejznámějším českým spisovatelem "

# Encode the prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Generate tokens step by step
generated_ids = input_ids
all_probs = []

# Generate tokens one by one to get probabilities
for _ in range(10):  # Generate 64 new tokens
    with torch.no_grad():
        outputs = model(input_ids=generated_ids)
        next_token_logits = outputs.logits[:, -1, :]
        
        # Apply temperature and top-p sampling
        next_token_logits = next_token_logits / 0.8  # temperature
        sorted_logits, sorted_indices = torch.sort(next_token_logits, descending=True)
        cumulative_probs = torch.cumsum(F.softmax(sorted_logits, dim=-1), dim=-1)
        sorted_indices_to_remove = cumulative_probs > 0.95  # top_p
        sorted_indices_to_remove[..., 1:] = sorted_indices_to_remove[..., :-1].clone()
        sorted_indices_to_remove[..., 0] = 0
        
        next_token_logits[sorted_indices_to_remove] = -float('Inf')
        next_token_probs = F.softmax(next_token_logits, dim=-1)

        # Sample from the distribution
        next_token = torch.multinomial(next_token_probs, num_samples=1)
        next_token_prob = next_token_probs.gather(1, next_token)

        # Append the generated token and its probability
        generated_ids = torch.cat((generated_ids, next_token), dim=1)
        all_probs.append(next_token_prob)

# Decode the generated tokens
generated_text = tokenizer.decode(generated_ids[0], skip_special_tokens=True)
print(generated_text)

# Convert all_probs to a tensor
all_probs_tensor = torch.cat(all_probs, dim=1)
print(all_probs_tensor)

