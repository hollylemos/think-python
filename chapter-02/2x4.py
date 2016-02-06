
#part 1:
# if a sphere with radius r is 4/3*(pi)r^3 . What is the volume of a sphere with radius 5?

r = 5.0

def volume(r):
	volume = ((4.0 / 3.0) * (3.14) * (r)**3)
	print 'Problem 1:'
	print 'The volume of a sphere with radius of 5 is:', round(volume)

volume(r)

#part 2
#suppose the cover price of a book is $24.95, but bookstores get a 40% discount. Shipping costs $3 for 
#the first copy and 75 cents for each additional copy. What is the total wholesale cost for 60 copies?

books = 60.0

def total(books):
	cost_of_book = 24.95 * (1 - 0.4) 
	shipping = (3 + (.75 * 59))
	totalcost = shipping + (books * cost_of_book)
	print 'Problem 2:'
	print 'The wholesale cost of each book is $', cost_of_book 
	print 'Shipping 60 books at a rate of $3 for the first book, and .75 cents for each additional book is $', shipping
	print 'The total cost for all 60 books and shipping is $', totalcost

total(books)

#part 3
#If I leave my house at 6:52 am and run 1 mile at an easy pace (8:15 per mile), then 3 miles at tempo 
#(7:12 per mile) and 1 mile at easy pace again, what time do I get home for breakfast?


start_hour = 6
start_minute = 52

def run():
	start = (6*60+52)*60
	easy = (8*60+15)*2
	fast = (7*60+12)*3
	easy_mph = 60.0/((8*60+15.0)/60)
	fast_mph= 60.0/((7*60+12.0)/60.0)
	runtime = (easy + fast)/60
	finish_hour = (start + easy + fast)/(60*60.0)
	finish_floored = (start + easy + fast)//(60*60) 
	finish_minute  = (finish_hour - finish_floored)*60
	print 'Problem 3:'
	print 'I started my run at %d:%d' % (start_hour, start_minute), 'am'
	print 'I ran for', runtime, 'minutes'
	print 'I ran 2 miles at an easy pace of', round(easy_mph, 2),'mph'
	print 'I ran 3 miles at a tempo pace of', round(fast_mph, 2),'mph'
	print 'Back for breakfast at %d:%d' % (finish_hour,finish_minute)


run()



