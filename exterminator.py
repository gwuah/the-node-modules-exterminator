from os.path import join
from os import walk 

def hunt(path) :
	path = os.walk(path)
	counter = 0
	db = {}

	for root, dirs, files in path :
		for dir_name in dirs :
			if dir_name == "node_modules" :
				counter += 1
				db[counter] = join(root, dir_name)

	return [db, counter]
