import pandas as pd
import PySimpleGUI as sg
from igraci import player_search

output_data = pd.read_csv('final_data.csv', index_col=0)
sg.theme('SandyBeach')

layout = [
    [sg.Text('Enter the last name of the player whose substitutes you are looking for')],
    [sg.Text('Input is both case- and language-sensitive')],
    [sg.Text('(You need to type in the name as it is natively written)')],
    [sg.Text('Name'), sg.InputText()],
    [sg.Text('Select the characteristics by which the players will be compared:')],
    [sg.Text('(If nothing is selected, the program will default to outputting overall similar players)')],
    [sg.Combo(['Overall', 'Attacking', 'Shooting', 'Passing',
               'Dribbling', 'Defending', 'Goalkeeping'], enable_events=True, key='combo')],
    [sg.Submit(), sg.Cancel()]
]

window1 = sg.Window('Player Search', layout)

while True:
    event, values = window1.read()
    if event is None or event == "Cancel":
        break
    if event == 'Submit':
        name = str(values[0])
        combo = values['combo']
        if combo == 'Overall':
            data = pd.read_csv('final_data.csv')
            player_search(data, name)

        elif combo == 'Attacking':
            data = pd.read_csv('attacking_data.csv')
            player_search(data, name)
        elif combo == 'Shooting':
            data = pd.read_csv('shooting_data.csv')
            player_search(data, name)
        elif combo == 'Passing':
            data = pd.read_csv('passing_data.csv')
            player_search(data, name)
        elif combo == 'Dribbling':
            data = pd.read_csv('dribbling_data.csv')
            player_search(data, name)
        elif combo == 'Defending':
            data = pd.read_csv('defending_data.csv')
            player_search(data, name)
        elif combo == 'Goalkeeping':
            data = pd.read_csv('goalkeeping_data.csv')
            player_search(data, name)
        elif combo == '':
            data = pd.read_csv('final_data.csv')
            player_search(data, name)

window1.close()
