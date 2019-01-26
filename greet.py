# Find out how many players total and if teams will be randomized or not

# For our Yes or No question later. Returns True (y) or False (n)
def randomYN():
    check = str(input("\nDo you want teams to be assigned at random?  (Y/N): ")).lower().strip()
    try:
        if check[0] == 'y':
            return True
        elif check[0] == 'n':
            return False
        else:
            print('Invalid Input')
    except: print("Please enter valid inputs")
    return randomYN()

# Greets players and asks if teams will be randomized.
def greet_user():
	print("This is the bracket maker.")
	

def get_player_count():
	while True:
		try:
			player_count = int(input("\nHow many players are there?: "))
			if player_count > 4 and player_count % 2 == 0:
				return player_count
				break
			else: print("Enter an even number larger than 4! ")
		except: print("Enter an even number larger than 4! ")

		

def get_player_names(player_count,player_names):
	"""Get the names of contestants"""
	x = 0
	while x < player_count:
		name = input("What is player " + str(x +1) + "'s name?: ")
		while True:
			if len(name) < 1:
				name = input("Try entering your name again: ")
			else: break
		player_names.append(name)
		x += 1
	

