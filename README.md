# Text Generation Using GPT-2

This project demonstrates how to generate text based on a custom prompt using a pre-trained GPT-2 model. The code utilizes the `transformers` library by Hugging Face to load the GPT-2 model, encode a prompt, and generate coherent text based on that prompt.

## Requirements

Before running the code, make sure to install the required dependencies. This project uses the Hugging Face `transformers` library and `torch` for working with the model.

### Install Dependencies

You can install the required dependencies using `pip`:

pip install transformers torch


- `transformers`: The Hugging Face library that provides access to various pre-trained models including GPT-2.
- `torch`: PyTorch, a deep learning framework used by the `transformers` library for model inference.

## Project Structure

The project consists of a single Python script that uses the GPT-2 model to generate text. Below is an explanation of the code flow:

/text-generation
  ├── generate_text.py        # Python script for generating text with GPT-2
  └── README.md               # This file (project documentation)


## Script Overview

### `generate_text.py`

This Python script loads a pre-trained GPT-2 model, encodes a user-provided prompt, and generates text based on that prompt. The generated text is then decoded and printed to the console.

### Key Components:

1. **Loading the Model and Tokenizer**:
   The pre-trained GPT-2 model and its corresponding tokenizer are loaded using Hugging Face's `from_pretrained` method.

2. **Prompt Encoding**:
   The input prompt is tokenized and encoded into the format that GPT-2 can process.

3. **Text Generation**:
   The `generate()` method is used to generate text from the encoded prompt. Several parameters control the behavior of the text generation, such as:
   - `max_length`: Maximum length of the generated text.
   - `num_return_sequences`: Number of text sequences to generate.
   - `temperature`: Controls the randomness of the generation (lower values make the output more deterministic).
   - `top_k` and `top_p`: Control diversity in sampling.
   - `no_repeat_ngram_size`: Prevents repetition in the generated text.

4. **Text Decoding**:
   The generated tokens are decoded back into human-readable text, and special tokens are removed (such as padding or end-of-sequence tokens).

5. **Output**:
   The resulting generated text is printed to the console.


### Important Parameters:

- `max_length`: Defines the maximum number of tokens for the generated text. The value is set to 100 by default in the script.
- `num_return_sequences`: Specifies the number of sequences to generate. The default is set to 1.
- `temperature`: Controls the randomness of predictions. A value close to 0 makes the model more focused (deterministic), and a value closer to 1 increases the randomness.
- `top_k` and `top_p`: These parameters control the diversity of the generated text by limiting the number of candidate tokens considered at each step.
- `no_repeat_ngram_size`: Helps prevent repetitive phrases by disallowing the generation of n-grams (e.g., 2-grams) that were already seen in the generated sequence.

### Example Output:

When you run the script, it will generate a story or text based on the given prompt. For example, with the prompt `"generate story over lion and rat"`, the output might look something like this:

The lion and the rat were once enemies, but one day, they found themselves in a strange situation. The rat had been caught in a hunter's trap, and the lion, seeing an opportunity to show mercy, decided to free the rat. The rat was grateful and promised to return the favor if the lion ever needed help. 

This is just an example, and the output will vary depending on the model's generation and randomness.

## Running the Script

To run the script and generate text, follow these steps:

1. Save the Python code into a file named `generate_text.py`.
2. Open a terminal and navigate to the directory where `generate_text.py` is located.
3. Run the script:

   python generate_text.py


4. The script will output the generated text based on the prompt `"generate story over lion and rat"` or whatever prompt you modify the code to use.

## Customizing the Prompt

To generate text based on a different topic or story, simply modify the `prompt` variable in the script. For example:

prompt = "once upon a time in a land far away, there was a brave knight"


This will generate a story starting with the new prompt.

## Troubleshooting

- **Error: `ModuleNotFoundError`**: Make sure that you have installed the required libraries with `pip install transformers torch`.
- **Out of Memory Errors**: If you are running into memory issues, try using a smaller model like `distilgpt2` instead of `gpt2`. You can change the model name like this:

  model_name = "distilgpt2"


## Conclusion

This project demonstrates how to leverage the power of pre-trained GPT-2 models to generate creative text based on custom prompts. By fine-tuning the model's generation parameters, you can control the length, diversity, and randomness of the output. Enjoy experimenting with different prompts and configurations to generate unique stories or content!
