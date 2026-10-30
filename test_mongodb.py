from pymongo import MongoClient
uri = "mongodb+srv://hardikkumar98338_db_user:<@password>@cluster0.cmnr5bi.mongodb.net/"
client = MongoClient(uri)
try:
    client.admin.command("ping")
    print("Connected successfully")
    client.close()

except Exception as e:
    raise Exception(
        "The following error occurred: ", e)