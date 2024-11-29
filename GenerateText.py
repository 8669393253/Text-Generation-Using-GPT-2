from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Load the pre-trained model and tokenizer
model_name = "gpt2"  # You can also use larger versions like 'gpt2-medium', 'gpt2-large', etc.
model = GPT2LMHeadModel.from_pretrained(model_name)
tokenizer = GPT2Tokenizer.from_pretrained(model_name)

# Encode a prompt (starting text)
prompt = "generate story over lion and rat"
inputs = tokenizer(prompt, return_tensors="pt")

# Generate text using the model
outputs = model.generate(**inputs, max_length=100, num_return_sequences=1, no_repeat_ngram_size=2, temperature=0.7)

# Decode the generated text
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)

print(generated_text)
