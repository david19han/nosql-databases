import pymongo
from pymongo import MongoClient
import pprint

client = MongoClient()
database = client.test
m = database.movies
# pprint.pprint(m.find_one())
# print(m.count())

#A: Update to PENDING RATING
print("Part A:")
result = m.update_many({"genres":"Comedy","rated":"NOT RATED"}, {"$set": {"rated": "Pending rating"}})
print("Result matched:",result.matched_count)
print("Result modified:",result.modified_count)
print("--------------------------")


#B: Insert movie
print("Part B:")
insert_movie = m.insert_one(
  {
  "title" : "Blockers",
  "year" : 2018,
  "countries" : ["USA"],
  "genres" : ["Comedy"],
  "directors" : ["Kay Cannon"],
  "imdb" : {"id":  2531344, "rating": 6.6, "votes": 6361}
  }
)
print("Inserted movie ID:",insert_movie.inserted_id)
print("Inserted movie record:",m.find_one({"title":"Blockers"}))
print("--------------------------")


#C: Total Comedy
print("Part C:")
pipeline = [{"$unwind" : "$genres"},{"$match": {"genres" : "Comedy"}},{"$group": {"_id": "$genres", "count": {"$sum": 1}}}]
total_comedy = m.aggregate(pipeline)
print("Total Comedy:",list(total_comedy))
print("--------------------------")


#D: Use the aggregation framework to find the number of movies made in the country you were born in with a rating of "Pending rating".
print("Part D:")
birth_pipeline = [{"$unwind": "$genres"}, {"$unwind": "$countries"}, {"$match": {"genres": "Comedy", "countries": "USA", "rated": "Pending rating"}},
  {"$group": {"_id": {"Country": "$countries", "rating": "$rated"}, "count": {"$sum": 1}}}]
total_birth_comedy = m.aggregate(birth_pipeline)
print("Total Comedy in USA:",list(total_birth_comedy))
print("--------------------------")

#E: Use $lookup pipeline operator. Add some documents to another collection, and 
#then do an aggregation with the $lookup on a field that you define. The examples 
#fields can be anything, you just have to set up the data and return at least two results from the lookup.


database.customers2.insert([
   { "name" : "David", "location" : "California", "phone" : "6266641617" },
   { "name" : "Tracy", "location" : "North Carolina", "phone" : "6266645617" }
])

database.orders2.insert([
  { "c_name" : "David", "description": "apples", "amount" : 5 },
  { "c_name" : "Tracy", "description": "cereal", "amount" : 2 },
  { "c_name" : "Amazon", "description": "servers", "amount" : 200 }
])

lookup = database.customers2.aggregate([
   {
      "$lookup": {
         "from": "orders2",
         "localField": "name",
         "foreignField": "c_name",
         "as": "transaction"
      }
   }])
print("Part E:")
pprint.pprint(list(lookup))