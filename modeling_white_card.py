import os
import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler

# Import plotly package
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.offline as offline
from plotly.offline import init_notebook_mode
import cufflinks as cf
cf.go_offline(connected=True)
init_notebook_mode(connected=True)

class modeling_white:
    '''channel: analysis channel (ex: 440nm #1_mv_comp)
       x_train: training data for model building
       y_train: ppm for model building
       x_test: testing data for model evaluation
       y_test: ppm for model        
       '''
    def __init__(self, name, sensor_number, channel, x_train, y_train, x_test, y_test, model_name, degree):
        self.name = name
        self.sensor_number = sensor_number
        self.channel = channel
        self.x_train = x_train
        self.y_train = y_train
        self.x_test = x_test
        self.y_test = y_test
        self.model_name = model_name
        self.degree = degree
        self.poly = PolynomialFeatures(degree=self.degree, include_bias=False)
        
        
    def regression_white_card(self):
        
        x = self.x_train[['Temperature']]
        X_ = self.x_test[['Temperature']]
        
        x = self.poly.fit_transform(x)
        X_ = self.poly.fit_transform(X_)
      

        # training set 
        model = self.model_name.fit(x, self.y_train[self.channel])
        yfit = model.predict(x)
        self.coeff = model.coef_
        self.intercept = model.intercept_
        self.rmse_train = np.sqrt(mean_squared_error(self.y_train[self.channel], yfit))

        # create a folder to store csv file
        self.folderName = '{}_degree={}'.format(self.name, self.degree)
#         self.folderName = 'degree={}_output_modify={}'.format(self.degree, self.output_modify)
        self.savePath = os.path.join(os.getcwd(), self.folderName)
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)

#         (New format)create a csv to save coefficient and white card std value for each channel    
        self.T_lower_bound = np.floor(self.x_train['Temperature'].min()) #取溫度下限
        self.T_upper_bound = np.ceil(self.x_train['Temperature'].max()) #取溫度上限
        self.H_lower_bound = np.floor(self.x_train['Humidity'].min()) #取濕度下限
        self.H_upper_bound = np.ceil(self.x_train['Humidity'].max()) #取濕度上限
        wavelength = self.channel.split(' ')[0]
                 
        coef_list = [self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound, self.degree, self.intercept]
        for i in self.coeff:
            coef_list.append(i)
        
        df_coef = pd.DataFrame()        
        df_coef['coefficient'] = coef_list #model coefficient  
        df_coef.T.to_csv(self.savePath + '/{}_T={}~{}_H={}~{}_{}.csv'.format(self.sensor_number, self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound, self.channel), header=False, index=False)

        
#         # (Old format vertical)create a csv to save coefficient and white card std value for each channel          
#         df_coef = pd.DataFrame()
#         df_coef['coefficient'] = np.insert(self.coeff, 0, self.intercept)
#         wavelength = self.channel.split(' ')[0]
#         df_coef['white_card_std'] = self.white_card_std['{} #{}'.format(wavelength, self.white_card_side)][0]
#         df_coef.to_csv(self.savePath + '/{}_T={}~{}_H={}~{}_degree={}_{}_shift{}_ppmx{}.csv'.format(self.sensor_number, self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound,  self.degree, self.channel, self.shift, self.multiple), header=False, index=False)

        # testing set
        self.y_pred = model.predict(X_) 
        self.rmse_test = np.sqrt(mean_squared_error(self.y_test[self.channel], self.y_pred))
        
        
        return self.y_pred, self.rmse_test       
                 
    
    def loss(self):
        print('RMSE_train= {:.2f}'.format(self.rmse_train))
        print('RMSE_test= {:.2f}'.format(self.rmse_test))
              
    
                    
    def coef(self):
        print(self.poly.get_feature_names())
        print('Coefficient=', self.coeff)
        print('Intercept=', self.intercept)
        return self.intercept, self.coeff
                
        
    def plot(self):  
        filename = 'T={}~{}_H={}~{}_{} (RMSE y_pred_scale= {:.2f})'.format(self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound, self.channel, self.rmse_test ) 
        df_result = pd.DataFrame()
        df_result['y_true'] = self.y_test[self.channel]
        df_result['y_pred'] = self.y_pred
#         df_result['y_pred_scale'] = self.y_pred_scale
#         df_result['y_pred_scale_buffer'] = self.y_buffer
        df_result['Humidity'] = self.x_test['Humidity']
        df_result.iplot(y=['y_true', 'y_pred'], 
                        kind='scatter', 
                        yTitle='ppm', 
                        title=filename)

              
        # save prediction result        
        plt.plot(df_result['y_true'])
        plt.plot(df_result['y_pred'])
#         plt.plot(df_result['y_pred_scale'])
        plt.ylabel('white card')
        plt.grid(alpha=0.3)
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),  loc=3, ncol=3, mode="expand")
        plt.title(filename, y=1.15, fontsize=10)
        plt.savefig(self.savePath + '/{}_'.format(self.sensor_number) + filename + '.png', dpi=200, bbox_inches='tight')
        plt.close() 
        # plt.show()
        
    
