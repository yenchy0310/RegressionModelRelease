import matplotlib.pyplot as plt
      
    
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
        
