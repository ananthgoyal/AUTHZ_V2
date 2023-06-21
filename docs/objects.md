# Objects 

## Persistent
The primary abstract super class that all persistent objects inherit from

### Class Attributes:
**`createdOn`**: [datetime] The datetime stamp object the object was created on; cannot be changed once object is created 

**`createdBy`**: [int] The ID of the User object that created this object

**`lastModifiedOn`**: [datetime] Datetime object indicating the time stamp this object was last modified. Auto-updated in system

**`lastModifiedBy`**: [int] The of ID of the User object that last edited this object

**`version`**: [int] The version number of the object. Auto-incremented in system

**`effectiveFrom`**: [date] Date object indicating the time this object is effective from

**`isEnabled`**: [bool] Whether the object is enabled; default value is True unless changed by User

**`id`**: [int] The unique ID of the object
 
### Class Methods:
**`updateModificationInfo(modifier: int = None)`**: Updates the persistent object timestamp information and version number. If modifier parameter is passed in then the lastModifiedBy attribute gets updated with the ID of the modifier ID. 


## Role

**`name`:** [str] Name of the Role

**`permissions`:** [List[int]] List of all unique Int ID's of permssions the role contains

**`tags`**: [List[str]] List of strings indicating all associated tags with role


## Class Attributes



### Class Methods:

**`addPermission(permission: int)`**: Adds a permission (ID) to the current set of permissions of the role (if permission is not already added)

**`remPermission(permission: int)`**: Removes a permission (ID) from the role's current set of permissions. Once complete returns the permission; returns None if permission was already removed/not present.

**`addTag(tag: str)`**: Adds a tag to the set of associated tags for the role. 

**`remTag(tag: str)`**: Removes the tag from the role's tags. Returns the tag if succesful. Returns None if tag was already removed/not present. 


## Users

## Permissions