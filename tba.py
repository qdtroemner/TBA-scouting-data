import requests
import secrets

class TBA:
	def __init__(self, team:str, event:str):
		self.auth = secrets.TBA_AUTH
		self.base_url = 'https://www.thebluealliance.com/api/v3'
		self.team = team
		self.event = event

	def get_event(self, endpoint:str=''):
		url = self.base_url + f'/event/{self.event}' + endpoint 
		return requests.get(url, 
			headers={'accept': 'application/json', 'X-TBA-Auth-Key': self.auth}, 
			params={'event_key': self.event}
		).json()

	def get_OPRs(self):
		endpoint = '/oprs'
		return self.get_event(endpoint)

	def get_matches(self):
		endpoint = '/matches'
		return self.get_event(endpoint)
	
	def get_teams(self):
		endpoint = '/teams'
		return self.get_event(endpoint)

	def get_team_status(self):
		url = self.base_url + f'/team/{self.team}/event/{self.event}/status'
		return requests.get(url, 
			headers={'accept': 'application/json', 'X-TBA-Auth-Key': self.auth}, 
			params={'team_key': self.team, 'event_key': self.event}
		).json()

def clamp_to_bin(num, min_val, max_val):
	range = max_val - min_val
	return (((num - min_val) * 1) / range) + 0