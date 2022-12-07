import gradio as gr
import pandas as pd
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

iris = load_iris()


def plot(atr1, atr2, plott):
    
    # The indices of the features that we are plotting
    labels = dict()
    # print(iris.data[0])
    for i in range(len(iris.data[0])):
        labels[iris.feature_names[i]] = i
    print(atr1)
    print(labels[atr1])
    print(atr2)
    print(labels[atr2])
    xidx = int(labels[atr1])
    yidx = int(labels[atr2])
    # xidx=0
    # yidx=1
    fig = plt.figure(figsize=(5, 4))
    if plott == 'Scatter':
      plt.scatter(iris.data[:, xidx], iris.data[:, yidx], c=iris.target)
      plt.xlabel(iris.feature_names[xidx])
      plt.ylabel(iris.feature_names[yidx])

    elif plott=='Histogram':
      plt.hist(x=iris.data,  histtype ='bar')
      plt.xlabel("Values")
      plt.ylabel("Frequency")
      plt.legend(cols)
    plt.tight_layout()
   
    return fig


demo = gr.Blocks()

with demo:
    gr.Markdown(
        r"Let Draw some Graph on iris"
    )
    with gr.Row():
      cols = []
      
      # print(iris.data[0])
      for i in range(len(iris.data[0])):
          cols.append(iris.feature_names[i])
      atr1 = gr.Dropdown(label = "First Attribute" , choices=cols)
      atr2 = gr.Dropdown(label = "Second Attribute" , choices=cols)
      plott = gr.Dropdown(label = "Select plot" , choices=['Scatter','Histogram','Boxplot'])
    output = gr.Plot()
    btn1 = gr.Button(value="Run")
    btn1.click(fn=plot, inputs=[atr1, atr2, plott],outputs=output)

if __name__ == "__main__":
    demo.launch(debug=True)
