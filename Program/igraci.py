import pandas as pd
import PySimpleGUI as sg


def player_search(output_data, player):
    if output_data['short_name'].str.contains(player).any():
        # check if any of the rows in column 'short_name' consists strings you entered as your desired player
        full_name = output_data[output_data['short_name'].str.contains(player)]['short_name']
        # .str.contains checks where is you input string contained, in which rows
        # full name is a pandas series object and can contain one or more elements
        if full_name.size > 1:
            # if there are more than one player with the same name/surname, code below picks only one
            full_name.to_csv('full_name.csv')

            sg.set_options(auto_size_buttons=True)
            df = pd.read_csv('full_name.csv', sep=',', engine='python', header=None)
            data = df.values.tolist()
            header_list = df.iloc[0].tolist()

            layout = [
                [sg.Text(full_name)],
                [sg.Text('Please choose one of the players from the list:')],
                [sg.Text('Enter his full name, and write it just as it is presented in the list above')],
                [sg.Text('Name:'), sg.InputText()],
                [sg.Submit(), sg.Cancel()]
            ]
            window = sg.Window('Table of available players', layout, grab_anywhere=False)
            event, values = window.read()
            window.close()
            chosen_player = str(values[0])
            new_name = full_name[full_name.str.contains(chosen_player)].item()
            # new name will be a string object
            # .item() transforms it from series to string because it takes only the item value from that series
            cluster = output_data.loc[output_data['short_name'] == new_name, 'Cluster'].item()
        # cluster variable returns the number of cluster in which our player is
        # .loc locates in which row is our player and then finds the cluster number from column Cluster
        # using .item() function
        else:
            # this part does the same as above, but only if there is only one player matching your search
            # e.g. if you look for Modrić, you'll get only one player matching that search
            full_name = full_name.item()
            cluster = output_data.loc[output_data['short_name'] == full_name, 'Cluster'].item()

        # is_in_cluster makes a boolean array (True/False) for values of our chosen cluster in the
        # column of all Cluster values
        is_in_cluster = output_data['Cluster'] == cluster
        # clustered_data returns a dataframe with only True values of is_in_cluster
        clustered_data = output_data[is_in_cluster]
        clustered_data.drop(['Cluster', 'Unnamed: 0'], inplace=True, axis=1)
        clustered_data.to_csv('clustered_data.csv')

        # print the final result with only necessary columns
        def table_example():

            sg.set_options(auto_size_buttons=True)
            df = pd.read_csv('clustered_data.csv', sep=',', engine='python', header=None)
            data = df.values.tolist()
            header_list = df.iloc[0].tolist()

            layout = [
                [sg.Table(values=data,
                          headings=header_list,
                          display_row_numbers=True,
                          auto_size_columns=False,
                          num_rows=min(25, len(data)))]
            ]

            window = sg.Window('Table', layout, grab_anywhere=False)
            event, values = window.read()
            window.close()

        table_example()
    # if you search for some non-existent player, you'll get this message
    else:
        layout = [
            [sg.Text('That player is not present in the database.')],
            [sg.Text('Please run the code again and search for a valid player')],
            [sg.Cancel()]
        ]

        window3 = sg.Window('Player Search', layout)
        event, values = window3.read()
        window3.close()
