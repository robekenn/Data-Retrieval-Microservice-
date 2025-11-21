#By Kaedin Hanohano
def retrieve_user(user_id, data):

    # Search for user with matching ID
    for user in data["users"]:
        if user["id"] == user_id:
            return user

    # User not found
    return {"error": "User not found"}
