import re
filename = input("ENTER THE C FILE:")
searchfile = open(filename,"r")
vulnc = ['gets','strcpy','stpcpy','strcat','strcmp','sprintf']
gets = re.findall('gets(',searchfile)
strcpy = re.finall('strcpy(',searchfile)
stpcpy = re.finall('stpcpy(',searchfile)
strcat = re.finall('strcat(',searchfile)
strcmp = re.finall('strcmp(',searchfile)
sprintf = re.finall('sprintf(',searchfile)
if len(gets) != 0:
	print("""
		MITIGATION:
		USE FGETS INSTEAD GETS
		"""
		)
else:
	pass
if len(strcpy) != 0:
	print("""
		MITIGATION:
		USE STRLCPY INSTEAD OF STRCPY
		"""
		)
else:
	pass
if len(stpcpy) != 0:
	print("""
		MITIGATION:
		USE STRLPY INSTEAD OF STPCPY
		"""
		)
else:
	pass
if len(strcat) != 0:
	print("""
		MITIGATION:
		TO MITIGATE STRCAT ISSUES USE STRNCAT
		"""
		)
else:
	pass
if len(strcmp) !=0 :
	print("""
	MITIGATION:
	TO MITIGATE STRCMP ISSUES USE STRNCPM)
	"""
	)
else:
	pass
if len(sprintf) !=0:
	print("""
	MITIGATION:
	TO MITIGATE SPRINTF ISSUES USE SNPRINTF
	"""
	)
else :
	pass



	 	
