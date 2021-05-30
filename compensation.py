import matplotlib.pyplot as plt

def compensation_online_test(data, coef, phage_side, white_card_side):
    '''Using white card to compensate phage shift
    phage_side: int 1 or 2 (AMS1:1, AMS2:2)
    white_card_side: int 1 or 2 (AMS1:1, AMS2:2)'''
        
    channel_list = ['410nm', '440nm', '470nm', '510nm', '550nm', '583nm', '620nm', '670nm' , '900nm']
    
    for channel in channel_list:
        
        # phage compensation
        data['{} #{}_comp'.format(channel, phage_side)] = data['{} #{}'.format(channel, phage_side)]* (coef['{} #{}'.format(channel, white_card_side)][1][0]/data['{} #{}'.format(channel, white_card_side)])
        
        # white card compensation
        data['{} #{}_comp'.format(channel, white_card_side)] = data['{} #{}'.format(channel, white_card_side)]* (coef['{} #{}'.format(channel, white_card_side)][1][0]/data['{} #{}'.format(channel, white_card_side)])
        
         # phage_mv compensation
        data['{} #{}_mv_comp'.format(channel, phage_side)] = data['{} #{}_mv'.format(channel, phage_side)]* (coef['{} #{}_mv'.format(channel, white_card_side)][1][0]/data['{} #{}_mv'.format(channel, white_card_side)])
        
        # white card_mv compensation       
        data['{} #{}_mv_comp'.format(channel, white_card_side)] = data['{} #{}_mv'.format(channel, white_card_side)]* (coef['{} #{}_mv'.format(channel, white_card_side)][1][0]/data['{} #{}_mv'.format(channel, white_card_side)])
        
def compensation_670nm_white_card_model(data, phage_side, white_card_side):
    
    '''only for 670nm compensation
    phage_side: int 1 or 2 (AMS1:1, AMS2:2)
    white_card_side: int 1 or 2 (AMS1:1, AMS2:2)'''     
   
   
    # phage compensation
    data['670nm #{}_comp'.format(phage_side)] = data['670nm #{}'.format(phage_side)]* (data['white card std']/data['670nm #{}'.format(white_card_side)])

    # white card compensation
    data['670nm #{}_comp'.format(white_card_side)] = data['670nm #{}'.format(white_card_side)]* (data['white card std']/data['670nm #{}'.format(white_card_side)])

    # phage_mv compensation
    data['670nm #{}_mv_comp'.format(phage_side)] = data['670nm #{}_mv'.format(phage_side)]* (data['white card std']/data['670nm #{}_mv'.format(white_card_side)])

    # white card_mv compensation       
    data['670nm #{}_mv_comp'.format(white_card_side)] = data['670nm #{}_mv'.format(white_card_side)]* (data['white card std']/data['670nm #{}_mv'.format(white_card_side)])    
    
def compensation_AS7341(data, white_card_std, phage_side, white_card_side):
    
    '''Using white card to compensate phage shift
    phage_side: int 1 or 2 (AMS1:1, AMS2:2)
    white_card_side: int 1 or 2 (AMS1:1, AMS2:2)'''
        
    channel_list = ['410nm', '440nm', '470nm', '510nm', '550nm', '583nm', '620nm', '670nm' , '900nm']
    
    for channel in channel_list:
        # phage compensation
        data['{} #{}_comp'.format(channel, phage_side)] = data['{} #{}'.format(channel, phage_side)]* (white_card_std['{} #{}'.format(channel, white_card_side)][0]/data['{} #{}'.format(channel, white_card_side)])
        
        # white card compensation
        data['{} #{}_comp'.format(channel, white_card_side)] = data['{} #{}'.format(channel, white_card_side)]* (white_card_std['{} #{}'.format(channel, white_card_side)][0]/data['{} #{}'.format(channel, white_card_side)])
        
        # phage_mv compensation
        data['{} #{}_mv_comp'.format(channel, phage_side)] = data['{} #{}_mv'.format(channel, phage_side)]* (white_card_std['{} #{}_mv'.format(channel, white_card_side)][0]/data['{} #{}_mv'.format(channel, white_card_side)])
        
        # white card_mv compensation       
        data['{} #{}_mv_comp'.format(channel, white_card_side)] = data['{} #{}_mv'.format(channel, white_card_side)]* (white_card_std['{} #{}_mv'.format(channel, white_card_side)][0]/data['{} #{}_mv'.format(channel, white_card_side)])
        
