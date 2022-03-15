"""
@TODO: team_qual_stats data is not retrievable after a competition is over. Catch this limitation to collect data after an event.
"""

from kilascout.tba import TBA
import pandas as pd

client = TBA(team='frc4481', event='2022flwp')
scouting_data = pd.DataFrame()

team_ids = []
for team in client.get_teams(): # Get the teams participating in an event
	team_ids.append(team['key'])
scouting_data.index = team_ids # Set the row labels to the team ids (eg. 'frc1024')

# Make API calls first (reduces bandwidth)
ratings = client.get_event_ratings() # CCWM, OPR, & DPR
for i, team in enumerate(scouting_data.index): # For every row in our data
	team_qual_stats = client.get_team_status(team)

	scouting_data.at[team, 'CCWM'] = ratings['ccwms'][team]
	scouting_data.at[team, 'OPR'] = ratings['oprs'][team]
	scouting_data.at[team, 'DPR'] = ratings['dprs'][team]
		
	if team_qual_stats is not None:
		team_qual_stats = team_qual_stats['qual'] # Team stats based on qualification matches
		for stat_index, stat in enumerate(team_qual_stats['sort_order_info']): # For every qualification stat
			key = stat['name'] # Get the name/description of the stat
			scouting_data.at[team, key] = team_qual_stats['ranking']['sort_orders'][stat_index] # Append stat to corresponding cell (team, stat label)

scouting_data.to_excel('/Users/qdtroemner/Documents/Programming/TBA Scouting Data/python_spreadsheets/data/scouting_data_2.xlsx')