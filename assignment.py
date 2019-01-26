#team_assignment

from random import choice

wc_teams = [
'Senegal','Panama','Mexico','Switzerland','Iceland','Australia','Spain','Saudi Arabia','Japan','England','Korea Republic','Serbia','Nigeria','Denmark','Iran','Uruguay','Colombia','Poland','Tunisia','Belgium','Sweden','Germany','Costa Rica','Brazil','Croatia','Argentina','Peru','France','Morocco','Portugal','Egypt','Russia',
]
		
def assign_teams(random, player_names, player_ass):
	if random == True:
		print("OK, we'll assign teams randomly!") #randomize team
		for name in player_names:
			team = choice(wc_teams)
			wc_teams.remove(team)
			player_ass[name] = team
			
	elif random == False:
		teams = False
		print("OK then, enter your team names as follows!")
		# have user enter their team and check that the team is in the wc_teams list
		# Loop to ensure that a real WC team is picked
		for name in player_names:
			team = input(name + ", enter your team here: ")
			while team.title() not in wc_teams:
				team = input("\nPick a different team, or make sure it is spelled right. Enter 'Help' to see the list of World Cup Teams: ")
				if team.lower() == 'help':
					for t in wc_teams:
						print(t)
			player_ass[name] = team
