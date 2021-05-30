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

class modeling:
    '''channel: analysis channel (ex: 440nm #1_mv_comp)
       x_train: training data for model building
       y_train: ppm for model building
       x_test: testing data for model evaluation
       y_test: ppm for model        
       '''
    def __init__(self, name, sensor_number, channel, x_train, y_train, x_test, y_test, model_name, degree, step, white_card_std, white_card_std_multiple=1, output_modify=1, shift=0, white_card_side=1, multiple=1):
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
        self.step = step
        self.output_modify = output_modify
        self.white_card_std = white_card_std
        self.white_card_side = white_card_side
        self.white_card_std_multiple = white_card_std_multiple
        self.shift = shift
        self.multiple = multiple
        
        
        
    def regression(self):
        
        x = self.x_train[['Temperature','Humidity', self.channel]]
        X_ = self.x_test[['Temperature','Humidity', self.channel]]
      
        x = self.poly.fit_transform(x)
        X_ = self.poly.fit_transform(X_)

        # training set 
        model = self.model_name.fit(x, self.y_train)
        yfit = model.predict(x)
        self.coeff = model.coef_
        self.intercept = model.intercept_
        self.rmse_train = np.sqrt(mean_squared_error(self.y_train, yfit))
        
        # create a folder to store csv file
        self.folderName = '{}_degree={}'.format(self.name, self.degree)
        self.savePath = os.path.join(os.getcwd(), self.folderName)
        if not os.path.exists(self.savePath):
            os.makedirs(self.savePath)

#         (New format)create a csv to save coefficient and white card std value for each channel    
#         self.T_lower_bound = np.floor(self.x_train['Temperature'].min()) #取溫度下限
#         self.T_upper_bound = np.ceil(self.x_train['Temperature'].max()) #取溫度上限
#         self.H_lower_bound = np.floor(self.x_train['Humidity'].min()) #取濕度下限
#         self.H_upper_bound = np.ceil(self.x_train['Humidity'].max()) #取濕度上限
#         wavelength = self.channel.split(' ')[0]
#         white_card_std = self.white_card_std['{} #{}'.format(wavelength, self.white_card_side)][0]*self.white_card_std_multiple #白片STD值
        
#         coef_list = [self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound, self.degree, white_card_std, self.intercept]
#         for i in self.coeff:
#             coef_list.append(i)
        
