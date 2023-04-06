# import necessary modules
import sqlite3

# create a connection to the SQLite database
conn = sqlite3.connect('food_ordering_app.db')

# create a cursor object to execute SQL queries
c = conn.cursor()

# create a table to store food items
c.execute('''CREATE TABLE IF NOT EXISTS food_items
             (food_id INTEGER PRIMARY KEY,
              name TEXT,
              quantity TEXT,
              price REAL,
              discount REAL,
              stock INTEGER)''')

# define a function to add new food items
def add_food_item(name, quantity, price, discount, stock):
    # generate a new food ID
    c.execute('''SELECT MAX(food_id) FROM food_items''')
    max_id = c.fetchone()[0]
    food_id = max_id + 1 if max_id else 1

    # insert the new food item into the database
    c.execute('''INSERT INTO food_items (food_id, name, quantity, price, discount, stock)
                 VALUES (?, ?, ?, ?, ?, ?)''', (food_id, name, quantity, price, discount, stock))
    
    # commit the changes to the database
    conn.commit()
    print('New food item added successfully!')


# define a function to edit food items using food ID
def edit_food_item(food_id, name=None, quantity=None, price=None, discount=None, stock=None):
    # construct the update query
    update_query = '''UPDATE food_items SET '''
    update_values = []
    if name is not None:
        update_query += '''name = ?, '''
        update_values.append(name)
    if quantity is not None:
        update_query += '''quantity = ?, '''
        update_values.append(quantity)
    if price is not None:
        update_query += '''price = ?, '''
        update_values.append(price)
    if discount is not None:
        update_query += '''discount = ?, '''
        update_values.append(discount)
    if stock is not None:
        update_query += '''stock = ?, '''
        update_values.append(stock)
    update_query = update_query[:-2] + ''' WHERE food_id = ?'''
    update_values.append(food_id)
    
    # execute the update query
    c.execute(update_query, tuple(update_values))
    
    # commit the changes to the database
    conn.commit()
    print('Food item updated successfully!')

# define a function to view the list of all food items
def view_food_items():
    c.execute('''SELECT * FROM food_items''')
    rows = c.fetchall()
    for row in rows:
        print(row)

# define a function to remove a food item from the menu using food ID
def remove_food_item(food_id):
    c.execute('''DELETE FROM food_items WHERE food_id = ?''', (food_id,))
    conn.commit()
    print('Food item removed successfully!')

# test the functions
add_food_item('Tandoori Chicken', '4 pieces', 240, 0, 100)
add_food_item('Vegan Burger', '1 piece', 320, 0.1, 50)
view_food_items()
edit_food_item(1, name='Tandoori Chicken (4 pieces)')
view_food_items()
remove_food_item(2)
view_food_items()

# close the database connection
conn.close()
