import time

#get how many seconds since 01/01/70
current = time.time()
#and print it using f-string
print(f"Seconds since January 1, 1970: {current:,.4f} or {current:.2e} in scientific notation")
# ,.4f formate avec des virgules pour les milliers et 4 chiffres apres la virgule
# .2e formate en notation scientifique


#now the formated date
date = time.strftime("%b %d %Y", time.localtime(current))
print(date)