# def compensation_online_test(data, coef):

#     '''Using white card to compensate phage shift'''       
   
#     data['410nm #1_comp'] = data['410nm #1']* (coef[1][0]/data['410nm #2'])
#     data['440nm #1_comp'] = data['440nm #1']* (coef[1][0]/data['440nm #2'])
#     data['470nm #1_comp'] = data['470nm #1']* (coef[1][0]/data['470nm #2'])
#     data['510nm #1_comp'] = data['510nm #1']* (coef[1][0]/data['510nm #2'])    
#     data['550nm #1_comp'] = data['550nm #1']* (coef[1][0]/data['550nm #2'])
#     data['583nm #1_comp'] = data['583nm #1']* (coef[1][0]/data['583nm #2'])
#     data['620nm #1_comp'] = data['620nm #1']* (coef[1][0]/data['620nm #2'])
#     data['670nm #1_comp'] = data['670nm #1']* (coef[1][0]/data['670nm #2'])
#     data['900nm #1_comp'] = data['900nm #1']* (coef[1][0]/data['900nm #2'])
    
#     data['410nm #2_comp'] = data['410nm #2']* (coef[1][0]/data['410nm #2'])
#     data['440nm #2_comp'] = data['440nm #2']* (coef[1][0]/data['440nm #2'])
#     data['470nm #2_comp'] = data['470nm #2']* (coef[1][0]/data['470nm #2'])
#     data['510nm #2_comp'] = data['510nm #2']* (coef[1][0]/data['510nm #2'])    
#     data['550nm #2_comp'] = data['550nm #2']* (coef[1][0]/data['550nm #2'])
#     data['583nm #2_comp'] = data['583nm #2']* (coef[1][0]/data['583nm #2'])
#     data['620nm #2_comp'] = data['620nm #2']* (coef[1][0]/data['620nm #2'])
#     data['670nm #2_comp'] = data['670nm #2']* (coef[1][0]/data['670nm #2'])
#     data['900nm #2_comp'] = data['900nm #2']* (coef[1][0]/data['900nm #2'])
    
#     data['410nm #1_mv_comp'] = data['410nm #1_mv']* (coef[1][0]/data['410nm #2_mv'])
#     data['440nm #1_mv_comp'] = data['440nm #1_mv']* (coef[1][0]/data['440nm #2_mv'])
#     data['470nm #1_mv_comp'] = data['470nm #1_mv']* (coef[1][0]/data['470nm #2_mv'])
#     data['510nm #1_mv_comp'] = data['510nm #1_mv']* (coef[1][0]/data['510nm #2_mv'])    
#     data['550nm #1_mv_comp'] = data['550nm #1_mv']* (coef[1][0]/data['550nm #2_mv'])
#     data['583nm #1_mv_comp'] = data['583nm #1_mv']* (coef[1][0]/data['583nm #2_mv'])
#     data['620nm #1_mv_comp'] = data['620nm #1_mv']* (coef[1][0]/data['620nm #2_mv'])
#     data['670nm #1_mv_comp'] = data['670nm #1_mv']* (coef[1][0]/data['670nm #2_mv'])
#     data['900nm #1_mv_comp'] = data['900nm #1_mv']* (coef[1][0]/data['900nm #2_mv'])
    
