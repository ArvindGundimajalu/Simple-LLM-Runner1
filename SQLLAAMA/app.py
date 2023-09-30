import gradio as gr
import time
from ctransformers import AutoModelForCausalLM

def load_llm():
    #llm = AutoModelForCausalLM.from_pretrained("TheBloke/CodeLlama-13B-Instruct-GGUF",
    llm = AutoModelForCausalLM.from_pretrained("sqllama/llama-7b-sqlcreatecontext-lora-defaultparams",
    model_type='llama',
    max_new_tokens = 1096,
    repetition_penalty = 1.13,
    temperature = 0.1
    )
    return llm

def llm_function(message, chat_history):
    start = time.time()
    llm = load_llm()
    response = llm(
        message
    )
    output_texts = response
    end = time.time()
    print(end - start)
    return output_texts

title = "CodeLlama 13B GGUF Demo"

examples = [
    'Write a python code to connect with a SQL database and list down all the tables.',
    'Write the python code to train a linear regression model using Scikit Learn.',
    'Explain the concepts of Functional Programming.',
    'Can you explain the benefits of Python programming language?'
]

gr.ChatInterface(
    fn=llm_function,
    title=title,
    examples=examples
).launch()