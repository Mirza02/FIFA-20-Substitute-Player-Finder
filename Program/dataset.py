import pandas as pd
from sklearn import preprocessing
from sklearn.cluster import KMeans

pd.set_option("display.max_columns", None)

#   reading .csv file into pandas dataframe
fifa20 = pd.read_csv('players_20.csv')
#   saving data for output which will be used later
column_copy = fifa20[['short_name', 'long_name', 'age', 'overall',
                      'nationality', 'club', 'wage_eur',
                      'contract_valid_until']]
#   copying the columns into a new dataset and saving output data to .csv
output_data = column_copy.copy()
output_data.to_csv('outputdata.csv')

#   deleting unnecessary columns before further analysis
fifa20.drop(['sofifa_id', 'player_url', 'potential',
             'real_face', 'release_clause_eur', 'team_jersey_number',
             'loaned_from', 'joined', 'nation_position',
             'nation_jersey_number', 'body_type',
             'player_tags', 'value_eur', 'player_traits',
             'international_reputation', 'team_position',
             'short_name', 'long_name', 'age',
             'dob', 'nationality', 'club', 'wage_eur',
             'contract_valid_until', 'ls', 'st', 'rs',
             'rs', 'lw', 'lf', 'cf', 'rf', 'rw', 'lam',
             'cam', 'ram', 'lm', 'lcm', 'cm', 'rcm',
             'rm', 'lwb', 'ldm', 'cdm', 'rdm', 'rwb',
             'lb', 'lcb', 'cb', 'rcb', 'rb'],
            inplace=True, axis=1)
#   operationalizing string values so they can be used in analysis
fifa20['preferred_foot'] = fifa20['preferred_foot'].replace(['Left', 'Right'], [0, 1])

fifa20['work_rate'] = fifa20['work_rate'].replace(['High/High', 'High/Medium', 'High/Low',
                                                   'Medium/High', 'Medium/Medium', 'Medium/Low',
                                                   'Low/High', 'Low/Medium', 'Low/Low'],
                                                  [0, 1, 2, 3, 4, 5, 6, 7, 8])
#   filling all empty values with 0
fifa20.fillna(value=0, inplace=True)


def player_positions(input_string):
    forward_position = ['ST', 'LW', 'RW']  # list
    center_position = ['CM', 'CAM', 'CF', 'CDM', 'LM', 'RM']
    back_position = ['CB', 'LB', 'RB']

    if 'GK' in input_string:
        return 0

    for i in range(len(forward_position)):
        if forward_position[i] in input_string:
            return 1

    for i in range(len(center_position)):
        if center_position[i] in input_string:
            return 2

    for i in range(len(back_position)):
        if back_position[i] in input_string:
            return 3


fifa20['player_positions'] = fifa20['player_positions'].apply(lambda x: player_positions(x))

column_copy_passing = fifa20[['height_cm', 'weight_kg', 'overall',
                              'player_positions', 'preferred_foot', 'weak_foot',
                              'skill_moves', 'work_rate', 'pace',
                              'passing', 'physic', 'attacking_crossing',
                              'attacking_heading_accuracy', 'attacking_short_passing', 'skill_curve',
                              'skill_long_passing', 'skill_ball_control', 'movement_reactions',
                              'movement_balance', 'power_jumping', 'power_strength',
                              'mentality_aggression', 'mentality_positioning', 'mentality_vision',
                              'mentality_composure']]

player_passing = column_copy_passing.copy()

column_copy_defending = fifa20[['height_cm', 'weight_kg', 'overall',
                                'player_positions', 'preferred_foot', 'weak_foot',
                                'work_rate', 'pace', 'defending',
                                'physic', 'movement_acceleration', 'movement_sprint_speed',
                                'movement_agility', 'movement_reactions', 'movement_balance',
                                'power_jumping', 'power_stamina', 'power_strength',
                                'mentality_aggression', 'mentality_interceptions', 'mentality_positioning',
                                'mentality_vision', 'mentality_composure', 'defending_marking',
                                'defending_standing_tackle', 'defending_sliding_tackle']]

player_defending = column_copy_defending.copy()