#     data['410nm #2_mv_comp'] = data['410nm #2_mv']* (coef[1][0]/data['410nm #2_mv'])
#     data['440nm #2_mv_comp'] = data['440nm #2_mv']* (coef[1][0]/data['440nm #2_mv'])
#     data['470nm #2_mv_comp'] = data['470nm #2_mv']* (coef[1][0]/data['470nm #2_mv'])
#     data['510nm #2_mv_comp'] = data['510nm #2_mv']* (coef[1][0]/data['510nm #2_mv'])    
#     data['550nm #2_mv_comp'] = data['550nm #2_mv']* (coef[1][0]/data['550nm #2_mv'])
#     data['583nm #2_mv_comp'] = data['583nm #2_mv']* (coef[1][0]/data['583nm #2_mv'])
#     data['620nm #2_mv_comp'] = data['620nm #2_mv']* (coef[1][0]/data['620nm #2_mv'])
#     data['670nm #2_mv_comp'] = data['670nm #2_mv']* (coef[1][0]/data['670nm #2_mv'])
#     data['900nm #2_mv_comp'] = data['900nm #2_mv']* (coef[1][0]/data['900nm #2_mv'])
    
# def compensation_AS7341(data, white_card_std, phage_side, white_card_side):

#     '''Using white card to compensate phage shift
#     phage_side: int 1 or 2 (AMS1:1, AMS2:2)
#     white_card_side: int 1 or 2 (AMS1:1, AMS2:2)'''
        
#     data['410nm #{}_comp'.format(phage_side)] = data['410nm #{}'.format(phage_side)]* (white_card_std['410nm #{}'.format(white_card_side)][0]/data['410nm #{}'.format(white_card_side)])
#     data['440nm #{}_comp'.format(phage_side)] = data['440nm #{}'.format(phage_side)]* (white_card_std['440nm #{}'.format(white_card_side)][0]/data['440nm #{}'.format(white_card_side)])
#     data['470nm #{}_comp'.format(phage_side)] = data['470nm #{}'.format(phage_side)]* (white_card_std['470nm #{}'.format(white_card_side)][0]/data['470nm #{}'.format(white_card_side)])
#     data['510nm #{}_comp'.format(phage_side)] = data['510nm #{}'.format(phage_side)]* (white_card_std['510nm #{}'.format(white_card_side)][0]/data['510nm #{}'.format(white_card_side)])    
#     data['550nm #{}_comp'.format(phage_side)] = data['550nm #{}'.format(phage_side)]* (white_card_std['550nm #{}'.format(white_card_side)][0]/data['550nm #{}'.format(white_card_side)])
#     data['583nm #{}_comp'.format(phage_side)] = data['583nm #{}'.format(phage_side)]* (white_card_std['583nm #{}'.format(white_card_side)][0]/data['583nm #{}'.format(white_card_side)])
#     data['620nm #{}_comp'.format(phage_side)] = data['620nm #{}'.format(phage_side)]* (white_card_std['620nm #{}'.format(white_card_side)][0]/data['620nm #{}'.format(white_card_side)])
#     data['670nm #{}_comp'.format(phage_side)] = data['670nm #{}'.format(phage_side)]* (white_card_std['670nm #{}'.format(white_card_side)][0]/data['670nm #{}'.format(white_card_side)])
#     data['900nm #{}_comp'.format(phage_side)] = data['900nm #{}'.format(phage_side)]* (white_card_std['900nm #{}'.format(white_card_side)][0]/data['900nm #{}'.format(white_card_side)])
    
#     data['410nm #{}_comp'.format(white_card_side)] = data['410nm #{}'.format(white_card_side)]* (white_card_std['410nm #{}'.format(white_card_side)][0]/data['410nm #{}'.format(white_card_side)])
#     data['440nm #{}_comp'.format(white_card_side)] = data['440nm #{}'.format(white_card_side)]* (white_card_std['440nm #{}'.format(white_card_side)][0]/data['440nm #{}'.format(white_card_side)])
#     data['470nm #{}_comp'.format(white_card_side)] = data['470nm #{}'.format(white_card_side)]* (white_card_std['470nm #{}'.format(white_card_side)][0]/data['470nm #{}'.format(white_card_side)])
#     data['510nm #{}_comp'.format(white_card_side)] = data['510nm #{}'.format(white_card_side)]* (white_card_std['510nm #{}'.format(white_card_side)][0]/data['510nm #{}'.format(white_card_side)])    
#     data['550nm #{}_comp'.format(white_card_side)] = data['550nm #{}'.format(white_card_side)]* (white_card_std['550nm #{}'.format(white_card_side)][0]/data['550nm #{}'.format(white_card_side)])
#     data['583nm #{}_comp'.format(white_card_side)] = data['583nm #{}'.format(white_card_side)]* (white_card_std['583nm #{}'.format(white_card_side)][0]/data['583nm #{}'.format(white_card_side)])
#     data['620nm #{}_comp'.format(white_card_side)] = data['620nm #{}'.format(white_card_side)]* (white_card_std['620nm #{}'.format(white_card_side)][0]/data['620nm #{}'.format(white_card_side)])
#     data['670nm #{}_comp'.format(white_card_side)] = data['670nm #{}'.format(white_card_side)]* (white_card_std['670nm #{}'.format(white_card_side)][0]/data['670nm #{}'.format(white_card_side)])
#     data['900nm #{}_comp'.format(white_card_side)] = data['900nm #{}'.format(white_card_side)]* (white_card_std['900nm #{}'.format(white_card_side)][0]/data['900nm #{}'.format(white_card_side)])
    
