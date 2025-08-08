import gradio as gradio
from transformers import pipeline

get_completion = pipeline("summarization",model = "sshleifer/distilbart-cnn-12-6")

def summarize(input):
  output = get_completion(input)
  return output[0]['summary_text']

gr.close_all()

demo = gr.Interface(fn=summarize, input="text", output="text")

demo.launch(share=Ture,)