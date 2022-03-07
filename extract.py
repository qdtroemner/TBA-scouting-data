from tba import TBA
import pandas as pd

CONTRIBUTION_WEIGHT = 0.5
OFFENSIVE_WEIGHT = 0.3
DEFENSIVE_WEIGHT = 0.2

client = TBA(team='frc1024', event='2022inkok')
data = pd.DataFrame()

teams = []
for team in client.get_teams():
	teams.append(team['key'])
data.index = teams

oprs = client.get_OPRs()
for i, team in enumerate(data.index):
	data.at[team, 'CCWM'] = oprs['ccwms'][team]
	data.at[team, 'OPR'] = oprs['oprs'][team]
	data.at[team, 'DPR'] = oprs['dprs'][team]

for i, team in enumerate(data.index):
	team_qual_stats = client.get_team_status(team)['qual']
	for stat_index, stat in enumerate(team_qual_stats['sort_order_info']):
		key = stat['name']
		data.at[team, key] = team_qual_stats['ranking']['sort_orders'][stat_index]
print(data)

#data.to_excel('./data/scouting_data.xlsx')