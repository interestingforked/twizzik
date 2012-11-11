import tweepy
import webbrowser
import twizzik_db


print twizzik_db.all_users()

# Make constants to hold values of our keys
CONSUMER_KEY = "wleBMXN8U0vYy0iyJqUccA"
CONSUMER_SECRET = "SDa0M6xromPe5nmHxo17AX1r9zEm7bDXBn52JG4EB9A"
ACCESS_TOKEN = "89395035-49W6pg7iFpQYbUrsoarGDKWrwgjyKKeqiDNMq0Bd6"
ACCESS_SECRET = "6C5qOk95i09IiXiQpQH73qMkreTQmL3c3T4oMfk8"


# set auth variables
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)

# create a new api
api = tweepy.API(auth)

# create an instance of the twitter api class
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth_url = auth.get_authorization_url()

# open the window for authorization, twitter will generate the pin
print "Enter " + auth_url + " in a browser window and paste the pin below\n"

# get the pin number from the user
verifier = raw_input('PIN: ').strip()
auth.get_access_token(verifier)

# get the access key and secret returned from twitter
access_key = auth.access_token.key
access_secret = auth.access_token.secret

# set authorization token
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

# make a tweet
def send_tweet():
    tweet_text = raw_input("Enter your tweet content below... Only the first 140 characters will be used.\n>>> ")
    api.update_status(tweet_text[0:140])
    print "You tweeted \n'" + tweet_text[0:140] + "'"
    restart = raw_input("Do you want to tweet again? (Y/N)\n>>> ")
    if restart.lower() == "y":
        send_tweet()
    else:
        print "Returning to the Main Menu...\n"

# search twitter
def keyword_follow():
    search_phrase = raw_input("What do you want to search for?\n>>> ").strip()
    search_number = raw_input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    for i in search_result:
        print i.from_user + " said " + i.text + "\n"
        to_follow = raw_input("Do you want to follow " + i.from_user + "? (Y/N)\n>>> ")
        if to_follow.lower() == "n":
            print i.from_user + " was not followed!"
        else:
            api.create_friendship(i.from_user)
            print "You followed " + i.from_user + "!\n"
            
    # check if the user wants to search again
    restart = raw_input("Do you want to search again? (Y/N)\n>>> ")
    if restart.lower() == "n":
        print "Returning to the Main Menu...\n"
    else:
        return keyword_follow()
    
def keyword_retweet():
    search_phrase = raw_input("What do you want to search for?\n>>> ").strip()
    search_number = raw_input("How many results do you want to return?\n>>> ")
    search_result = api.search(search_phrase, rpp=search_number)
    for i in search_result:
        print i.from_user + " said " + i.text + "\n"
        to_retweet = raw_input("Do you want to retweet" + i.from_user + "? (Y/N)\n>>> ")
        if to_retweet.lower() == "n":
            print i.from_user + " was not retweeted!"
        else:
            api.retweet(i.id)
            print "Retweeted!\n"
            again = raw_input("See more? (Y/N)\n>>> ")
            if again.lower() == "n":
                break       
    # check if the user wants to search again
    restart = raw_input("Do you want to search again? (Y/N)\n>>> ")
    if restart.lower() == "n":
        print "Returning to the Main Menu...\n"
    else:
        return keyword_retweet()

def mass_unfollow():
    print "You can unfollow " + str(api.rate_limit_status()['remaining_hits']) + " people this hour...\n"
    print "Checking who doesn't follow you back. This will take a minute.\n"
    # first, create some lists to hold the followers
    followers = []
    friends = []
    
    # we have to use a Cursor for pagination purposes
    for follower in tweepy.Cursor(api.followers).items():
        followers.append(follower)

    for friend in tweepy.Cursor(api.friends).items():
        friends.append(friend)
        
    # create a non_reciprocals list, these are non-followers (set - set)
    non_reciprocal = list(set(friends) - set(followers))
    print str(len(non_reciprocal)) + " non-reciprocal followers.\n"

    # first, double check that we want to unfollow
    double_check = raw_input("Unfollow them? (Y/N) ***WARNING, THIS ACTION CANNOT BE UNDONE***\n>>> " )

    if double_check.lower() == "y":
        # count the number of people we unfollow, just for fun
        counter = 0
        for i in non_reciprocal:
            if api.rate_limit_status()['remaining_hits'] > 0:
                api.destroy_friendship(i.screen_name)
                print "Successfully unfollowed " + i.screen_name
            else:
                print "You ran out of hits! Try again in an hour!"
                break
            counter += 1
        print "You unfollowed " + str(counter) + " people!\n"
        print "Now returning to the Main Menu."
    else:
        print "Returning to the Main Menu...\n"
# whitelist functions
def whitelist():
    whitelist_selection = raw_input("(1)Add User | (2)Delete User | (3)Display Whitelist | (4)Back to Main\n>>> ")
    if whitelist_selection == "1":
	add_more = True
	while add_more == True:
            print "Add User"
            print "--------\n"
	    user_id = raw_input("User ID of the Member to ADD?\n>>> ")
	    screen_name = raw_input("Screen Name of the Member to ADD?\n>>> ")
	    twizzik_db.add_whitelist_user(user_id,screen_name)
            check = raw_input("Add Another User? (Y/N)\n>>>")
	    if check != "y":
                add_more = False
		print "Returning to Main Menu\n\n"
    else:
	print "Function Coming Soon!"	              

# create the menu
keep_running = True
while keep_running:
    print "Main Menu"
    print "---------\n"
    selection = raw_input("(1)Tweet | (2)Keyword Follow | (3)Keyword Retweet | (4)Mass Unfollow | (5)White List | (6)End\n\n>>> ")
    if selection == "1":
        print "New Tweet"
        print "---------\n"
        send_tweet()
    elif selection == "2":
        print "Keyword Follow"
        print "--------------\n"
        keyword_follow()
    elif selection == "3":
        print "Keyword Retweet"
        print "---------------\n"
        keyword_retweet()
    elif selection == "4":
        print "Mass Unfollow"
        print "-------------\n"
        print "WARNING: MASS UNFOLLOW IS AGAINST THE TOS OF TWITTER. YOU'VE BEEN WARNED\n"
        mass_unfollow()
    elif selection == "5":
	print "White List"
	print "----------\n"
	whitelist()
    else:
        print "BYE!\n\n"
        keep_running = False
