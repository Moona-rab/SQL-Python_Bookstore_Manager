# Creating ebookstore database
# The program should present the user with the following menu:
# 1. Enter book
# 2. Update book
# 3. Delete book
# 4. Search books
# 0. Exit
# The program should perform the function that the user selects  

import sqlite3
import os

# create forlder if i does not exist
if not os.path.exists("data"):
    os.makedirs("data")




def book_id():
    '''
    Function to enter book id
    '''
    idx = int(input('Enter Book ID: '))
    return idx

def show_data():
    '''
    Function to show all database rows from table
    '''

    cursor.execute('''SELECT * FROM ebookstore''')
    print('\nid : Title: Author: Quantity')
    for row in cursor:
    
        
        print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3],))
        db.commit()     
    print("\n")    


try:
    db = sqlite3.connect('data/ebookstore_db')
    
    # Get a cursor object
    cursor = db.cursor()

    # Create a table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS ebookstore(id INTEGER PRIMARY KEY AUTOINCREMENT, Title TEXT, Author TEXT,
                        Qty INTEGER)
        ''')
 
    db.commit()

    # Create database values
    cursor = db.cursor()

    id1 = 3001
    title1 = 'A Tale of Two Cities'
    author1 = 'Charles Dickens'
    qty1 = 30

    id2 = 3002
    title2 = "Harry Potter and the Philosopher's Stone"
    author2 = 'J.K. Rowling'
    qty2 = 40

    id3 = 3003
    title3 = 'The Lion, the Witch and the Wardrobe'
    author3 ='C. S. Lewis'
    qty3 = 25

    id4 = 3004
    title4 = 'The Lord of the Rings'
    author4 = 'J.R.R Tolkien'
    qty4 = 37

    id5 = 3005
    title5 = 'Alice in Wonderland'
    author5 = 'Lewis Carroll'
    qty5 = 12

    # Insert values to table
    ebookstore_ = [(id1,title1,author1,qty1),(id2,title2,author2,qty2),(id3,title3,author3,qty3),(id4,title4,author4,qty4),(id5,title5,author5,qty5)]
    cursor.executemany(''' INSERT INTO ebookstore(id, title, author, qty) VALUES(?,?,?,?)''',
    ebookstore_)
    
    db.commit()

    # Create a menu
    menu = {}
    menu['1']="Enter book."
    menu['2']="Update book."
    menu['3']="Delete book"
    menu['4']="Search book"
    menu['0']="Exit"

    while True:
        options = menu.keys()
        print('\nMenu:')
        for entry in options:
            print(entry, menu[entry])
     
        selection = input("\nPlease select an option from the menu: ")

        # Enter a book
        if selection =='1':
            title = input('Enter Title: ')
            author = input('Enter Author: ')
            # handle user error with try-except block
            try:
                quantity = int(input('Enter Quantity: '))
            except ValueError:
                    print("Invalid input. Please try again!")
                    continue

            cursor.execute('''INSERT INTO ebookstore(title,author,qty)
            VALUES(:title,:author,:qty)''',
            {'title':title,'author':author,'qty':quantity})
            print("Book added!\n")
            show_data()
            db.commit()
  
        # Update a book
        elif selection == '2':

            # returns everything in the DB
            show_data()

            column = input('What would you like to change? Enter either title(t), author(a), quantity(q) or press (r) to return to main menu: ')     
            # using .lower() function to handle case sensitivity
            column = column.lower()
      
            if column == 't':
                new_title = input('Enter New Title: ')
                # call idx funcion
                # handle user error with try-except block
                try:
                    idx = book_id()
                except ValueError:
                    print("Invalid input. Please try again!")
                    continue
                cursor.execute('''UPDATE ebookstore SET title = ? WHERE id = ? ''', (new_title,
                idx))
                print("Book updated!\n")
                db.commit()

            elif column == 'a':
                new_author = input('Enter New Auhor: ')
                # call idx funcion
                # handle user error with try-except block
                try:
                    idx = book_id()
                except ValueError:
                    print("Invalid input. Please try again!")
                    continue
                cursor.execute('''UPDATE ebookstore SET author = ? WHERE id = ? ''', (new_author,
                idx))
                print("Book updated!\n")
                db.commit()

            elif column == 'q':
                new_quantity = input('Enter New Quantity: ')
                # call idx funcion
                # handle user error with try-except block
                try:
                    idx = book_id()
                except ValueError:
                    print("Invalid input. Please try again!")
                    continue
                cursor.execute('''UPDATE ebookstore SET qty = ? WHERE id = ? ''', (new_quantity,
                idx))
                print("Book updated!\n")
                db.commit()
            
            elif column == 'r':
                continue
          
           # handle user error by returning user to menu if input is outside the specified parameters
            else:
                print("invalid input. Please try again!")
              

        # Delete a book
        elif selection == '3':
            # call idx funcion
            # handle user error with try-except block
            try:
                # returns everything in the DB
                show_data()

                idx = book_id()
            except ValueError:
                print("Invalid input. Please try again!")
                continue
            cursor.execute('''DELETE FROM ebookstore WHERE id = ? ''', (idx,))
            db.commit()
            print("Book deleted!\n")
        
        # Search a book
        elif selection == '4':

            # returns everything in the DB
            show_data()
            
            column = input('How would you like to search? Enter either id(i), title(t), author(a), quantity(q) or press (r) to return to main menu: ' )
            # using .lower() function to handle case sensitivity
            column = column.lower()
            
            if column == 't':             
                title = input('Enter Title: ')
                # use 'LIKE' function to allow for faster search and user variance               
                cursor.execute('''SELECT id, title, author, qty FROM ebookstore WHERE title LIKE ? ''', ('%'+title+'%',))
                                 
                for row in cursor:
                # row[0] returns the first column in the query (name)
                    print('\nid : Title: Author: Quantity')
                    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3],))
                    db.commit
   
            elif column == 'a':
                author = input('Enter Author: ')
                # use 'LIKE' function to allow for faster search and user variance
                cursor.execute('''SELECT id, title, author, qty FROM ebookstore WHERE author LIKE ? ''', ('%'+author+'%',))
                for row in cursor:
                # row[0] returns the first column in the query (name)
                    print('\nid : Title: Author: Quantity')
                    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3],))
                    db.commit()

            elif column == 'q':
                # handle user error with try-except block
                try:
                    quantity = int(input('Enter Quantity: '))
                except ValueError:
                    print("Invalid input. Please try again!")
                    continue
                cursor.execute('''SELECT id, title, author, qty FROM ebookstore WHERE qty = ? ''', (quantity,))
                for row in cursor:
                # row[0] returns the first column in the query (name)
                    print('\nid : Title: Author: Quantity')
                    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3],))
                    db.commit()
            
            elif column == 'i':
                idx = book_id()
                cursor.execute('''SELECT id, title, author, qty FROM ebookstore WHERE id = ? ''', (idx,))
                for row in cursor:
                # row[0] returns the first column in the query (name)
                    print('{0} : {1} : {2} : {3}'.format(row[0], row[1], row[2], row[3],))
                    db.commit()

            elif column == 'r':
                continue

            # handle user error by returning user to menu if input is outside the specified parameters
            else:
                print("input does not exist in database. Please try again!")
            
        
        elif selection == '0':
            break
        
        # handle user error by returning user to menu if input is outside the specified parameters
        else:
            print("Invalid input. Please try again using menu options!")


    cursor.execute('''DROP TABLE ebookstore''')
    db.commit()

except Exception as e:
    # Roll back any change if something goes wrong
    db.rollback()
    raise e
finally:
    # Close the db connection
    db.close()