class User(object):
  def __init__(self, name, email):
    self.name = name
    self.email = email
    self.books = {}

  def get_email(self):
    return self.email

  def change_email(self, address):
    self.email = address
    print("This user's email has been updated.")

  def __repr__(self):
    return "User {name}; email {email}; books read: {books}".format(name = self.name, email = self.email, books = len(self.books))

  def __eq__(self, other_user):
    return self.name == other_user.name and self.email == other_user.email

  def read_book(self, book, rating = None):
    self.books[book] = rating

  def get_average_rating(self):
    sum_rating = 0
    average_rating = 0
    for rating in self.books.values():
      if rating is None:
        pass
      else:
        sum_rating += rating
    average_rating = sum_rating / len(self.books)
    return average_rating

class Book(object):
  def __init__(self, title, isbn):
    self.title = title
    self.isbn = isbn
    self.ratings = []
    
  def get_title(self):
    return self.title

  def get_isbn(self):
    return self.isbn

  def set_isbn(self, new_isbn):
    self.isbn = new_isbn
    print("This book's ISBN has been updated.")

  def add_rating(self, rating): 
    if rating >= 0 and rating <= 4:
      self.ratings.append(rating)
    else:
      print("Invalid Rating.")

  def __eq__(self, other_book):
    return self.title == other_book.title and self.isbn == other_book.isbn

  def get_average_rating(self):
    sum_rating = 0
    average_rating = 0
    for rating in self.ratings:
      sum_rating += rating
    average_rating = sum_rating / len(self.ratings)
    return average_rating

  def __repr__(self):
    return "{title}".format(title = self.title)

  def __hash__(self):
    return hash((self.title, self.isbn))

class Fiction(Book):
  def __init__(self, title, author, isbn):
    super().__init__(title, isbn)
    self.author = author

  def get_author(self):
    return self.author

  def __repr__(self):
    return "{title} by {author}".format(title = self.title, author = self.author)

class Non_Fiction(Book):
  def __init__(self, title, subject, level, isbn):
    super().__init__(title, isbn)
    self.subject = subject
    self.level = level

  def get_subject(self):
    return self.subject

  def get_level(self):
    return self.level

  def __repr__(self):
    return "{title}, {level} manual on {subject}".format(title = self.title, level = self.level, subject = self.subject)

class TomeRater:
  def __init__(self):
    self.users = {}
    self.books = {}
    self.isbns = []

  def __repr__(self):
    return "Tome Rater currently storing " + str(len(self.users)) + " users and " + str(len(self.isbns)) + " unique books."

  def __eq__(self, other_rater):
    return self.users == other_rater.users and self.isbns == other_rater.isbns

  def create_book(self, title, isbn):
    new_book = Book(title, isbn)
    if isbn in self.isbns:
      print("A book with that ISBN already exists!")
    else:
      self.isbns.append(isbn)
      return new_book

  def create_novel(self, title, author, isbn):
    new_novel = Fiction(title, author, isbn)
    if isbn in self.isbns:
      print("A novel with that ISBN already exists!")
    else:
      self.isbns.append(isbn)
      return new_novel

  def create_non_fiction(self, title, subject, level, isbn):
    new_non_fiction = Non_Fiction(title, subject, level, isbn)
    if isbn in self.isbns:
      print("A non-fiction with that ISBN already exists!")
    else:
      self.isbns.append(isbn)
      return new_non_fiction

  def add_book_to_user(self, book, email, rating = None):
    if self.users.get(email) is None:
      print("No user with email {email}!".format(email = email))
    else:
      self.users.get(email).read_book(book, rating)
      if rating is None:
        pass
      else:
        book.add_rating(rating)
      if self.books.get(book) is None:
        self.books[book] = 1
      else:
        self.books[book] += 1

  def add_user(self, name, email, user_books = None):
    new_user = User(name, email)
    if "@" in email:
      if ".com" in email or ".org" in email or ".edu" in email:
        if email in self.users.keys():
          print("A user with this email already exists!")
        else:
          self.users[email] = new_user
          if user_books is None:
            pass
          else:
            for book in user_books:
              self.add_book_to_user(book, email)
          self.users[email] = new_user
      else:
        print("Invalid email domain!")
    else:
      print("Invalid email provided!")    

  def print_catalog(self):
    for book in self.books.keys():
      print(book)

  def print_users(self):
    for user in self.users.values():
      print(user)

  def most_read_book(self):
    highest_key = ""
    highest_value = float("-inf")
    for key, value in self.books.items():
      if value > highest_value:
        highest_key = key
        highest_value = value
    return highest_key

  def highest_rated_book(self):
    highest_key = ""
    highest_avg_rating = float("-inf")
    for book in self.books.keys():
      if book.get_average_rating() > highest_avg_rating:
        highest_key = book
        highest_avg_rating = book.get_average_rating()
    return highest_key

  def most_positive_user(self):
    highest_user = ""
    highest_avg_rating = float("-inf")
    for user in self.users.values():
      if user.get_average_rating() > highest_avg_rating:
        highest_user = user
        highest_avg_rating = user.get_average_rating()
    return highest_user

  def get_n_most_read_books(self, n):
    sorted_book_library = []
    book_read_count = float("-inf")
    for key, value in self.books.items():
      if value >= book_read_count:
        beg_element = []
        beg_element.append([key, value])
        sorted_book_library = beg_element + sorted_book_library
        book_read_count = value
      else:
        sorted_book_library.append([key, value])
    return sorted_book_library[:n]

  def get_n_most_prolific_readers(self, n):
    sorted_readers = []
    book_read_count = float("-inf")
    for user in self.users.values():
      if len(user.books) >= book_read_count:
        beg_element = []
        beg_element.append([user])
        sorted_readers = beg_element + sorted_readers
        book_read_count = len(user.books)
      else:
        sorted_readers.append([user])
    return sorted_readers[:n]
