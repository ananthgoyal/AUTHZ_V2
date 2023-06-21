# Roles

See [here](https://github.com/ananthgoyal/AUTHZ_4_PYTHON/blob/main/doc/objects.md) for class attributes and methods

## Create a Role
**POST /roles**:
Inserts a Role object in DB. 

JSON format:
```
{
"name" : str
"permissions": List[int]
"tags": List[str],
"createdBy": int, 
"lastModifiedBy": int,
"isEnabled": bool,
"effectiveFrom": "YYYY-MM-DD",
"id": int
}
```
## Read All Roles

**GET /roles**:Returns all Role objects in DB (currently not paginated)

## Read a Role

**GET /roles/user_id**: Returns the associated Role object in DB with "user_id"

## Update a Role

**PUT /roles/user_id**: Updates the Role object associated with "user_id" in DB
JSON format:
```
{
"name" : str
"permissions": List[int]
"tags": List[str],
"isEnabled": bool,
"effectiveFrom": "YYYY-MM-DD",
"id": int
}
```

## Delete a Role 
**DELETE /roles/user_id**: Delete the Role object associated with "user_id" from DB

# User

# Permission


