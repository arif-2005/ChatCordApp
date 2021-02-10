import datetime

def time(type):
	t = datetime.datetime.now()
	y = str(t.year)
	m = str(t.month)
	d = str(t.day)
	h = str(t.hour)
	m = str(t.minute)
	s = str(t.second)
	if (len(m) == 1):
		m = "0" + m
	if(int(h) > 12):
		h = str(int(h)-12)
		meridian = "pm"
	else:
		meridian = "am"
	if(type == "h"):
		return (h)
	if(type == "m"):
		return (m)
	if(type == "s"):
		return (s)
	if(type == "hm"):
		return (h+":"+m+" "+meridian)
	if(type == "ms"):
		return (m+":"+s)
	if(type == "hs"):
		return (h+":"+s)
	if(type == "ymdhms"):
		return (y+"/"+m+"/"+d+"-"+h+":"+m+":"+s)
	else:
		return ("Value not applicable")


def pdate():
	t = datetime.datetime.now()
	Y = str(t.year)
	M = str(t.month)
	D = str(t.day)
	if (int(M)==1):
		M = "Jan"
	elif (int(M)==2):
		M = "Feb"
	elif (int(M)==3):
		M = "Mar"
	elif (int(M)==4):
		M = "Apr"
	elif (int(M)==5):
		M = "May"
	elif (int(M)==6):
		M = "June"
	elif (int(M)==7):
		M = "July"
	elif (int(M)==8):
		M = "Aug"
	elif (int(M)==9):
		M = "Sep"
	elif (int(M)==10):
		M = "Oct"
	elif (int(M)==11):
		M = "Nov"
	else:
		M = "Dec"
	if (len(D)==1):
		if (D == "1"):
			D = D+"st "
		elif (D == "2"):
			D = D+"nd "
		elif (D == "3"):
			D = D+"rd "
		else:
			D = D+"th "
	else:
		g = str(int(D)%10)
		if (g == "1"):
			D = D+"st "
		elif (g == "2"):
			D = D+"nd "
		elif (g == "3"):
			D = D+"rd "
		else:
			D = D+"th "
	return (D+M)

print(time("hm"))
print(pdate())