#     data['410nm #{}_mv_comp'.format(phage_side)] = data['410nm #{}_mv'.format(phage_side)]* (white_card_std['410nm #{}_mv'.format(white_card_side)][0]/data['410nm #{}_mv'.format(white_card_side)])
#     data['440nm #{}_mv_comp'.format(phage_side)] = data['440nm #{}_mv'.format(phage_side)]* (white_card_std['440nm #{}_mv'.format(white_card_side)][0]/data['440nm #{}_mv'.format(white_card_side)])
#     data['470nm #{}_mv_comp'.format(phage_side)] = data['470nm #{}_mv'.format(phage_side)]* (white_card_std['470nm #{}_mv'.format(white_card_side)][0]/data['470nm #{}_mv'.format(white_card_side)])
#     data['510nm #{}_mv_comp'.format(phage_side)] = data['510nm #{}_mv'.format(phage_side)]* (white_card_std['510nm #{}_mv'.format(white_card_side)][0]/data['510nm #{}_mv'.format(white_card_side)])    
#     data['550nm #{}_mv_comp'.format(phage_side)] = data['550nm #{}_mv'.format(phage_side)]* (white_card_std['550nm #{}_mv'.format(white_card_side)][0]/data['550nm #{}_mv'.format(white_card_side)])
#     data['583nm #{}_mv_comp'.format(phage_side)] = data['583nm #{}_mv'.format(phage_side)]* (white_card_std['583nm #{}_mv'.format(white_card_side)][0]/data['583nm #{}_mv'.format(white_card_side)])
#     data['620nm #{}_mv_comp'.format(phage_side)] = data['620nm #{}_mv'.format(phage_side)]* (white_card_std['620nm #{}_mv'.format(white_card_side)][0]/data['620nm #{}_mv'.format(white_card_side)])
#     data['670nm #{}_mv_comp'.format(phage_side)] = data['670nm #{}_mv'.format(phage_side)]* (white_card_std['670nm #{}_mv'.format(white_card_side)][0]/data['670nm #{}_mv'.format(white_card_side)])
#     data['900nm #{}_mv_comp'.format(phage_side)] = data['900nm #{}_mv'.format(phage_side)]* (white_card_std['900nm #{}_mv'.format(white_card_side)][0]/data['900nm #{}_mv'.format(white_card_side)])
    
