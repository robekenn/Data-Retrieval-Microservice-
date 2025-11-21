
#By Kaedin Hanohano
def push_user(user_id, user_data, data):

    # Check if user_id already exists
    user_exists = False
    for i, user in enumerate(data["users"]):
        if user["id"] == user_id:
            # Update existing user
            data["users"][i] = {"id": user_id, **user_data}
            user_exists = True
            return "OK - User updated"

    # If user doesn't exist, add new user
    if not user_exists:
        new_user = {"id": user_id, **user_data}
        data["users"].append(new_user)
        return "OK - User added"
