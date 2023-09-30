# Load model directly
from transformers import AutoTokenizer, AutoModelForCausalLM

tokenizer = AutoTokenizer.from_pretrained("sqllama/llama-7b-sqlcreatecontext-lora-defaultparams")
model = AutoModelForCausalLM.from_pretrained("sqllama/llama-7b-sqlcreatecontext-lora-defaultparams")

text = """CREATE TABLE stadium (
    stadium_id number,
    location text,
    name text,
    capacity number,
)

-- Using valid SQLite, answer the following questions for the tables provided above.

-- how many stadiums in total?

SELECT"""

input_ids = tokenizer(text, return_tensors="pt").input_ids

generated_ids = model.generate(input_ids, max_length=500)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))