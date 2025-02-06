from flask import Flask, render_template
import util


# create an application instance
# all requests it receives from clients to this object for handling
# we are instantiating a Flask object by passing __name__ argument to the Flask constructor. 
# The Flask constructor has one required argument which is the name of the application package. 
# Most of the time __name__ is the correct value. The name of the application package is used 
# by Flask to find static assets, templates and so on.
app = Flask(__name__)

# evil global variables
# can be placed in a config file
# here is a possible tutorial how you can do this
username='raywu1990'
password='test'
host='127.0.0.1'
port='5432'
database='dvdrental'

# route is used to map a URL with a Python function
# complete address: ip:port/
# 127.0.0.1:5000/
@app.route('/')
# this is how you define a function in Python
def index():
    return render_template('index.html')


@app.route('/api/unique')
def api_unique():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    record = util.run_and_fetch_sql(cursor, "SELECT a.fruit_a AS unique_fruit_a, b.fruit_b AS unique_fruit_b FROM basket_a AS a FULL OUTER JOIN basket_b AS b ON a.fruit_a = b.fruit_b WHERE a.fruit_a IS NULL OR b.fruit_b IS NULL;")
    if isinstance(record, list):
        # this will return all column names of the select result table
        # ['customer_id','store_id','first_name','last_name','email','address_id','activebool','create_date','last_update','active']
        col_names = [desc[0] for desc in cursor.description]
        # only use the first five rows
        log = record[:10]
        # log=[[1,2],[3,4]]
        # disconnect from database
        util.disconnect_from_db(connection,cursor)
        # using render_template function, Flask will search
        # the file named index.html under templates folder
        return render_template('show.html', sql_table = log, table_title=col_names)

    else:
        # you can replace this part with a 404 page
        #print('Something is wrong with the SQL command')
        util.disconnect_from_db(connection,cursor)
        return render_template('showerror.html', message = record)

@app.route('/api/update_basket_a')
def update():
    # connect to DB
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    result = util.run_and_commit_sql(cursor, connection, "INSERT INTO basket_a (a, fruit_a) VALUES (5, 'Cherry');")
    if result == 1:
        message = "Success!"
    else:
        message = result
    util.disconnect_from_db(connection,cursor)
    return render_template('update.html', display_message = message)

@app.route('/api/reset/')
def reset():
    #connect to db
    cursor, connection = util.connect_to_db(username,password,host,port,database)
    # execute SQL commands
    CMD = """
        DROP TABLE IF EXISTS basket_a; CREATE TABLE basket_a (

        a INT PRIMARY KEY,

        fruit_a VARCHAR (100) NOT NULL

        );

        DROP TABLE IF EXISTS basket_b; CREATE TABLE basket_b (

            b INT PRIMARY KEY,

            fruit_b VARCHAR (100) NOT NULL

        );
        INSERT INTO basket_a (a, fruit_a)

        VALUES

            (1, 'Apple'),

            (2, 'Orange'),

            (3, 'Banana'),

            (4, 'Cucumber');

        INSERT INTO basket_b (b, fruit_b)

        VALUES

            (1, 'Orange'),

            (2, 'Apple'),

            (3, 'Watermelon'),

            (4, 'Pear');
        """
    result = util.run_and_commit_sql(cursor, connection, CMD)
    if result == 1:
        message = "Success!"
    else:
        message = result
    util.disconnect_from_db(connection,cursor)
    return render_template('reset.html', display_message = message)


if __name__ == '__main__':
	# set debug mode
    app.debug = True
    # your local machine ip
    ip = '127.0.0.1'
    app.run(host=ip)

