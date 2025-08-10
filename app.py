import gradio as gr
from transformers import pipeline
import torch

get_completion = pipeline("summarization",model = "sshleifer/distilbart-cnn-12-6")

def summarize(input):
  output = get_completion(input)
  return output[0]['summary_text']

gr.close_all()

demo = gr.Interface(fn=summarize, inputs="text", outputs="text")

demo.launch(share=True, server_name="0.0.0.0", server_port=7860)
