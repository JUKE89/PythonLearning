#Functions
def recursive_list_printer(input_list):
	for each_item in input_list:
		if isinstance(each_item, list):
			recursive_list_printer(each_item)
		else:
			print(each_item)

#single line comment: defining a nested list
movies = ["The Holy Grail", 1975, "Terry Jones & Terry Gilliam", 91, ["Graham Chapman", ["Michael Palin", "John Cleese","Terry Gilliam", "Eric Idle", "Terry Jones"]]]

"""multi line comment
This is a multi line comment"""
recursive_list_printer(movies)