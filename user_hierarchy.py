"""
Assignment title: User Hierarchy
Author: Shubham Mukund Bhosale

"""

# input for roles
roles = [
            {
                "Id": 1,
                "Name": "System Administrator",
                "Parent": 0
            },
            {
                "Id": 2,
                "Name": "Location Manager",
                "Parent": 1
            },
            {
                "Id": 3,
                "Name": "Supervisor",
                "Parent": 2
            },
            {
                "Id": 4,
                "Name": "Employee",
                "Parent": 3
            },
            {
                "Id": 5,
                "Name": "Trainer",
                "Parent": 3
            }
        ];

# input for users
users = [
            {
                "Id": 1,
                "Name": "Adam Admin",
                "Role": 1
            },
            {
                "Id": 2,
                "Name": "Emily Employee",
                "Role": 4
            },
            {
                "Id": 3,
                "Name": "Sam Supervisor",
                "Role": 3
            },
            {
                "Id": 4,
                "Name": "Mary Manager",
                "Role": 2
            },
            {
                "Id": 5,
                "Name": "Steve Trainer",
                "Role": 5
            }
        ]

# list to store role objects
roles_obj = []

# list to store user objects
users_obj = []

# list to store subordinate objects
subordinate_list = []

# function to create objects of roles
def setRoles(roles):

    # empty dictionary to store each role object
    role_obj = {}
    
    # loop through role data and create each role object
    for role in roles:
        role_obj["Id"] = role["Id"]
        role_obj["Name"] = role["Name"]
        role_obj["Parent"] = role["Parent"]

        # append role oject to global list of roles
        roles_obj.append(role_obj.copy())

# function to create objects of users
def setUsers(users):

    # empty dictionary to store each user object
    user_obj = {}

    # loop through user data and create each user object
    for user in users:
        user_obj["Id"] = user["Id"]
        user_obj["Name"] = user["Name"]
        user_obj["Role"] = user["Role"]

        # append user object to global list of users
        users_obj.append(user_obj.copy())

# function to retrieve subordinates
def getSubOrdinates(user_id):
 
    subordinate_list = []

    # match the given user with user_id
    for user in users_obj:
        if user_id == user["Id"]:

            # check for subordinates using role_id
            for subordinate in users_obj:
                if user["Role"] < subordinate["Role"]:

                    # append subordinate to list of subordinates
                    subordinate_list.append(subordinate.copy())
            break
    
    # print list of subordinates
    if subordinate_list:
        print(subordinate_list)
    else:
        print("This user has no subordinates.")

# function call to set roles           
setRoles(roles)

# function call to set users           
setUsers(users)

# retrieve subordinates associated with user_id
getSubOrdinates(3)
getSubOrdinates(1)
getSubOrdinates(5)