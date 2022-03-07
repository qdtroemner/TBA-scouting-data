import requests
import secrets

class TBA:
	def __init__(self, team:str, event:str):
		self.auth = secrets.TBA_AUTH
		self.base_url = 'https://www.thebluealliance.com/api/v3'
		self.team = team
		self.event = event

	def tba_get(self, endpoint:str='', params={}):
		url = self.base_url + endpoint
		try:
			req = requests.get(url,
				headers={'accept': 'application/json', 'X-TBA-Auth-Key': self.auth}, 
				params=params
			)
			if req.status_code == 200: return req.json()
			else:
				print(req.text)
				exit
		except Exception as error:
			print(error)
			exit

	# Get CCWM, OPR, and DPR stats for teams participating in the event
	def get_OPRs(self):
		endpoint = f'/event/{self.event}/oprs'
		return self.tba_get(endpoint, params={'event_key': self.event})

	# Get the matches that have been played in the event
	def get_matches(self):
		endpoint = f'event/{self.event}/matches'
		return self.tba_get(endpoint, params={'event_key': self.event})
	
	# Get the information of teams participating in the event
	def get_teams(self):
		endpoint = f'/event/{self.event}/teams'
		return self.tba_get(endpoint, params={'event_key': self.event})

	# Get a team's ranking and other statistics
	def get_team_status(self, team):
		endpoint = f'/team/{team}/event/{self.event}/status'
		return self.tba_get(endpoint, params={'team_key': self.team, 'event_key': self.event})