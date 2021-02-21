from frame import Frame
from object_frame import Object_Frame
import plotly.graph_objects as go
import numpy as np

def plotter(frames = [],rest_frame:Frame = Frame()):
    
    new_vel = [x.relative_velocity(rest_frame) for x in frames]
    slopes = [rest_frame.c/x for x in new_vel if x != 0]
    
    x = np.arange(-10,10,1)
    fig = go.Figure()
    for index,slope in enumerate(slopes):
        fig.add_trace(go.Scatter(x=x, y=slope*x,
                        mode='lines+markers',
                        name='{}'.format(index)))

    fig.add_trace(go.Scatter(x=[0 for _ in x], y=x,
                        mode='lines+markers',
                        name='RestFrame'))

    fig.update_layout(title='Minkowski Diagram: frame_vel : {}m/s'.format(rest_frame._velocity),
                   xaxis_title='distance in 3e8 m',
                   yaxis_title='time in 1 second', template='plotly_dark')
    fig.update_xaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black', range=[-10, 10])
    fig.update_yaxes(zeroline=True, zerolinewidth=2, zerolinecolor='Black', range=[-10, 10])

    fig.show()

if __name__ == "__main__":
    c = 3e8
    frames = [Frame(c/i) for i in range(1,5)]
    plotter(frames)
    #plotter(frames,Frame(2e8))