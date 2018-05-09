# -*- coding: utf-8 -*-
# David Han - dth2126
# Put the use case you chose here. Then justify your database choice:
# I chose the HackerNews use-case and implemented using MongoDB. MongoDB was a good choice because it's better for larger datasets rather than 
#using something like Redis. 

# Explain what will happen if coffee is spilled on one of the servers in your cluster, causing it to go down.
# Then the information on that server will not be able to be displayed. However, since Mongo supports replication, we may be able to 
# be fault tolerant since the secondary would become the new primary and support the application.

# What data is it not ok to lose in your app? What can you do in your commands to mitigate the risk of lost data?
# In this app, it's not okay to lose really any data as it is all important. Commands to mitigate the risk of lost data would include
# basically ones that focus on connecting to a replica set like MongoClient('localhost', replicaset='foo'),MongoClient('localhost:27018', replicaset='foo')...
#

#OBJECTS

# Users:
# 	"David Han"
# 	"Tracy Han"
# 	"John Han"

# Articles:
# 	"Subscription Hell"
# 	"Gitea: Open source, self-hosted GitHub alternative"
# 	"Origins of the finger command (1990)"
# 	"NASA advisers say SpaceX rocket technology could put lives at risk"
# 	"Researchers have developed a water-based battery to store solar and wind energy"

# Article Comments:
# 	"Awesome"
# 	"Interesting"
# 	"Lol"
# 	"Woah"
# 	"Damn"

# Jobs:
# 	"The Muse Is Hiring a PM for Data and Analytics"
# 	"VoiceOps is hiring in SF to build AI for B2B voice data"
# 	"Razorpay (YC W15) Is Hiring an Senior / Principal Engineer in Bangalore"
# 	"Well-capitalized startup seeks talented engineers","link":"flexport.com"
# 	"PlanGrid (YC W12) Is Hiring Front End and Data Engineers to Modernize Contruction"

# Ask Forum:
# 	"How do you benefit from Hacker News?"
# 	"Is Electron really that bad for desktop apps?"
# 	"What problem in your industry is a potential startup?"
# 	"Startup to enterprise and back to startups – how?"
# 	"What Are SaaS Adoption Hurdles for Large Enterprises?"

# Ask Forum Comments:
# 	"haha"
# 	"You don't benefit"
# 	"healthcare"
# 	"fintech"
# 	"go read a book"

#Relationships defined in schema.

#Make sure to run "mongo" before running "python final_project.py". 

import pymongo
import datetime
from pymongo import MongoClient
from pprint import pprint
from bson.binary import Binary


# Table 1: Articles

