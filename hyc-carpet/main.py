import matplotlib
matplotlib.use("Agg") 
import mpld3
import matplotlib.pyplot as plt
from matplotlib import colors
from flask import Flask
from flask import request
import numpy
 
def calculate(degree):
    size=3**degree
    matrix=numpy.ones([size, size])
    for elem in range(degree+1):
        step=3**(degree-elem)
        for x in range(size):
            if x%3==1:
                for y in range(size):
                    if y%3==1:
                        matrix[y*step:(y+1)*step, x*step:(x+1)*step]=0
    return matrix

def render_carpet(degree):
    matrix=calculate(degree)

    fig=plt.figure()

    ax = plt.Axes(fig, [0., 0., 1., 1.])
    fig.add_axes(ax)

    img=ax.imshow(matrix)
    return mpld3.fig_to_html(fig)

app = Flask(__name__)

@app.route('/')
def hello_world():
    degree = request.args.get('degree', default = 6, type = int)
    print("Degree:", degree)
    return render_carpet(degree)

if __name__ == '__main__':
    app.run()