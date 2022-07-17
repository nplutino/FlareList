#================================ Import Section ==============================#
import PySimpleGUI as sg
import numpy as np
import pandas as pd

#================================ Functions ===================================#
def DataDownload(start,end):

    if start < '2003-01-01':
        df = pd.read_csv('https://raw.githubusercontent.com/nplutino/' \
        'FlareList/main/FlareList_1986-2002.csv',parse_dates=True)
        df = df[(df['tstart']>start)&(df['tstart']<end)]
    else:
        df = pd.DataFrame()
    if end > '2003-01-01':
        df2 = pd.read_csv('https://raw.githubusercontent.com/nplutino/' \
        'FlareList/main/FlareList_2003-2020.csv',parse_dates=True)
        df2 = df2[(df2['tstart']<end)&(df2['tstart']>start)]
    else:
        df2 = pd.DataFrame()
    return pd.concat([df,df2])

def DataVisualization(data):

    layout = [
    [sg.Table(values=data.values.tolist(), headings=data.columns.tolist(),
    max_col_width=35, auto_size_columns=True, display_row_numbers=False,
                    justification='right', num_rows=10, key='-TABLE-',
                    row_height=35)]
                    ]

    window = sg.Window("List of solar flares", layout)

    while True:
        event, values = window.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

    window.close()

def Avviso(testo):

    layout = [[sg.Text(testo,font=('Helvetica',15))],]
    window=sg.Window("Warning!",layout)

    while True:
        event,values = window.read()
        if event == sg.WIN_CLOSED:
            break

#================================ Theme Options ===============================#
sg.set_options(font=('Helvetica', 11))
sg.theme('Darkgrey')
positioning=(1300,500)

#================================ Buttons and Widgets =========================#
first_col = [

    [sg.Text('Solar Flare Catalog Download App',font=('Helvetica',20),pad=10)],
    [sg.Multiline('This tool can be used to request, visualize and download' \
    ' a list of solar flare events. These events have been registred starting' \
    ' from GOES soft-X solar signal (NASA) and using a new detection' \
    ' algorithm.', no_scrollbar=True,size=(45,4))],
    [sg.HSeparator(pad=20)],

    [sg.Text('Select a date range. Please notice that only data from' \
    ' 1986-2020 are available.', key='-TXT-')],

    [sg.Text('Start Date'), sg.Input(key='-START-', enable_events=True,
    default_text='(yyyy-mm-dd)', size=(20,1)),
    sg.CalendarButton('Select', target='-START-', format='%Y-%m-%d',
    close_when_date_chosen=False,begin_at_sunday_plus=1)],

    [sg.Text('End Date '), sg.Input(key='-END-', enable_events=True,
     default_text='(yyyy-mm-dd)', size=(20,1)),
    sg.CalendarButton('Select', target='-END-', format='%Y-%m-%d',
    close_when_date_chosen=False,begin_at_sunday_plus=1)],

    [sg.Button('Import',key='-IMPORT-',disabled=True),
    sg.ProgressBar(100,key='-PROGRESS-',size=(20,20),border_width=3),
    sg.Text('0%',key='-PERCENTAGE-')],

    [sg.Text('Select a format for the output file')],
    [sg.Radio('CSV', "RADIO1", key='-RADIO-', default=True),
    sg.Radio('XLSX', "RADIO1", key='-RADIO-', default=False),
    sg.Radio('DAT',"RADIO1", key = '-RADIO-', default=False)],

    [sg.Text("Choose an output folder:"), sg.Input(key='-IN1-',size=(20,1)),
    sg.FolderBrowse('Select')],

    [sg.Button('View',disabled=True),sg.Button("Save",disabled=True)],

    [sg.HSeparator(pad=10)],
    [sg.Text('How to acknowledge',font=('Helvetica',15),pad=5)],
    [sg.Multiline('This tool accompanies the article "A new catalog of solar' \
    ' flare events from soft x-ray GOES signal in the period 1986-2020" by N.' \
    ' Plutino et al. If you download data using this software please'\
    ' acknowledge the authors by citing the paper.'
    ,no_scrollbar=True,size=(45,5))],
    [sg.Button("Exit",pad=10)],
]

#=============================== Layout =======================================#

layout = [
    [
        sg.Column(first_col, element_justification='center'),
    ]
]

#=========================== Main Window ======================================#
window = sg.Window('Solar Flare Catalog Download App', layout,finalize=True)

while True:
    position=window.CurrentLocation()
    event, values = window.read()
    if event in (sg.WIN_CLOSED, 'Exit'):
        print('App shut down successfully')
        break

    if (values['-START-'] != '(yyyy-mm-dd)') \
    and (values['-END-'] != '(yyyy-mm-dd)'):
        window['-IMPORT-'].update(disabled=False)
    if event == '-IMPORT-':
        data = DataDownload(values['-START-'],values['-END-'])
        window['-PROGRESS-'].update_bar(100)
        window['-PERCENTAGE-'].update('100%')
        window['Save'].update(disabled=False)
        window['View'].update(disabled=False)
    if event == 'Save':
        if values['-IN1-']=='':
            Avviso('Please choose a destination folder before saving')
        else:
            dest_string=values['-IN1-']+'/'+values['-START-']
            if values['-RADIO-'] == True:
                data.to_csv(dest_string+'.csv',index=False)
            elif values['-RADIO-1'] == True:
                data.to_excel(dest_string+'.xlsx',index=False)
            else:
                data.to_csv(dest_string+'.dat',sep='|',index=False)
    if event == 'View':
        DataVisualization(data)

window.close()
