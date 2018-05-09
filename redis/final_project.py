# David Han - dth2126
# Put the use case you chose here. Then justify your database choice:
# 
#
# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
#
#
# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
#
#

import pymongo
import datetime
from pymongo import MongoClient
from pprint import pprint
from bson.binary import Binary


# Table 1: Articles

def create_articles(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.articles.insert_many([
		{"a_id": 1, "title":"Subscription Hell", "link":"https://techcrunch.com/2018/05/06/subscription-hell/", "points":0,"timedate":d},
		{"a_id": 2, "title":"Gitea: Open source, self-hosted GitHub alternative", "link":"https://gitea.io/en-US/", "points":0,"timedate":d},
		{"a_id": 3, "title":"Origins of the finger command (1990)", "link":"https://groups.google.com/forum/#!msg/alt.folklore.computers/IdFAN6HPw3k/Ci5BfN8i26AJ", "points":0,"timedate":d},
		{"a_id": 4, "title":"NASA advisers say SpaceX rocket technology could put lives at risk", "link":"http://www.chicagotribune.com/news/nationworld/ct-nasa-spacex-rocket-elon-musk-20180505-story.html", "points":0,"timedate":d},
		{"a_id": 5, "title":"Researchers have developed a water-based battery to store solar and wind energy", "link":"https://news.stanford.edu/2018/04/30/new-water-based-battery-offers-large-scale-energy-storage/", "points":0,"timedate":d}
	])

# Table 2: Article Comments
def create_acomments(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.acomments.insert_many([
		{"c_id":1,"a_id":1,"u_id":1,"timedate":d,"comment":"Awesome!"},
		{"c_id":2,"a_id":1,"u_id":1,"timedate":d,"comment":"Interesting read"},
		{"c_id":3,"a_id":3,"u_id":3,"timedate":d,"comment":"Lol"},
		{"c_id":4,"a_id":3,"u_id":2,"timedate":d,"comment":"Woah"},
		{"c_id":5,"a_id":4,"u_id":3,"timedate":d,"comment":"Damn"}
	])


# Table 3: Jobs
def create_jobs(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.jobs.insert_many([
		{"j_id":1,"title":"The Muse Is Hiring a PM for Data and Analytics","link":"themuse.com","timedate":d},
		{"j_id":2,"title":"VoiceOps is hiring in SF to build AI for B2B voice data","link":"voiceops.com","timedate":d},
		{"j_id":3,"title":"Razorpay (YC W15) Is Hiring an Senior / Principal Engineer in Bangalore","link":"razorpay.com","timedate":d},
		{"j_id":4,"title":"Well-capitalized startup seeks talented engineers","link":"flexport.com","timedate":d},
		{"j_id":5,"title":"PlanGrid (YC W12) Is Hiring Front End and Data Engineers to Modernize Contruction","link":"plangrid.com","timedate":d}
	])

# Table 4: Ask Forum
def create_askforum(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.askforum.insert_many([
		{"ask_id":1,"title":"How do you benefit from Hacker News?","link":"https://news.ycombinator.com/item?id=17005203","points":0,"timedate":d},
		{"ask_id":2,"title":"Is Electron really that bad for desktop apps?","link":"https://news.ycombinator.com/item?id=17005551","points":0,"timedate":d},
		{"ask_id":3,"title":"What problem in your industry is a potential startup?","link":"https://news.ycombinator.com/item?id=16995260","points":0,"timedate":d},
		{"ask_id":4,"title":"Startup to enterprise and back to startups – how?","link":"https://news.ycombinator.com/item?id=16991101","points":0,"timedate":d},
		{"ask_id":5,"title":"What Are SaaS Adoption Hurdles for Large Enterprises?","link":"https://news.ycombinator.com/item?id=17006078","points":0,"timedate":d},
	])

# Table 5: Ask Forum Comments
def create_askcomments(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.askcomments.insert_many([
		{"c_id":1,"j_id":1,"u_id":1,"timedate":d,"comment":"haha"},
		{"c_id":2,"j_id":1,"u_id":1,"timedate":d,"comment":"You don't benefit"},
		{"c_id":3,"j_id":3,"u_id":3,"timedate":d,"comment":"healthcare"},
		{"c_id":4,"j_id":3,"u_id":2,"timedate":d,"comment":"fintech"},
		{"c_id":5,"j_id":4,"u_id":3,"timedate":d,"comment":"go read a book"}
	])

# Table 6: Users
def create_users(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.users.insert_many([
		{"u_id":1,"name":"David Han","article_upvoted":[],"ask_upvoted":[],"article_comments_id":[1,2],"ask_comments":[1,2]},
		{"u_id":2,"name":"Tracy Han","article_upvoted":[],"ask_upvoted":[],"article_comments_id":[4],"ask_comments":[4]},
		{"u_id":3,"name":"John Han","article_upvoted":[],"ask_upvoted":[],"article_comments_id":[3,5],"ask_comments":[3,5]},
	])

pprint(db.users)

# # Action 1: Publish an article
# def action_sign_up(db, username="david", password="ilikemobike"):
# 	db.user.insert_one(
# 		{
# 			"username": username,
# 			"password": password,
# 			"deposit": 0
# 		},
# 	)


# Action 2: <describe the action here>


# Action 3: <describe the action here>


# Action 4: <describe the action here>


# Action 5: <describe the action here>


# Action 6: <describe the action here>


# Action 7: <describe the action here>


# Action 8: <describe the action here>



