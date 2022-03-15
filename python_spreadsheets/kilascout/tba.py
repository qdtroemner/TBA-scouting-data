import requests
try:
	from . import tba_secrets
except ImportError:
	import tba_secrets

class TBA:
	def __init__(self, team:str, event:str):
		"""
			Initializes a new The Blue Alliance API client.
			
			Parameters
			----------
			team : str
				TBA team key (eg. 'frc1024'). This will be the default team used in most calls.
			event : str
				TBA event key (eg. '2022inkok'). This will be the default event used in most calls.
		"""
		self.auth = tba_secrets.TBA_AUTH
		self.base_url = 'https://www.thebluealliance.com/api/v3'
		self.team = team
		self.event = event

	def tba_get(self, endpoint:str=''):
		"""
			Returns the JSON response of an HTTP GET request for the TBA API.

			Parameters
			----------
			endpoint : str
			The endpoint of the API request.
		"""
		url = self.base_url + endpoint
		try:
			req = requests.get(url,
				headers={'accept': 'application/json', 'X-TBA-Auth-Key': self.auth}, 
			)
			if req.status_code == 200: return req.json()
			else:
				print(req.text)
				exit
		except Exception as error:
			print(error)
			exit

	# Get CCWM, OPR, and DPR stats for teams participating in the event
	def get_event_ratings(self):
		"""
			Gets contribution to winning margin (CCWM), 
			offensive power ranking (OPR), and defensive power ranking (DPR)
			for each team in the default event.
		"""
		endpoint = f'/event/{self.event}/oprs'
		return self.tba_get(endpoint)

	# Get the matches that have been played in the event
	def get_matches(self):
		"""
			Returns a list of matches that have been played (and will be played?)
			in the default event.
		"""
		endpoint = f'/event/{self.event}/matches'
		return self.tba_get(endpoint)
	
	# Get the information of teams participating in the event
	def get_teams(self):
		"""
			Returns a list of teams participating in the default event.
		"""
		endpoint = f'/event/{self.event}/teams'
		return self.tba_get(endpoint)

	# Get a team's ranking and other statistics
	def get_team_status(self, team):
		"""
			Gets a team's competition rank and status.

			Parameters
			----------
			team : str
				The team to get ranking and status of.
		"""
		endpoint = f'/team/{team}/event/{self.event}/status'
		return self.tba_get(endpoint)

	def get_event(self):
		"""
		"""
		endpoint = f'/event/{self.event}'
		return self.tba_get(endpoint)

	def get_event_stream_url(self):
		""""""
		req = self.get_event()
		streams = req['webcasts']
		if len(streams) > 0:
			for stream in streams:
				if stream['type'] == 'twitch':
					return 'https://www.twitch.tv/' + stream['channel']
		return None

	def get_match_zebra(self, match):
		""""""
		endpoint = f'/match/{match}/zebra_motionworks'
		return self.tba_get(endpoint)

	"""
		ENDPOINTS OF INTEREST
		---------------------

		teams

		/team/{team_key}/event/{event_key}/matches
		/team/{team_key}/event/{event_key}/matches/simple
		/team/{team_key}/event/{event_key}/matches/keys

		/team/{team_key}/event/{event_key}/status
		
		events

		/event/{event_key}/teams
		/event/{event_key}/teams/simple
		/event/{event_key}/teams/keys

		/event/{event_key}/teams/statuses
	"""

if __name__ == "__main__":
	client = TBA(team='frc1024', event='2022inkok')
	print(client.get_team_status('frc1024'))