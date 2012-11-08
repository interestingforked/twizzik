twizzik
=======

_Current supported functions include:_

**twizzik.py**  
 ========

`send_tweet()` - sends tweets from the command line  

`keyword_follow()` - allows for searching the _twittersphere_ and following other users based on those tweets  

`keyword_retweet()` - same as `keyword_follow()` but adds the ability to retweet.  

`mass_unfollow()` - checks the authenticated user's followers and following and automatically unfollows non-reciprocal users  

**twizzik_db.py**  
 ===========  

_Upcoming functions include:_  

`add_whitelist_user()` -  This will create a whitelist of users (for the authenticated user) that will not be unfollowed with the `mass_unfollow()` function.  

`del_whitelist_user()` -  This will remove a user from the whitelist of the Authenticated user.

`get_whitelist()` -  

`add_blacklist_user()` -  

`del_blacklist_user()` -  

`get_blacklist()` -  

`add_track_user()` -  

`del_track_user()` -  

`get_tracked_users()` -  