#         df_coef = pd.DataFrame()        
#         df_coef['coefficient'] = coef_list #model coefficient  
#         df_coef.T.to_csv(self.savePath + '/{}_T={}~{}_H={}~{}_degree={}_{}_shift{}_ppmx{}.csv'.format(self.sensor_number, self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound,  self.degree, self.channel, self.shift, self.multiple), header=False, index=False)

        
        # (Old format vertical)create a csv to save coefficient and white card std value for each channel  
        self.T_lower_bound = np.floor(self.x_train['Temperature'].min()) #取溫度下限
        self.T_upper_bound = np.ceil(self.x_train['Temperature'].max()) #取溫度上限
        self.H_lower_bound = np.floor(self.x_train['Humidity'].min()) #取濕度下限
        self.H_upper_bound = np.ceil(self.x_train['Humidity'].max()) #取濕度上限
        wavelength = self.channel.split(' ')[0]
        
        
        df_coef = pd.DataFrame()
        df_coef['coefficient'] = np.insert(self.coeff, 0, self.intercept)
        wavelength = self.channel.split(' ')[0]
        df_coef['white_card_std'] = self.white_card_std['{} #{}'.format(wavelength, self.white_card_side)][0]
        df_coef.to_csv(self.savePath + '/{}_T={}~{}_H={}~{}_degree={}_{}_shift{}_ppmx{}.csv'.format(self.sensor_number, self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound,  self.degree, self.channel, self.shift, self.multiple), header=False, index=False)

        # testing set
        self.y_pred = model.predict(X_) * self.output_modify
        self.rmse_test = np.sqrt(mean_squared_error(self.y_test, self.y_pred))
        
        # scale range limit 0ppm
        self.y_pred_scale = self.y_pred.copy()
        for i,j in enumerate(self.y_pred):
            if j < 0:
                self.y_pred_scale[i]=0
            # elif j > 60:
            #     self.y_pred_scale[i]=60
            else:
                self.y_pred_scale[i]
        
        self.rmse_test_scale = np.sqrt(mean_squared_error(self.y_test, self.y_pred_scale))  

        return self.y_pred, self.rmse_test 


    def y_pred_scale_buffer(self, buffer):
        '''y_data: y_pred or y_pred_scale'''    

        buffer = buffer
        self.y_buffer = []
        
        if len(self.y_buffer) == 0:
            self.y_buffer.append(self.y_pred_scale[0])

        for i in range(1, len(self.y_pred_scale)):        
            diff = self.y_pred_scale[i] - self.y_buffer[i-1]
            if diff >= buffer:
                self.y_buffer.append(self.y_buffer[i-1]+buffer)
            elif diff <= -buffer:
                self.y_buffer.append(self.y_buffer[i-1]-buffer)
            else:
                self.y_buffer.append(self.y_pred_scale[i])
                
        return self.y_buffer          
                 
    
    def loss(self):
        print('RMSE_train= {:.2f}'.format(self.rmse_train))
        print('RMSE_test= {:.2f}'.format(self.rmse_test))
        # print('RMSE_test_scale= {:.2f}'.format(self.rmse_test_scale))

        
    def loss_each_step(self):
        self.each_step_data_point = int(len(self.y_test)/len(self.step))
        self.y_pred_step_base = self.y_pred.reshape(len(self.step), self.each_step_data_point)
        self.y_test_step_base = np.array(self.y_test).reshape(len(self.step), self.each_step_data_point)

        self.rmse_step_base = []
        for i, j in enumerate(self.step):
            rmse_step = np.sqrt(mean_squared_error(self.y_test_step_base[i], self.y_pred_step_base[i]))
            self.rmse_step_base.append(rmse_step)
            print('RMSE test {}{}{:.2f}'.format(j, ' ', rmse_step))

        return self.rmse_step_base
    
    '''Ignore RH30% prediction performance'''
    # def loss_noRH30(self):
    #     y_pred_noRH30 = self.y_pred[self.each_step_data_point:]
    #     y_test_noRH30 = self.y_test[self.each_step_data_point:]
    #     self.rmse_noRH30 = np.sqrt(mean_squared_error(y_pred_noRH30, y_test_noRH30))      
        
        
    def coef(self):
        print(self.poly.get_feature_names())
        print('Coefficient=', self.coeff)
        print('Intercept=', self.intercept)
        return self.intercept, self.coeff
                
        
    def plot(self):  
        filename = 'T={}~{}_H={}~{}_degree={}_{}_shift{}_ppmx{} (RMSE y_pred_scale= {:.2f})'.format(self.T_lower_bound, self.T_upper_bound, self.H_lower_bound, self.H_upper_bound,  self.degree, self.channel, self.shift, self.multiple, self.rmse_test ) 
        df_result = pd.DataFrame()
        df_result['y_true'] = self.y_test
        df_result['y_pred'] = self.y_pred
        df_result['y_pred_scale'] = self.y_pred_scale
        df_result['y_pred_scale_buffer'] = self.y_buffer
        df_result['Humidity'] = self.x_test['Humidity']
        df_result.iplot(y=['y_true', 'y_pred', 'y_pred_scale', 'y_pred_scale_buffer'], 
                        kind='scatter', 
                        yTitle='ppm', 
                        title=filename)

              
        # save prediction result        
        plt.plot(df_result['y_true'])
        plt.plot(df_result['y_pred'])
#         plt.plot(df_result['y_pred_scale'])
        plt.ylabel('ppm')
        plt.grid(alpha=0.3)
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102),  loc=3, ncol=3, mode="expand")
        plt.title(filename, y=1.15, fontsize=10)
        plt.savefig(self.savePath + '/{}_'.format(self.sensor_number) + filename + '.png', dpi=200, bbox_inches='tight')
        plt.close() 
        # plt.show()
        
    
