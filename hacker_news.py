#Reading in modules used
import urllib.request as request
import json
import numpy as np
import pandas as pd
import webbrowser
from datetime import datetime







def extract_story( art_num ):
    '''
    Purpose: Extracts details on item number (if it is a HN story)
    Output: Metadata on article (JSON/dict)
    '''
    temp_url = 'https://hacker-news.firebaseio.com/v0/item/' + str( art_num ) + '.json?print=pretty'
    response = request.urlopen( temp_url )
    data = json.loads( response.read().decode('utf8') )
    if data[ 'type' ] != 'story':
        print( 'Item Number Not Story' )
    else:
        for i in [ 'title', 'url', 'score', 'time' ]:
            print( str( i ) + ': ' + str( data[ i ] ) )
        return( data )







def extract_recent( num_articles = 10 ):
    '''
    Purpose: Extracts num_articles most recent HN stories
    Input: Number of stories to be extracted
    Output: Dataframe with metadata of most recent stories

    Warning: Code takes a long time to run since HN has a lot of comments that are parsed as well
    '''
    most_recent = 'https://hacker-news.firebaseio.com/v0/maxitem.json?print=pretty'
    response = request.urlopen( most_recent )
    data = json.loads( response.read().decode('utf8') )
    title_list = list()
    url_list = list()
    score_list = list()
    time_list = list()
    counter = 0
    while len( title_list ) < num_articles:
        print( 'Story Count: ' + str( counter ), end = '\r', flush = True )
        temp_url = 'https://hacker-news.firebaseio.com/v0/item/' + str( data ) + '.json?print=pretty'
        response = request.urlopen( temp_url )
        out = json.loads( response.read().decode('utf8') )
        data = data - 1
        if 'type' in out.keys():
            if out[ 'type' ] == 'story':
                try:
                    title = out[ 'title' ]
                    url = out[ 'url' ] 
                    score = out[ 'score' ]
                    try:
                        time = datetime.utcfromtimestamp( out[ 'time' ] ).strftime('%Y-%m-%d %H:%M:%S')
                    except:
                        time = 'N/A'
                    text_store.append( title )
                    url_store.append( url )
                    score_store.append( score )
                    time_store.append( time )
                    counter = counter + 1
                except:
                    pass
            else:
                pass
        else:
            pass
    df_out = pd.DataFrame( { 'Title':text_store, 'URL':url_store, 'Score':score_store, 'Time':time_store } ) 
    return( df_out )







def extract_all_hn():
    '''
    Purpose: Extracts newest, top and best HN stories
    Input: None
    Output: Dataframes with metadata on the newest, top and best HN stories
    '''

    #############################################
    ############# Getting new stories ###########
    #############################################

    print( 'Extracting Newest Stories' )
    response = request.urlopen( 'https://hacker-news.firebaseio.com/v0/newstories.json?print=pretty' )
    new_stor = json.loads(response.read().decode('utf8'))

    text_store = list()
    url_store = list()
    score_store = list()
    time_store = list()

    for i in new_stor:
        temp_url = 'https://hacker-news.firebaseio.com/v0/item/' + str( i ) + '.json?print=pretty'
        response = request.urlopen( temp_url )
        data = json.loads( response.read().decode('utf8') )
        try:
            title = data[ 'title' ]
            url = data[ 'url' ] 
            score = data[ 'score' ]
            try:
                time = datetime.utcfromtimestamp( data[ 'time' ] ).strftime('%Y-%m-%d %H:%M:%S')
            except:
                time = 'N/A'
            text_store.append( title )
            url_store.append( url )
            score_store.append( score )
            time_store.append( time )
        except:
            pass

    #Saving as dataframe
    df_new = pd.DataFrame( { 'Title':text_store, 'URL':url_store, 'Score':score_store, 'Time':time_store } ) 
    df_new = df_new.sort_values( by = 'Score', ascending = False ).reset_index( drop = True )
    df_new[ 'category' ] = 'new'

    #############################################
    ############# Getting top stories ###########
    #############################################

    print( 'Extracting Top Stories' )
    response = request.urlopen( 'https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty' )
    top_stor = json.loads(response.read().decode('utf8'))

    text_store = list()
    url_store = list()
    score_store = list()
    time_store = list()

    for i in top_stor:
        temp_url = 'https://hacker-news.firebaseio.com/v0/item/' + str( i ) + '.json?print=pretty'
        response = request.urlopen( temp_url )
        data = json.loads( response.read().decode('utf8') )
        try:
            title = data[ 'title' ]
            url = data[ 'url' ] 
            score = data[ 'score' ]
            try:
                time = datetime.utcfromtimestamp( data[ 'time' ] ).strftime('%Y-%m-%d %H:%M:%S')
            except:
                time = 'N/A'
            text_store.append( title )
            url_store.append( url )
            score_store.append( score )
            time_store.append( time )
        except:
            pass

    #Saving as dataframe
    df_top = pd.DataFrame( { 'Title':text_store, 'URL':url_store, 'Score':score_store, 'Time':time_store } ) 
    df_top = df_top.sort_values( by = 'Score', ascending = False ).reset_index( drop = True )
    df_top[ 'category' ] = 'top'

    #############################################
    ############ Getting best stories ###########
    #############################################

    print( 'Extracting Best Stories' )
    response = request.urlopen( 'https://hacker-news.firebaseio.com/v0/beststories.json?print=pretty' )
    best_stor = json.loads(response.read().decode('utf8'))

    text_store = list()
    url_store = list()
    score_store = list()
    time_store = list()

    for i in best_stor:
        temp_url = 'https://hacker-news.firebaseio.com/v0/item/' + str( i ) + '.json?print=pretty'
        response = request.urlopen( temp_url )
        data = json.loads( response.read().decode('utf8') )
        try:
            title = data[ 'title' ]
            url = data[ 'url' ] 
            score = data[ 'score' ]
            try:
                time = datetime.utcfromtimestamp( data[ 'time' ] ).strftime('%Y-%m-%d %H:%M:%S')
            except:
                time = 'N/A'
            text_store.append( title )
            url_store.append( url )
            score_store.append( score )
            time_store.append( time )
        except:
            pass

    #Saving as dataframe
    df_best = pd.DataFrame( { 'Title':text_store, 'URL':url_store, 'Score':score_store, 'Time':time_store } ) 
    df_best = df_best.sort_values( by = 'Score', ascending = False ).reset_index( drop = True )
    df_best[ 'category' ] = 'best'

    #############################################
    ########### Compiling all frames ############
    #############################################
    
    print( 'Compiling Results' )
    df_all = pd.concat( [ df_best, df_top, df_new ], ignore_index=True )
    df_all.drop_duplicates( subset = 'URL', keep = 'first', inplace = True )
    df_all = df_all.sort_values( by = 'Score', ascending = False ).reset_index( drop = True )

    #############################################
    ############# Returning Results #############
    #############################################

    return( df_best, df_top, df_new, df_all )