#     data['410nm #{}_mv_comp'.format(white_card_side)] = data['410nm #{}_mv'.format(white_card_side)]* (white_card_std['410nm #{}_mv'.format(white_card_side)][0]/data['410nm #{}_mv'.format(white_card_side)])
#     data['440nm #{}_mv_comp'.format(white_card_side)] = data['440nm #{}_mv'.format(white_card_side)]* (white_card_std['440nm #{}_mv'.format(white_card_side)][0]/data['440nm #{}_mv'.format(white_card_side)])
#     data['470nm #{}_mv_comp'.format(white_card_side)] = data['470nm #{}_mv'.format(white_card_side)]* (white_card_std['470nm #{}_mv'.format(white_card_side)][0]/data['470nm #{}_mv'.format(white_card_side)])
#     data['510nm #{}_mv_comp'.format(white_card_side)] = data['510nm #{}_mv'.format(white_card_side)]* (white_card_std['510nm #{}_mv'.format(white_card_side)][0]/data['510nm #{}_mv'.format(white_card_side)])    
#     data['550nm #{}_mv_comp'.format(white_card_side)] = data['550nm #{}_mv'.format(white_card_side)]* (white_card_std['550nm #{}_mv'.format(white_card_side)][0]/data['550nm #{}_mv'.format(white_card_side)])
#     data['583nm #{}_mv_comp'.format(white_card_side)] = data['583nm #{}_mv'.format(white_card_side)]* (white_card_std['583nm #{}_mv'.format(white_card_side)][0]/data['583nm #{}_mv'.format(white_card_side)])
#     data['620nm #{}_mv_comp'.format(white_card_side)] = data['620nm #{}_mv'.format(white_card_side)]* (white_card_std['620nm #{}_mv'.format(white_card_side)][0]/data['620nm #{}_mv'.format(white_card_side)])
#     data['670nm #{}_mv_comp'.format(white_card_side)] = data['670nm #{}_mv'.format(white_card_side)]* (white_card_std['670nm #{}_mv'.format(white_card_side)][0]/data['670nm #{}_mv'.format(white_card_side)])
#     data['900nm #{}_mv_comp'.format(white_card_side)] = data['900nm #{}_mv'.format(white_card_side)]* (white_card_std['900nm #{}_mv'.format(white_card_side)][0]/data['900nm #{}_mv'.format(white_card_side)])
        

# def compensation_AS7341(data, white_card_std):

#     '''Using white card to compensate phage shift'''
        
#     data['410nm #1_comp'] = data['410nm #1']* (white_card_std['410nm #2'][0]/data['410nm #2'])
#     data['440nm #1_comp'] = data['440nm #1']* (white_card_std['440nm #2'][0]/data['440nm #2'])
#     data['470nm #1_comp'] = data['470nm #1']* (white_card_std['470nm #2'][0]/data['470nm #2'])
#     data['510nm #1_comp'] = data['510nm #1']* (white_card_std['510nm #2'][0]/data['510nm #2'])    
#     data['550nm #1_comp'] = data['550nm #1']* (white_card_std['550nm #2'][0]/data['550nm #2'])
#     data['583nm #1_comp'] = data['583nm #1']* (white_card_std['583nm #2'][0]/data['583nm #2'])
#     data['620nm #1_comp'] = data['620nm #1']* (white_card_std['620nm #2'][0]/data['620nm #2'])
#     data['670nm #1_comp'] = data['670nm #1']* (white_card_std['670nm #2'][0]/data['670nm #2'])
#     data['900nm #1_comp'] = data['900nm #1']* (white_card_std['900nm #2'][0]/data['900nm #2'])
    
#     data['410nm #2_comp'] = data['410nm #2']* (white_card_std['410nm #2'][0]/data['410nm #2'])
#     data['440nm #2_comp'] = data['440nm #2']* (white_card_std['440nm #2'][0]/data['440nm #2'])
#     data['470nm #2_comp'] = data['470nm #2']* (white_card_std['470nm #2'][0]/data['470nm #2'])
#     data['510nm #2_comp'] = data['510nm #2']* (white_card_std['510nm #2'][0]/data['510nm #2'])    
#     data['550nm #2_comp'] = data['550nm #2']* (white_card_std['550nm #2'][0]/data['550nm #2'])
#     data['583nm #2_comp'] = data['583nm #2']* (white_card_std['583nm #2'][0]/data['583nm #2'])
#     data['620nm #2_comp'] = data['620nm #2']* (white_card_std['620nm #2'][0]/data['620nm #2'])
#     data['670nm #2_comp'] = data['670nm #2']* (white_card_std['670nm #2'][0]/data['670nm #2'])
#     data['900nm #2_comp'] = data['900nm #2']* (white_card_std['900nm #2'][0]/data['900nm #2'])
    
