
# import iplot package
import plotly.graph_objs as go
import plotly.express as px
import plotly.offline as offline
from plotly.offline import init_notebook_mode
import cufflinks as cf
cf.go_offline(connected=True)
init_notebook_mode(connected=True)

# import plotly.graph_objs as go
# import plotly.offline as offline
# from plotly.offline import init_notebook_mode
# import cufflinks as cf
# cf.go_offline(connected=True)


def plot_4D(training_data, testing_data, channel_list, sensor_number):
    '''Visualize 4D data, x=Humidity, y=Temperautre, z=channel, color=ppm
       channel_list = ['900nm #1_mv_comp', '900nm #1'] or ['900nm #1_mv_comp']
       trainning_data, testing_data is a dictionary
       training_data = {'0C':df_0C,
                        '10C':df_10C,
                        '20C':df_20C,
                        '30C':df_30C,
                        '40C':df_40C,
                        '50C':df_50C 
                        }

        testing_data = {
                        '4C_test':df_test_4C,
                        '27C_test':df_test_27C
                        }
    '''


    data = []
    for channel in channel_list:
        for name, df_data in training_data.items():
            trace = go.Scatter3d(x = df_data['Humidity'],
                                 y = df_data['Temperature'],
                                 z = df_data[channel],
                                 mode='markers',
                                 name=name,
                                 marker=dict(size=2,
                                             symbol='circle',
                                             opacity=0.5,
                                             color=df_data['ppm'],
                                             colorscale=[[0, 'rgb(255,160,122)'], [1.0, 'rgb(128,0,0)']])
                                             )
            data.append(trace)

        for name, df_data in testing_data.items():
            trace_1 = go.Scatter3d(x = df_data['Humidity'],
                                   y = df_data['Temperature'],
                                   z = df_data[channel],
                                   mode='markers',
                                   name=name,
                                   marker=dict(size=2,
                                               symbol='circle',
                                               opacity=0.5,
                                               color=df_data['ppm'],
                                               colorscale=[[0, 'rgb(192,192,192)'], [1.0, 'rgb(0,0,0)']])
                                               )
            data.append(trace_1)
            
    # convert channels list to string        
    channel_list = ', '.join(channel_list)    
    layout = go.Layout(title = '4D '+ channel_list + ' ' +sensor_number,
                       scene = dict(xaxis = dict(title='Humidity'),
                                    zaxis = dict(title=channel),
                                    yaxis = dict(title='Temperature')),
                                    margin=dict(l=50, r=50, b=50, t=50))
        
    fig = go.Figure(data=data, layout=layout)
    cf.iplot(fig)
    
def plot_4D_multi_model(training_data, testing_data, channel_list, sensor_number):
    '''Visualize 4D data, x=Humidity, y=Temperautre, z=channel, color=ppm
       channel_list = ['900nm #1_mv_comp', '900nm #1'] or ['900nm #1_mv_comp']
       trainning_data, testing_data is a list
       training_data = [df_0C, df_10C, df_20C, df_30C, df_40C, '50C':df_50C] 
       testing_data = [df_test_4C, df_test_27C]
    '''


    data = []
    for channel in channel_list:
        for df_data in training_data:
            trace = go.Scatter3d(x = df_data['Humidity'],
                                 y = df_data['Temperature'],
                                 z = df_data[channel],
                                 mode='markers',
                                 marker=dict(size=2,
                                             symbol='circle',
                                             opacity=0.5,
                                             color=df_data['ppm'],
                                             colorscale=[[0, 'rgb(255,160,122)'], [1.0, 'rgb(128,0,0)']])
                                             )
            data.append(trace)

        for df_data in testing_data:
            trace_1 = go.Scatter3d(x = df_data['Humidity'],
                                   y = df_data['Temperature'],
                                   z = df_data[channel],
                                   mode='markers',
                                   marker=dict(size=2,
                                               symbol='circle',
                                               opacity=0.5,
                                               color=df_data['ppm'],
                                               colorscale=[[0, 'rgb(192,192,192)'], [1.0, 'rgb(0,0,0)']])
                                               )
            data.append(trace_1)
            
    # convert channels list to string        
    channel_list = ', '.join(channel_list)    
    layout = go.Layout(title = '4D '+ channel_list + ' ' +sensor_number,
                       scene = dict(xaxis = dict(title='Humidity'),
                                    zaxis = dict(title=channel),
                                    yaxis = dict(title='Temperature')),
                                    margin=dict(l=50, r=50, b=50, t=50))
        
    fig = go.Figure(data=data, layout=layout)
    cf.iplot(fig)