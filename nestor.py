#!/usr/bin/python3
# authored by chris heckler

def main():
	print("This is my first module")

def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item, list):
			print_lol(each_item)
		else:
			print(each_item)

if __name__ == "__main__": main()
