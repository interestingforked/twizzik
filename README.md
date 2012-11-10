twizzik
=======
##Functions

_Current supported functions include:_

**twizzik.py**  
 ========

`send_tweet()` - sends tweets from the command line  

`keyword_follow()` - allows for searching the _twittersphere_ and following other users based on those tweets  

`keyword_retweet()` - same as `keyword_follow()` but adds the ability to retweet  

`mass_unfollow()` - checks the authenticated user's followers and following and automatically unfollows non-reciprocal users  

`add_whitelist_user()` - This will add a user to a whitelist of users - useful for `mass_unfollow()`  

`all_whitelist_user()` - This will fetch all of the users from the `twizzik.White_List` table  

**twizzik_db.py**  
 ===========  

_Upcoming functions include:_  

`del_whitelist_user()` - This will remove a user from the whitelist of the Authenticated user

`add_blacklist_user()` - This will add a user to a blacklist of members who won't show up in any search results

`del_blacklist_user()` - This will remove a user from the blacklist of the Authenticated user  

`get_blacklist()` - This will fetch all of the users from the `twizzik.Black_List` table  

`add_track_user()` - This will add a user to the list of members to be tracked (future)  

`del_track_user()` - This will remove a user to the list of members to be tracked (future)  

`get_tracked_users()` - This will fetch all of the users from the `twizzik.User_Tracking` table  

##Databases
```
/* This is the Users Table */
mysql> SHOW COLUMNS FROM `twizzik`.`Users`;
+-----------------------+--------------+------+-----+---------+-------+
| Field                 | Type         | Null | Key | Default | Extra |
+-----------------------+--------------+------+-----+---------+-------+
| created_at            | varchar(255) | NO   |     | NULL    |       |
| default_profile_image | tinyint(1)   | NO   |     | 0       |       |
| description           | varchar(255) | YES  |     | NULL    |       |
| favourites_count      | int(11)      | NO   |     | 0       |       |
| followers_count       | int(11)      | NO   |     | 0       |       |
| friends_count         | int(11)      | NO   |     | 0       |       |
| id                    | bigint(20)   | NO   |     | NULL    |       |
| location              | varchar(255) | YES  |     | NULL    |       |
| name                  | varchar(255) | NO   |     | NULL    |       |
| screen_name           | varchar(255) | NO   |     | NULL    |       |
| statuses_count        | int(11)      | NO   |     | 0       |       |
+-----------------------+--------------+------+-----+---------+-------+
11 rows in set (0.00 sec)

```
```
/* This is the Tweets Table */
mysql> SHOW COLUMNS FROM `twizzik`.`Tweets`;
+-------------------------+--------------+------+-----+---------+-------+
| Field                   | Type         | Null | Key | Default | Extra |
+-------------------------+--------------+------+-----+---------+-------+
| created_at              | varchar(255) | NO   |     | NULL    |       |
| favorited               | tinyint(1)   | YES  |     | NULL    |       |
| id                      | bigint(20)   | NO   |     | NULL    |       |
| in_reply_to_screen_name | varchar(255) | YES  |     | NULL    |       |
| retweet_count           | int(11)      | NO   |     | NULL    |       |
| retweeted               | tinyint(1)   | NO   |     | NULL    |       |
+-------------------------+--------------+------+-----+---------+-------+
6 rows in set (0.00 sec)
```
```
/* This is the White List Users Table */
mysql> SHOW COLUMNS FROM `twizzik`.`White_List`;
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| id             | bigint(20)   | NO   |     | NULL    |       |
| screen_name    | varchar(255) | NO   |     | NULL    |       |
| dt_whitelisted | date         | NO   |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
```
```
/* This is the Black List Users Table */
mysql> SHOW COLUMNS FROM `twizzik`.`Black_List`;
+----------------+--------------+------+-----+---------+-------+
| Field          | Type         | Null | Key | Default | Extra |
+----------------+--------------+------+-----+---------+-------+
| id             | bigint(20)   | NO   |     | NULL    |       |
| screen_name    | varchar(255) | NO   |     | NULL    |       |
| dt_blacklisted | date         | NO   |     | NULL    |       |
+----------------+--------------+------+-----+---------+-------+
3 rows in set (0.00 sec)
```
```
/* This is the User Tracking Table */
mysql> SHOW COLUMNS FROM `twizzik`.`User_Tracking`;
+------------------+--------------+------+-----+---------+-------+
| Field            | Type         | Null | Key | Default | Extra |
+------------------+--------------+------+-----+---------+-------+
| created_at       | date         | NO   |     | NULL    |       |
| favourites_count | int(11)      | NO   |     | NULL    |       |
| followers_count  | int(11)      | NO   |     | NULL    |       |
| friends_count    | int(11)      | NO   |     | NULL    |       |
| id               | bigint(20)   | NO   |     | NULL    |       |
| screen_name      | varchar(255) | NO   |     | NULL    |       |
| dt_updated       | date         | NO   |     | NULL    |       |
+------------------+--------------+------+-----+---------+-------+
7 rows in set (0.00 sec)
```


