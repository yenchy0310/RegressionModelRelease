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
        
    
def compensation_AS7341(data, phage_side, white_card_side, compChannel):
    
    '''Using white card to compensate phage shift
    phage_side: int 1 or 2 (AMS1:1, AMS2:2)
    white_card_side: int 1 or 2 (AMS1:1, AMS2:2)''' 
    
    channel = compChannel.split()[0]
  
        # phage compensation
    data['{} #{}_comp'.format(channel, phage_side)] = data['{} #{}'.format(channel, phage_side)]* (data['white card std']/data['{} #{}'.format(channel, white_card_side)])

    # white card compensation
    data['{} #{}_comp'.format(channel, white_card_side)] = data['{} #{}'.format(channel, white_card_side)]* (data['white card std']/data['{} #{}'.format(channel, white_card_side)])

    # phage_mv compensation
    data['{} #{}_mv_comp'.format(channel, phage_side)] = data['{} #{}_mv'.format(channel, phage_side)]* (data['white card std']/data['{} #{}_mv'.format(channel, white_card_side)])

    # white card_mv compensation       
    data['{} #{}_mv_comp'.format(channel, white_card_side)] = data['{} #{}_mv'.format(channel, white_card_side)]* (data['white card std']/data['{} #{}_mv'.format(channel, white_card_side)])       

def constant_compensation_AS7341(data, white_card_std, phage_side, white_card_side):
    
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