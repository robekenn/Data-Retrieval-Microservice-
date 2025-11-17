#By Kenneth Robertson
def delete_user(UserID, data):

    #count the beginning length of the array for checking later
    dataLength = len(data["users"])

    #delete the users with the given ID
    data["users"] = [user for user in data["users"] if user["id"] != UserID]

    #check the length to see if anything has been deleted
    if dataLength == len(data["users"]):
        return "ERROR NO USERS DELETED"
    else:
        return "OK"

