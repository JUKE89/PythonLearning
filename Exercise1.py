movies = ["The Holy Grail", "The Life of Brian", "The Meaning of Life"]
#insert Year before each movie
movies.insert(1, 1975)
movies.insert(3, 1979)
movies.insert(5, 1983)

#printing individually
#print (movies[0])
#print (movies[1])
#print (movies[2])
#print (movies[3])
#print (movies[4])
#print (movies[5])

#looping
##for
for each_movie in movies:
	print (each_movie)

##while
count = 0
while ( count < len(movies) ):
	print (movies[count])
	count = count + 1