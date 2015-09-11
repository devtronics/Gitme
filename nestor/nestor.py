#!/usr/bin/python3
# authored by chris heckler


def main():
	print("This is my first module")

""" This function takes a positional argument called 'the_list' which is any Pytohon list(of, possibly, nested lists) Each data item in the provided list is (recursively) printed to the screen on its own line. Vim is becoming fun to work with as well. """

def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

if __name__ == "__main__": main()