def save_all_hn( output_title = 'hn_articles' ):
    '''
    Purpose: Saves newest, top and best HN stories to Excel sheet
    Input: Filename for destination spreadsheet (optional)
    Output: Saves spreadsheet with story metadata
    '''

    print( 'Beginning HN Extraction' )
    df_best, df_top, df_new, df_all = extract_all_hn()
    df_best[ 'Status' ] = np.nan
    df_top[ 'Status' ] = np.nan
    df_new[ 'Status' ] = np.nan
    df_all[ 'Status' ] = np.nan
    df_best = df_best[[ 'Status', 'Title', 'URL', 'Score', 'Time' ]]
    df_top = df_top[[ 'Status', 'Title', 'URL', 'Score', 'Time' ]]
    df_new = df_new[[ 'Status', 'Title', 'URL', 'Score', 'Time' ]]
    df_all = df_all[[ 'Status', 'Title', 'URL', 'Score', 'Time' ]]

    print( 'Generating Spreadsheet' )
    #Creating writer to save data
    writer = pd.ExcelWriter( output_title + '.xlsx', engine='xlsxwriter' )

    #Write each dataframe to a different worksheet.
    df_best.to_excel( writer, sheet_name='best', index = False )
    df_top.to_excel( writer, sheet_name='top', index = False )
    df_new.to_excel( writer, sheet_name='new', index = False )
    df_all.to_excel( writer, sheet_name = 'all', index = False )

    #Saving formats for use
    workbook  = writer.book
    #cell_format = workbook.add_format( { 'bg_color': '#D6D4CA', 'font_color':':#5F4B32' } )
    cell_format = workbook.add_format( { 'bg_color': '#FBF0D9', 'font_color':'#574A2A' } )
    col_format = workbook.add_format( { 'valign':'vcenter', 'align':'left', 'font_size':28, 'font_name':'Times New Roman' } )

    #Implementing format for each sheet
    #Note due to bug in pd.to_excel(), the header column is formatted, and the URLs are not either
    for i in [ 'best', 'top', 'new', 'all' ]:
        worksheet = writer.sheets[ i ]
        worksheet.set_column( 0, 1, 10, cell_format = col_format )
        worksheet.set_column( 1, 100, 250, cell_format = col_format )
        worksheet.set_default_row( 100 )
        worksheet.conditional_format( 'A1:XFD1048576', { 'type': 'cell',
                                                    'criteria':'!=',
                                                    'value': 3000000000000,
                                                    'format':cell_format } )


    # Close the Pandas Excel writer and output the Excel file.
    print( 'Saving to Excel' )
    writer.save()







def open_hn_web( input_sheet = 'hn_articles.xlsx', input_tab = 'all' ):
    '''
    Purpose: Opens all marked (Status = 1) articles from Excel sheet returned in function above in default browser
    Input: Name of input Excel workbook, name of input tab/sheet (defaults to 'all')
    Output: N/A (Tabs opened in default browser)
    '''

    #Reading in Data
    df = pd.read_excel( input_sheet, input_tab )
    df = df[ df.Status == 1 ].reset_index( drop = True )

    first_url = df.URL[ 0 ]
    webbrowser.open( first_url, new=1 )

    url_list = df.URL[ 1: ]
    for i in url_list:
        webbrowser.open( i, new=2 )











