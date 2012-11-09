import MySQLdb as mdb
import sys


def all_users():
    
    '''selects all information from `Users` table'''

    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')
    
    with con:
        # create a new cursor object 
        cur = con.cursor()
	# execute the query
        cur.execute("SELECT * FROM `Users`")
        # get all rows
        rows = cur.fetchall()
	# get headers from cursor object
        desc = cur.description
	# print out the headers (for now)
	col_name_list = [tuple[0] for tuple in cur.description]	
	# print out our rows of data		 
	for row in rows:
            print row

def add_whitelist_user(user_id,screen_name):
    
    '''adds a user to the whitelist'''
     
    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')
    
    with con:
	# create a new cursor object
	cur = con.cursor()
	# execute the query
        try:
            cur.execute("""INSERT INTO `White_List` (`id`,`screen_name`,`dt_whitelisted`) VALUES (%s,%s,CURDATE())""",(user_id,screen_name))
	    con.commit()
	    print "Added User to White List"
	except:
	    con.rollback()
	    print "Failed to Add User to White List"

