import gradio as gr
from transformers import pipeline

generator = pipeline("text-generation", max_new_tokens=100, pad_token_id=50256, num_return_sequences=2)

def predict(prompt):
    completion = generator(prompt)[0]["generated_text"]
    print(completion)
    return completion

def greet(name):
    return "Hello " + name

# We instantiate the Textbox class
textbox = gr.Textbox(label="Type your name here:", placeholder="John Doe", lines=2)

# demo = gr.Interface(fn=greet, inputs="text", outputs="text")
# demo = gr.Interface(fn=greet, inputs=textbox, outputs="text")
demo = gr.Interface(fn=predict, inputs=textbox, outputs="text")


demo.launch()