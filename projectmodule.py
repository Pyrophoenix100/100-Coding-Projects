def printheader(projectname, projectnum, startdate, enddate, notes):
	print("======================================")
	print("100 Coding Projects")
	print("Project #%d - %s" % (projectnum, projectname))
	print("Started: %s" % startdate)
	print("Completed: %s" % enddate)
	if notes != "": 
		print(notes)
	print("======================================")