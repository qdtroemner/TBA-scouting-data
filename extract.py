from tba import TBA, clamp_to_bin
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
	ccwm = oprs['ccwms'][team]
	opr = oprs['oprs'][team]
	dpr = oprs['dprs'][team]
	data.at[team, 'CCWM'] = ccwm
	data.at[team, 'OPR'] = opr
	data.at[team, 'DPR'] = dpr
	data.at[team, 'Average'] = (
		clamp_to_bin(ccwm, data['CCWM'].min(), data['CCWM'].max()) + 
		clamp_to_bin(opr, data['OPR'].min(), data['OPR'].max()) + 
		clamp_to_bin(dpr, data['DPR'].min(), data['DPR'].max())
	) / 3
	data.at[team, 'Weighted Average'] = (
		clamp_to_bin(ccwm, data['CCWM'].min(), data['CCWM'].max()) * CONTRIBUTION_WEIGHT + 
		clamp_to_bin(opr, data['OPR'].min(), data['OPR'].max()) * OFFENSIVE_WEIGHT + 
		clamp_to_bin(dpr, data['DPR'].min(), data['DPR'].max()) * DEFENSIVE_WEIGHT
	)

data.to_excel('./data/OPRs_v2.xlsx')