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
        coef=list 
        x0=float (temperature)
        x1=float (humidity)
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

def interpolation(signal, signal_0ppm, signal_10ppm, signal_60ppm):
    '''predict ppm by interpolation algorithm
       signal=int (real-time signal)'''
    
    if (signal_0ppm < signal_60ppm): # positive response
    
        if (signal>signal_0ppm)&(signal<signal_10ppm):
            ppm = abs(10-0)/abs(signal_10ppm-signal_0ppm)*abs((signal)-signal_0ppm) #interpolation
            return ppm

        elif (signal>signal_10ppm)&(signal<signal_60ppm):
            ppm = abs(60-10)/abs(signal_60ppm-signal_10ppm)*abs((signal)-signal_10ppm)+10 #interpolation
            return ppm

        elif (signal > signal_60ppm):
            ppm = abs(60-10)/abs(signal_60ppm-signal_10ppm)*abs((signal)-signal_60ppm)+60
            return ppm

        else:
            ppm = (-10)/(signal_0ppm-signal_10ppm)*((signal)-signal_0ppm)
            return ppm
        
    else: # negative response
        
        if (signal<signal_0ppm)&(signal>signal_10ppm):
            ppm = abs(10-0)/abs(signal_10ppm-signal_0ppm)*abs((signal)-signal_0ppm) #interpolation
            return ppm

        elif (signal<signal_10ppm)&(signal>signal_60ppm):
            ppm = abs(60-10)/abs(signal_60ppm-signal_10ppm)*abs((signal)-signal_10ppm)+10 #interpolation
            return ppm

        elif (signal < signal_60ppm):
            ppm = abs(60-10)/abs(signal_60ppm-signal_10ppm)*abs((signal)-signal_60ppm)+60
            return ppm

        else:
            ppm = (-10)/(signal_0ppm-signal_10ppm)*((signal)-signal_0ppm)
            return ppm