#     data['410nm #1_mv_comp'] = data['410nm #1_mv']* (white_card_std['410nm #2_mv'][0]/data['410nm #2_mv'])
#     data['440nm #1_mv_comp'] = data['440nm #1_mv']* (white_card_std['440nm #2_mv'][0]/data['440nm #2_mv'])
#     data['470nm #1_mv_comp'] = data['470nm #1_mv']* (white_card_std['470nm #2_mv'][0]/data['470nm #2_mv'])
#     data['510nm #1_mv_comp'] = data['510nm #1_mv']* (white_card_std['510nm #2_mv'][0]/data['510nm #2_mv'])    
#     data['550nm #1_mv_comp'] = data['550nm #1_mv']* (white_card_std['550nm #2_mv'][0]/data['550nm #2_mv'])
#     data['583nm #1_mv_comp'] = data['583nm #1_mv']* (white_card_std['583nm #2_mv'][0]/data['583nm #2_mv'])
#     data['620nm #1_mv_comp'] = data['620nm #1_mv']* (white_card_std['620nm #2_mv'][0]/data['620nm #2_mv'])
#     data['670nm #1_mv_comp'] = data['670nm #1_mv']* (white_card_std['670nm #2_mv'][0]/data['670nm #2_mv'])
#     data['900nm #1_mv_comp'] = data['900nm #1_mv']* (white_card_std['900nm #2_mv'][0]/data['900nm #2_mv'])
    
#     data['410nm #2_mv_comp'] = data['410nm #2_mv']* (white_card_std['410nm #2_mv'][0]/data['410nm #2_mv'])
#     data['440nm #2_mv_comp'] = data['440nm #2_mv']* (white_card_std['440nm #2_mv'][0]/data['440nm #2_mv'])
#     data['470nm #2_mv_comp'] = data['470nm #2_mv']* (white_card_std['470nm #2_mv'][0]/data['470nm #2_mv'])
#     data['510nm #2_mv_comp'] = data['510nm #2_mv']* (white_card_std['510nm #2_mv'][0]/data['510nm #2_mv'])    
#     data['550nm #2_mv_comp'] = data['550nm #2_mv']* (white_card_std['550nm #2_mv'][0]/data['550nm #2_mv'])
#     data['583nm #2_mv_comp'] = data['583nm #2_mv']* (white_card_std['583nm #2_mv'][0]/data['583nm #2_mv'])
#     data['620nm #2_mv_comp'] = data['620nm #2_mv']* (white_card_std['620nm #2_mv'][0]/data['620nm #2_mv'])
#     data['670nm #2_mv_comp'] = data['670nm #2_mv']* (white_card_std['670nm #2_mv'][0]/data['670nm #2_mv'])
#     data['900nm #2_mv_comp'] = data['900nm #2_mv']* (white_card_std['900nm #2_mv'][0]/data['900nm #2_mv'])

def plot(df_1, df_2, channel):
    start = 0
    end = 40
    fig, axs = plt.subplots(1, 4, figsize=(20,5))
    
    axs[0].set_title(channel + ' phage')
    axs[0].scatter(list(range(0,(end-start))), df_1['{} #1'.format(channel)][start:end])
    axs[0].scatter(list(range(0,(end-start))), df_2['{} #1'.format(channel)][start:end])
        
    axs[1].set_title('white card')
    axs[1].scatter(list(range(0,(end-start))), df_1['{} #2'.format(channel)][start:end])
    axs[1].scatter(list(range(0,(end-start))), df_2['{} #2'.format(channel)][start:end])
    
    axs[2].set_title('phage compensation')
    axs[2].scatter(list(range(0,(end-start))), df_1['{} #1_comp'.format(channel)][start:end])
    axs[2].scatter(list(range(0,(end-start))), df_2['{} #1_comp'.format(channel)][start:end])
    difference = df_2['{} #1_comp'.format(channel)][0:100].mean()-df_1['{} #1_comp'.format(channel)][0:100].mean()
    print('{} shift amount'.format(channel), '{:.2f}'.format(difference))
    
    
    axs[3].set_title('white card compensation')
    axs[3].scatter(list(range(0,(end-start))), df_1['{} #2_comp'.format(channel)][start:end], label='df_1')
    axs[3].scatter(list(range(0,(end-start))), df_2['{} #2_comp'.format(channel)][start:end], label='df_2')
    axs[3].legend()