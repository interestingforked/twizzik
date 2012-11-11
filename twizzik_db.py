import MySQLdb as mdb
import sys

	
def add_tracking_user(user_id,screen_name):

    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')   
    cur = con.cursor()
    cur.execute("INSERT INTO `User_Tracking_Ids` (`id`,`screen_name`,`dt_added`) VALUES (%s,%s,CURDATE())",(user_id,screen_name))
    print "Added User to Tracking"

def all_tracking_user():

    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')
    cur = con.cursor()	
    cur.execute("SELECT * FROM `User_Tracking_Ids`")
    rows = cur.fetchall()
    for row in rows:
        print row

def all_user():
    
    '''selects all information from `User` table'''

    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')   
    cur = con.cursor()
    cur.execute("SELECT * FROM `User`")
    rows = cur.fetchall()
    desc = cur.description      
    print "\n%15s %15s %15s %15s" % (desc[0][0],desc[1][0],desc[2][0],desc[3][0])
    for row in rows:
        print row

def add_whitelist_user(user_id,screen_name,my_name):
    
    '''adds a user to the whitelist'''    
    
    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')   
    cur = con.cursor()
    cur.execute("INSERT INTO `White_List` (`id`,`screen_name`,`dt_whitelisted`,`whitelisted_by`) VALUES (%s,%s,CURDATE(),%s)",(user_id,screen_name,my_name))
    print "Added User to White List for " + my_name + "\n"

def all_whitelist_user():

	con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')
	cur = con.cursor()
	cur.execute("SELECT * FROM `White_List`")
	rows = cur.fetchall()
	desc = cur.description
	print "\n%15s %15s %15s %15s" % (desc[0][0],desc[1][0],desc[2][0],desc[3][0])
	print "-" * 65
	for row in rows:
		print "%15s %15s %15s %15s" % row
        print "-" * 65 + "\n"

def check_whitelist(non_reciprocal):
    
    '''checks whitelist against non_reciprocal followers list'''
    con = mdb.connect('localhost','twizzik','twIzz1k','twizzik')
    cur = con.cursor()
    cur.execute("SELECT `id` FROM `White_List`")
    whitelist_users = []
    rows = cur.fetchall()
    for row in rows:
        whitelist_users.append(row)
    for users in whitelist_users:
        print users

 
   





    
