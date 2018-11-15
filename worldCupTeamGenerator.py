##world cup program

#enter number of players
#ask if teams will be randomized (from WC pool)
#alternatively can pick (from WC pool)
from random import choice

print("The World cup is bloody great!")

wc_teams = [
'Senegal','Panama','Mexico','Switzerland','Iceland','Australia','Spain','Saudi Arabia','Japan','England','Korea Republic','Serbia','Nigeria','Denmark','Iran','Uruguay','Colombia','Poland','Tunisia','Belgium','Sweden','Germany','Costa Rica','Brazil','Croatia','Argentina','Peru','France','Morocco','Portugal','Egypt','Russia',
]
		
#lets find out how many players are playing:
while True:
	try:
		players = int(input("\nHow many players are there?: "))
		break
	except: print("Enter a number, m8")
	
#create a list of names based on number of players

player_names = []
x = 0

while x < players:
	name = input("What is player " + str(x +1) + "'s name?: ")
	player_names.append(name)
	x += 1

#randomize teams or nah?
random = (input("Do you want randomized teams? Say Yes or No: "))

player_ass = {}

if random.lower() == "no":
	print("OK then, enter your team names as follows!")
	#have user enter their team and check that the team is in the wc_teams list
	for name in player_names:
		team = input(name + ", enter your team here: ")
		if team.title() not in wc_teams:
			team = input("Pick a different team, or make sure it is spelled right")
		player_ass[name] = team
		
else:
	print("OK, we'll assign teams randomly!") #randomize team
	for name in player_names:
		team = choice(wc_teams)
		wc_teams.remove(team)
		player_ass[name] = team
	
print(player_ass)
