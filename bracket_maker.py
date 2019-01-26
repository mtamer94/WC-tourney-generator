# Second try at this
import greet as g
import assignment as a

def fifa_tournament():
	
	player_names = []
	player_ass = {}
	
	while True:

		# Gret user
		g.greet_user() 
		
		# Random will be True if the players want teams randomized
		random = g.randomYN()
		
		# Get number of players. Must be even and greater than 4
		player_count = g.get_player_count()
		
		#Based on number of players, fill a list with their names
		g.get_player_names(player_count, player_names)

		# Assign teams if random, or manually select
		a.assign_teams(random, player_names, player_ass)

		# Export bracket to Google sheets or excel
		"""Build and export Bracket"""
		
		export_bracket(player_ass)

		# Email bracket to as many people who want


fifa_tournament()