def create_articles(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.articles.insert_many([
		{"a_id": 1, "title":"Subscription Hell", "link":"https://techcrunch.com/2018/05/06/subscription-hell/", "points":10,"timedate":d},
		{"a_id": 2, "title":"Gitea: Open source, self-hosted GitHub alternative", "link":"https://gitea.io/en-US/", "points":2,"timedate":d},
		{"a_id": 3, "title":"Origins of the finger command (1990)", "link":"https://groups.google.com/forum/#!msg/alt.folklore.computers/IdFAN6HPw3k/Ci5BfN8i26AJ", "points":100,"timedate":d},
		{"a_id": 4, "title":"NASA advisers say SpaceX rocket technology could put lives at risk", "link":"http://www.chicagotribune.com/news/nationworld/ct-nasa-spacex-rocket-elon-musk-20180505-story.html", "points":80,"timedate":d},
		{"a_id": 5, "title":"Researchers have developed a water-based battery to store solar and wind energy", "link":"https://news.stanford.edu/2018/04/30/new-water-based-battery-offers-large-scale-energy-storage/", "points":30,"timedate":d}
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
		{"ask_id":1,"title":"How do you benefit from Hacker News?","link":"https://news.ycombinator.com/item?id=17005203","points":30,"timedate":d},
		{"ask_id":2,"title":"Is Electron really that bad for desktop apps?","link":"https://news.ycombinator.com/item?id=17005551","points":10,"timedate":d},
		{"ask_id":3,"title":"What problem in your industry is a potential startup?","link":"https://news.ycombinator.com/item?id=16995260","points":3,"timedate":d},
		{"ask_id":4,"title":"Startup to enterprise and back to startups – how?","link":"https://news.ycombinator.com/item?id=16991101","points":58,"timedate":d},
		{"ask_id":5,"title":"What Are SaaS Adoption Hurdles for Large Enterprises?","link":"https://news.ycombinator.com/item?id=17006078","points":139,"timedate":d},
	])

# Table 5: Ask Forum Comments
def create_askcomments(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.askcomments.insert_many([
		{"c_id":1,"ask_id":1,"u_id":1,"timedate":d,"comment":"haha"},
		{"c_id":2,"ask_id":1,"u_id":1,"timedate":d,"comment":"You don't benefit"},
		{"c_id":3,"ask_id":3,"u_id":3,"timedate":d,"comment":"healthcare"},
		{"c_id":4,"ask_id":3,"u_id":2,"timedate":d,"comment":"fintech"},
		{"c_id":5,"ask_id":4,"u_id":3,"timedate":d,"comment":"go read a book"}
	])

# Table 6: Users
def create_users(db):
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.users.insert_many([
		{"u_id":1,"name":"David Han","pub_askforum":[],"pub_jobs":[],"pub_articles":[],"article_upvoted":[],"ask_upvoted":[],"article_comments_id":[1,2],"ask_comments_id":[1,2]},
		{"u_id":2,"name":"Tracy Han","pub_askforum":[],"pub_jobs":[],"pub_articles":[],"article_upvoted":[],"ask_upvoted":[],"article_comments_id":[4],"ask_comments_id":[4]},
		{"u_id":3,"name":"John Han","pub_askforum":[],"pub_jobs":[],"pub_articles":[],"article_upvoted":[],"ask_upvoted":[],"article_comments_id":[3,5],"ask_comments_id":[3,5]},
	])

def getUser(db,u_id):
	d = db.users.find_one({"u_id": u_id})
	return d["name"]

# Action 1: Publish an article
def publish_article(db,title,link,u_id):
	a = db.articles.find_one(sort=[("a_id", -1)])
	newID = a["a_id"] + 1
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.articles.insert_one(
		{"a_id": newID, "title":title, "link":link, "points":0,"timedate":d},
	)
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "pub_articles" : newID} } )
	return newID

# Action 2: Comment an article
def comment_article(db,a_id,u_id,comment):
	a = db.acomments.find_one(sort=[("c_id", -1)])
	newID = a["c_id"] + 1
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.acomments.insert_one(
		{"c_id":newID,"a_id":a_id,"u_id":u_id,"timedate":d,"comment":comment},
	)
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "article_comments_id" : newID} } )
	return newID


# Action 3: List 5 Highest Voted Articles
def highest_voted_articles(db):
	res = db.articles.find(sort=[("points", -1)]).limit(5)
	print("5 HIGHEST VOTED ARTICLES")
	for ele in res:
		print "ID:",ele["a_id"],"|","Title:",ele["title"],"|","Points:",ele["points"]
		comments = db.acomments.find(({"a_id": ele["a_id"]})).sort("c_id")
		print "COMMENTS:"
		for c in comments:
			print "	", "\'",c["comment"],"\'","by",getUser(db,c["u_id"])

# Action 4: Up vote an article
def upvote_article(db,a_id,u_id):
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "article_upvoted" : a_id} } )
	db.articles.update({ "a_id" : a_id }, { "$inc" :{'points': 1}})

# Action 5: Publish a job
def publish_job(db,title,link,u_id):
	a = db.jobs.find_one(sort=[("a_id", -1)])
	newID = a["j_id"] + 1
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.jobs.insert_one(
		{"j_id": newID, "title":title, "link":link,"timedate":d},
	)
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "pub_jobs" : newID} } )
	return newID


# Action 6: Publish ask forum
def publish_askforum(db,title,link,u_id):
	a = db.askforum.find_one(sort=[("a_id", -1)])
	newID = a["ask_id"] + 1
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.askforum.insert_one(
		{"ask_id": newID, "title":title, "link":link,"points":0,"timedate":d},
	)
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "pub_askforum" : newID} } )
	return newID


# Action 7: Upvote an ask forum
def upvote_askforum(db,ask_id,u_id):
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "ask_upvoted" : ask_id} } )
	db.askforum.update({ "ask_id" : ask_id }, { "$inc" :{'points': 1}})


