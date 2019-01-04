from TomeRater import *

Tome_Rater = TomeRater()

#Create some books:
book1 = Tome_Rater.create_book("Society of Mind", 12345678)
novel1 = Tome_Rater.create_novel("Alice In Wonderland", "Lewis Carroll", 12345)
novel1.set_isbn(9781536831139)
nonfiction1 = Tome_Rater.create_non_fiction("Automate the Boring Stuff", "Python", "beginner", 1929452)
nonfiction2 = Tome_Rater.create_non_fiction("Computing Machinery and Intelligence", "AI", "advanced", 11111938)
novel2 = Tome_Rater.create_novel("The Diamond Age", "Neal Stephenson", 10101010)
novel3 = Tome_Rater.create_novel("There Will Come Soft Rains", "Ray Bradbury", 10001000)

#Intentionally created books with existing ISBNs to test if ISBN is unique
Tome_Rater.create_book("Society of Mind2", 12345678)
Tome_Rater.create_novel("The Diamond Age2", "Neal Stephenson2", 10101010)
Tome_Rater.create_non_fiction("Computing Machinery and Intelligence2", "AI", "advanced", 11111938)
#All of these books should return a message stating that the ISBN already exists

#Create users:
Tome_Rater.add_user("Alan Turing", "alan@turing.com")
Tome_Rater.add_user("David Marr", "david@computation.org")

#Intentionally added another user with an existing email to test the existing account checker 
Tome_Rater.add_user("David Marr2", "david@computation.org")
#Should print "A user with this email already exists!"

#Intentionally added a user with an invalid email to test invalid email checker
Tome_Rater.add_user("David Marr3", "david-computation.org")
Tome_Rater.add_user("David Marr2", "david@computation.or")
#Should print "Invalid email domain!" and "Invalid email provided!", respectively

#Add a user with three books already read:
Tome_Rater.add_user("Marvin Minsky", "marvin@mit.edu", user_books=[book1, novel1, nonfiction1])

#Add books to a user one by one, with ratings:
Tome_Rater.add_book_to_user(book1, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction1, "alan@turing.com", 3)
Tome_Rater.add_book_to_user(nonfiction2, "alan@turing.com", 4)
Tome_Rater.add_book_to_user(novel3, "alan@turing.com", 1)
Tome_Rater.add_book_to_user(novel2, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "marvin@mit.edu", 2)
Tome_Rater.add_book_to_user(novel3, "david@computation.org", 4)


#Uncomment these to test your functions:
print(Tome_Rater)
Tome_Rater.print_catalog()
Tome_Rater.print_users()
print("Most positive user:")
print(Tome_Rater.most_positive_user())
print("Highest rated book:")
print(Tome_Rater.highest_rated_book())
print("Most read book:")
print(Tome_Rater.most_read_book())
print("Most read books:")
print(Tome_Rater.get_n_most_read_books(3))
print("Most prolific readers:")
print(Tome_Rater.get_n_most_prolific_readers(2))
