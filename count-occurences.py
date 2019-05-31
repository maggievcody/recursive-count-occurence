def cnt_occur(mylist, value):
	i = 0
	if mylist == []:								# base case = empty list
		return 0
	elif mylist[i] == value:							# checks if value is in mylist
		return 1 + cnt_occur(mylist[(i+1):],value)				# if value is in mylist then returns a count of one and checks rest of list
	else:
		if isinstance(mylist[i], list) == True:					# checks if item of mylist is a list
			if value in mylist[i]:						# checks if value is in list in mylist
				return 1 + cnt_occur(mylist[(i+1):],value)		# returns a count of one and checks the rest of list
			else:
				return cnt_occur(mylist[(i+1):],value)
		else:
			return cnt_occur(mylist[(i+1):],value)				# checks rest of list
