import gradio as gr

def greet(name):
    return "hey " + name

demo = gr.Interface(fn= greet,
                    inputs="text",
                    outputs="text")

demo.launch(share=False) # share=False doesn't create a public link