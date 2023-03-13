sport = 'basketball'
#creating iteration variable like index
index = 0
#while the iteration variable is less than the length of sport, SO the sport is 8 so from zero to five it will be 9
while index < len(sport):
    #pull out sport of index 1, 2, 3, 4, 5, 6, 7, 8, 9
    letter = sport[index]
    #print 2 columns, (one for numbers) and (one for letters)
    print(index, letter)
    #run and add 1 to index
    index = index + 1

