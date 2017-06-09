#Module for recursive_list_printer
#Functions
def recursive_list_printer(input_list):
	for each_item in input_list:
		if isinstance(each_item, list):
			recursive_list_printer(each_item)
		else:
			print(each_item)