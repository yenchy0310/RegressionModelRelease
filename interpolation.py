import math
import numpy as np

# def calculate_ppm_surface_signal(coef, x0, degree): 
#     '''Caculate the signal of each data pair of temperature and humidity  
#         coef=list 
#         x0=float (temperature)
#         return float'''
    
#     if degree == 1 :
#         term = [1, x0]
    
#     elif degree == 2:
#         term = [1, x0, x0**2]
        
#     elif degree == 3:
#         term = [1, x0, x0**2, x0**3]
                                                                                                                                    
#     else:
#         print('Check degree value') 
        
#     signal = np.inner(coef, term)

#     return signal


def calculate_ppm_surface_signal(coef, x0, x1, degree): 
    '''Caculate the signal of each data pair of temperature and humidity  
        coef : list 
        x0 : float (temperature)
        x1 : float (humidity)
        return float'''
    
    if degree == 1 :
        term = [1, x0, x1]
    
    elif degree == 2:
        term = [1, x0, x1, x0**2, x0*x1, x1**2]
        
    elif degree == 3:
        term = [1, x0, x1, x0**2, x0*x1, x1**2, x0**3, x0**2*x1, x0*x1**2, x1**3]
                                                                                                                                    
    else:
        print('Check degree value') 
        
    signal = np.inner(coef, term)

    return signal


def __interpolation(signal_ppm_dict, signal, low, up):    
    ppm = (up-low) / (signal_ppm_dict[up]-signal_ppm_dict[low]) * (signal-signal_ppm_dict[low]) + low
    return ppm
    
def __extrapolation(signal_ppm_dict, signal, low, up):    
    ppm = (up-low) / (signal_ppm_dict[up]-signal_ppm_dict[low]) * (signal-signal_ppm_dict[up]) + up
    return ppm

def __exponential_interpolation(signal_ppm_dict, signal, low, up):
    log_ppm = math.log(up-low) / (signal_ppm_dict[up]-signal_ppm_dict[low]) * (signal-signal_ppm_dict[low]) + math.log((low+1))
    ppm = math.exp(log_ppm)
    return ppm

def __exponential_extrapolation(signal_ppm_dict, signal, low, up):    
    log_ppm = math.log(up-low) / (signal_ppm_dict[up]-signal_ppm_dict[low]) * (signal-signal_ppm_dict[up]) + math.log(up)
    ppm = math.exp(log_ppm)
    return ppm
    
def linear_interpolation(signal_ppm_dict, signal, ppm_low, ppm_mid, ppm_up):
    '''predict ppm by interpolation algorithm
       signal_ppm_dict : dictionary
       signal : int, sensor raw data
       ppm_low : int
       ppm_mid : int
       ppm_up : int'''
        
    if (signal_ppm_dict[ppm_up] > signal_ppm_dict[ppm_low]):    
    
        # linear interpolation
        if (signal > signal_ppm_dict[ppm_low]) & (signal <= signal_ppm_dict[ppm_mid]):
            low = ppm_low
            up = ppm_mid
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm   
        
        # linear interpolation
        elif (signal > signal_ppm_dict[ppm_mid]) & (signal <=signal_ppm_dict[ppm_up]):
            low = ppm_mid
            up = ppm_up            
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        # linear extrapolation
        elif (signal > signal_ppm_dict[ppm_up]):
            low = ppm_mid
            up = ppm_up 
            ppm = __extrapolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        else:
            return 0
        
    else:
        
        # linear interpolation
        if (signal < signal_ppm_dict[ppm_low]) & (signal >= signal_ppm_dict[ppm_mid]):
            low = ppm_low
            up = ppm_mid
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm   
        
        # linear interpolation
        elif (signal < signal_ppm_dict[ppm_mid]) & (signal >=signal_ppm_dict[ppm_up]):
            low = ppm_mid
            up = ppm_up            
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        # linear extrapolation
        elif (signal < signal_ppm_dict[ppm_up]):
            low = ppm_mid
            up = ppm_up 
            ppm = __extrapolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        else:
            return 0
        
def exponential_interpolation(signal_ppm_dict, signal, ppm_low, ppm_up):
    '''predict ppm by interpolation algorithm
       signal_ppm_dict : dictionary
       signal : int, sensor raw data
       ppm_low : int
       ppm_up : int'''
    
    if (signal_ppm_dict[ppm_up] > signal_ppm_dict[ppm_low]):    
        
        # exponential interpolation
        if (signal > signal_ppm_dict[ppm_low]) & (signal <= signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_interpolation(signal_ppm_dict, signal, low, up) 
            return ppm
        
        # exponential extrapolation
        elif (signal > signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_extrapolation(signal_ppm_dict, signal, low, up)
            return ppm

        else:
            return 0
        
    else:
        
        # exponential interpolation
        if (signal < signal_ppm_dict[ppm_low]) & (signal >= signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_interpolation(signal_ppm_dict, signal, low, up) 
            return ppm
        
        # exponential extrapolation
        elif (signal < signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_extrapolation(signal_ppm_dict, signal, low, up)
            return ppm
    
    
def hybrid_interpolation(signal_ppm_dict, signal, ppm_low, ppm_mid, ppm_up):
    
    '''predict ppm by interpolation algorithm
       signal_ppm_dict : dictionary
       signal : int, sensor raw data
       ppm_low : int
       ppm_up : int'''
    
    if (signal_ppm_dict[ppm_up] > signal_ppm_dict[ppm_low]):    
    
        #linear interpolatio
        if (signal > signal_ppm_dict[ppm_low]) & (signal <= signal_ppm_dict[ppm_mid]):
            low = ppm_low
            up = ppm_mid
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        #exponential interpolation
        elif (signal > signal_ppm_dict[ppm_mid]) & (signal <= signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_interpolation(signal_ppm_dict, signal, low, up)  
            return ppm
        
        #exponential extrapolation
        elif (signal > signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_extrapolation(signal_ppm_dict, signal, low, up) 
            return ppm

        else:
            return 0
        
    else:
        
        #linear interpolatio
        if (signal < signal_ppm_dict[ppm_low]) & (signal >= signal_ppm_dict[ppm_mid]):
            low = ppm_low
            up = ppm_mid
            ppm = __interpolation(signal_ppm_dict, signal, low, up)
            return ppm
        
        #exponential interpolation
        elif (signal < signal_ppm_dict[ppm_mid]) & (signal >= signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_interpolation(signal_ppm_dict, signal, low, up)  
            return ppm
        
        #exponential extrapolation
        elif (signal < signal_ppm_dict[ppm_up]):
            low = ppm_low
            up = ppm_up
            ppm = __exponential_extrapolation(signal_ppm_dict, signal, low, up) 
            return ppm

        else:
            return 0
        
     
        

