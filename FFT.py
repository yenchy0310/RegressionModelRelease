import numpy as np
import pandas as pd

def FFT_transform(data):
    
    '''Fourier Transform'''
    
    FFT_channel = ['410nm #1_mv', '440nm #1_mv', '470nm #1_mv', 
                   '510nm #1_mv', '550nm #1_mv', '583nm #1_mv', 
                   '620nm #1_mv', '670nm #1_mv', '900nm #1_mv',
        
                   '410nm #2_mv', '440nm #2_mv', '470nm #2_mv', 
                   '510nm #2_mv', '550nm #2_mv', '583nm #2_mv', 
                   '620nm #2_mv', '670nm #2_mv', '900nm #2_mv']
    
    columns_amp = ['410nm #1_mv_FFT_amp', '440nm #1_mv_FFT_amp', '470nm #1_mv_FFT_amp', 
                   '510nm #1_mv_FFT_amp', '550nm #1_mv_FFT_amp', '583nm #1_mv_FFT_amp', 
                   '620nm #1_mv_FFT_amp', '670nm #2_mv_FFT_amp', '900nm #1_mv_FFT_amp',    
        
                   '410nm #2_mv_FFT_amp', '440nm #2_mv_FFT_amp', '470nm #2_mv_FFT_amp', 
                   '510nm #2_mv_FFT_amp', '550nm #2_mv_FFT_amp', '583nm #2_mv_FFT_amp', 
                   '620nm #2_mv_FFT_amp', '670nm #2_mv_FFT_amp', '900nm #2_mv_FFT_amp']
    
    FFT_amp = np.abs(np.fft.fft(data[FFT_channel]))
    df_FFT_amp = pd.DataFrame(FFT_amp, columns=columns_amp)
    data = pd.concat([data, df_FFT_amp], axis=1, copy=True)
    return data