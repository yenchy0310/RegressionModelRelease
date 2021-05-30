import numpy as np

def create_white_card_std_column(data, white_intercept, white_coef, degree):

    white_card_std_list = []
    for temp in data['Temperature']: 

        if degree == 1:
            term = [temp]
        
        elif degree == 2:
            term = [temp, temp**2]
    
        else:
            print('Check degree value') 
        
        white_card_std = np.inner(white_coef, term) + white_intercept       
        white_card_std_list.append(float(white_card_std)) 

    data['white card std'] = white_card_std_list