# Action 8: List 5 Highest Voted Ask Forums
def highest_voted_forums(db):
	res = db.askforum.find(sort=[("points", -1)]).limit(5)
	print("5 HIGHEST VOTED ASK FORUMS")
	for ele in res:
		print "ID:",ele["ask_id"],"|",ele["title"],ele["points"]

		# print "ID:",ele["a_id"],"|","Title:",ele["title"],"|","Points:",ele["points"]
		comments = db.askcomments.find(({"ask_id": ele["ask_id"]})).sort("c_id")
		print "COMMENTS:"
		for c in comments:
			print "	", "\'",c["comment"],"\'","by",getUser(db,c["u_id"])

# Action 9: Comment an ask forum
def comment_askforum(db,ask_id,u_id,comment):
	a = db.askcomments.find_one(sort=[("c_id", -1)])
	newID = a["c_id"] + 1
	d = datetime.datetime.now().strftime("%Y%m%d")
	db.askcomments.insert_one(
		{"c_id":newID,"ask_id":ask_id,"u_id":u_id,"timedate":d,"comment":comment},
	)
	db.users.update( { "u_id" : u_id }, { "$addToSet" : { "ask_comments_id" : newID} } )
	return newID

# Action 9: Get all User info
def user_info(db,u_id):
	u = db.users.find_one({"u_id": u_id})
	# print "User ID:",u_id 
	print u["name"]
	print "-------"
	print "PUBLISHED Ask Forum:"
	for i in u["pub_askforum"]:
		print getAskForumTitle(db,i)
	print "-------"
	print "PUBLISHED Jobs:"
	for i in u["pub_jobs"]:
		print getJobTitle(db,i)
	print "-------"
	print "PUBLISHED Articles:"
	for i in u["pub_articles"]:
		print getArticleTitle(db,i)
	print "-------"
	print "UPVOTES in Ask Forum"
	for i in u["article_upvoted"]:
		print getAskForumTitle(db,i)
	print "-------"
	print "UPVOTES in Articles"
	for i in u["article_upvoted"]:
		print getArticleTitle(db,i)
	print "-------"
	print "COMMENTS in Ask Forum"
	for i in u["ask_comments_id"]:
		t = getAskForumComment(db,i)
		print "Commented:","\'",t[0],"\'","in Ask Forum:",getAskForumTitle(db,t[1])
	print "-------"
	print "COMMENTS in Articles"
	for i in u["article_comments_id"]:
		t = getArticleComment(db,i)
		print "Commented:","\'",t[0],"\'","in Article:",getArticleTitle(db,t[1])
	print "-------"

def getArticleTitle(db,a_id):
	d = db.articles.find_one({"a_id": a_id})
	return d["title"]
def getJobTitle(db,j_id):
	d = db.jobs.find_one({"j_id": j_id})
	return d["title"]
def getAskForumTitle(db,ask_id):
	d = db.askforum.find_one({"ask_id": ask_id})
	return d["title"]
def getAskForumComment(db,c_id):
	d = db.askcomments.find_one({"c_id": c_id})
	return (d["comment"],d["ask_id"])
def getArticleComment(db,c_id):
	d = db.acomments.find_one({"c_id": c_id})
	return (d["comment"],d["a_id"])



###TESTING

client = MongoClient("mongodb://localhost")
print("connected")
if "hnews" in client.database_names():
	client.drop_database('hnews')

db = client.hnews
create_users(db)
create_articles(db)
create_acomments(db)
create_jobs(db)
create_askforum(db)
create_askcomments(db)

# print("---------USERS-----------")
# res = db.users.find()
# for ele in res:
# 	pprint(ele)

publish_article(db,"new_article","new_link",1)
comment_article(db,1,3,"nah")
comment_askforum(db,1,3,"I don't believe that's correct")
upvote_article(db,2,1)
publish_job(db,"new_job","new_link",1)
publish_askforum(db,"What is life?","new_link",1)
upvote_askforum(db,5,1)

highest_voted_articles(db)
print
highest_voted_forums(db)
print
user_info(db,1)
print
user_info(db,2)
print
user_info(db,3)

