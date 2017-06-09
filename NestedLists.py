#Nested Lists
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]
#Print the whole nested list mess
#print (movies)
for each_item in movies:
	if isinstance (each_item, list):
		for each_nest_item in each_item:
			print (each_nest_item)
	else:
		print (each_item)