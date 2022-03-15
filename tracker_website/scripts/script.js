const EVENT = '2022ncgre';
const TEAM = 'frc4795';
var client = new TBA(EVENT, TEAM);

const PARENT_URL = 'localhost';

function set_stream_URL() {
	client.get_event().then(data => {
		if (data.webcasts.length > 0) {
			let webcasts = data.webcasts;
			for (webcast of webcasts) {
				if (webcast.type == "twitch") {
					let channelID = webcast.channel;
					let streamURL = `https://player.twitch.tv/?channel=${channelID}&parent=${PARENT_URL}`;
					document.getElementById('event-stream').src = streamURL;
				}
			}
		}
	});
}

function set_next_match_info() {
	client.get_team_matches().then(data => {
		let next_match = Infinity; // Set it to highest possible value and work down
		for (match of data) {
			let n = match.match_number;
			if (match.actual_time != null) {
				continue;
			}
			if (n < next_match) {
				next_match = n;
			}
		}
		document.getElementById('next-match-label').innerHTML = next_match;
	});
}

(function() {
	console.log("Ready");
	set_stream_URL();
	set_next_match();

	client.get_team_matches().then(data => {
		console.log(data);
	});
})();