column_copy_shooting = fifa20[['height_cm', 'weight_kg', 'overall',
                               'player_positions', 'preferred_foot', 'weak_foot',
                               'skill_moves', 'work_rate', 'shooting',
                               'physic', 'attacking_finishing', 'attacking_heading_accuracy',
                               'attacking_volleys', 'skill_curve', 'skill_fk_accuracy',
                               'skill_ball_control', 'movement_agility', 'movement_reactions',
                               'movement_balance', 'power_shot_power', 'power_jumping',
                               'power_stamina', 'power_strength', 'power_long_shots',
                               'mentality_aggression', 'mentality_positioning', 'mentality_vision',
                               'mentality_penalties', 'mentality_composure']]

player_shooting = column_copy_shooting.copy()

column_copy_dribbling = fifa20[['height_cm', 'weight_kg', 'overall',
                                'player_positions', 'preferred_foot', 'weak_foot',
                                'skill_moves', 'work_rate', 'pace',
                                'dribbling', 'physic', 'skill_dribbling',
                                'skill_curve', 'skill_ball_control', 'movement_acceleration',
                                'movement_sprint_speed', 'movement_agility', 'movement_reactions',
                                'movement_balance', 'power_stamina', 'mentality_aggression',
                                'mentality_vision', 'mentality_composure']]

player_dribbling = column_copy_dribbling.copy()

column_copy_goalkeeping = fifa20[['height_cm', 'weight_kg', 'overall',
                                  'player_positions', 'preferred_foot', 'weak_foot',
                                  'work_rate', 'gk_diving', 'gk_handling',
                                  'gk_kicking', 'gk_reflexes', 'gk_speed',
                                  'gk_positioning', 'skill_curve', 'attacking_short_passing',
                                  'skill_long_passing', 'movement_agility', 'movement_reactions',
                                  'movement_balance', 'power_shot_power', 'power_jumping',
                                  'power_stamina', 'power_strength', 'mentality_aggression',
                                  'mentality_interceptions', 'mentality_positioning', 'mentality_vision',
                                  'mentality_composure', 'goalkeeping_diving', 'goalkeeping_handling',
                                  'goalkeeping_kicking', 'goalkeeping_positioning', 'goalkeeping_reflexes']]

player_goalkeeping = column_copy_goalkeeping.copy()

column_copy_attacking = fifa20[['height_cm', 'weight_kg', 'overall',
                                'player_positions', 'preferred_foot', 'weak_foot',
                                'skill_moves', 'work_rate', 'pace',
                                'shooting', 'passing', 'dribbling',
                                'physic', 'attacking_crossing', 'attacking_finishing',
                                'attacking_heading_accuracy', 'attacking_short_passing', 'attacking_volleys',
                                'skill_dribbling', 'skill_curve', 'skill_fk_accuracy',
                                'skill_long_passing', 'skill_ball_control', 'movement_acceleration',
                                'movement_sprint_speed', 'movement_agility', 'movement_reactions',
                                'movement_balance', 'power_shot_power', 'power_jumping',
                                'power_stamina', 'power_strength', 'power_long_shots',
                                'mentality_aggression', 'mentality_positioning', 'mentality_interceptions',
                                'mentality_vision', 'mentality_penalties', 'mentality_composure']]

player_attacking = column_copy_attacking.copy()


#   data is scaled in the range from 0 to 1, so no problems would arise during analysis
def cluster(table):
    x = table.values
    scaler = preprocessing.MinMaxScaler()
    x_scaled = scaler.fit_transform(x)
    X_norm = pd.DataFrame(x_scaled)

    #   1000 clusters are made with random starting points
    kmeans = KMeans(init="random", n_clusters=1000, random_state=42)
    preds = kmeans.fit_predict(X_norm)

    # a column named 'Cluster' is added to the output data and saved to .csv
    output_data['Cluster'] = preds
    return


cluster(fifa20)
output_data.to_csv('final_data.csv')

cluster(player_passing)
output_data.to_csv('passing_data.csv')

cluster(player_attacking)
output_data.to_csv('attacking_data.csv')

cluster(player_defending)
output_data.to_csv('defending_data.csv')

cluster(player_dribbling)
output_data.to_csv('dribbling_data.csv')

cluster(player_goalkeeping)
output_data.to_csv('goalkeeping_data.csv')

cluster(player_shooting)
output_data.to_csv('shooting_data.csv')
