import gradio as gr
import pandas as pd
import pickle


def predict(revolutions, humidity, x1, x2, x3, x4, x5):
    tst = pd.DataFrame([[revolutions, humidity, x1, x2, x3, x4, x5]],
          columns=['revolutions', 'humidity', 'x1', 'x2', 'x3', 'x4', 'x5'])
    filehandler = open("elevator.pkl", "rb")
    bm_loaded = pickle.load(filehandler)
    filehandler.close()
    a=bm_loaded.predict(tst)
    b=a[0]
    return b

with gr.Blocks() as demo:
    with gr.Row():
      revolutions = gr.Number(label='revolutions')
      humidity = gr.Number(label='humidity')
    with gr.Row():
      x1 = gr.Number(label='x1')
      x2 = gr.Number(label='x2')
      x3 = gr.Number(label='x3')
      x4= gr.Number(label='x4')
      x5= gr.Number(label='x5')
    with gr.Row(): 
      Vibration = gr.Number(label='vibration') 
    with gr.Row():  
      button = gr.Button(value="What Vibration?")
      button.click(predict,
            inputs=[revolutions, humidity, x1, x2, x3, x4, x5],
            outputs=[Vibration])
demo.launch()