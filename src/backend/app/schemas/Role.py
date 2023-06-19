#!/usr/bin/python
#-*- coding: utf-8 -*-
from typing import List
from schemas.Persistent import Persistent
from pydantic import Field


class Role(Persistent):
    """Is an organized set of permissions intended to reflect an organization function."""
    name: str = "" #Name of the Role
    #permissions: List[int] = [] #List of all unique Int ID's of permissions the role contains
    tags: List[str] = [] #List of strings indicating all associated tags with role
    description: str = "" #Description of the role

    class Config:
        orm_mode = True

    def addPermission(self, permission):
        """Adds a permission to the set"""
        if permission not in self.permissions:
            self.permissions.append(permission)

    def remPermission(self, permission):
        """Removes a permission from a the set"""
        if permission in self.permissions:
            self.permissions.remove(permission)
            return permission
        return None

    def addTag(self, tag):
        """Adds a tag to the tag set"""
        if tag not in self.tags:
            self.tags.append(tag)

    def remTag(self, tag):
        """Removes a tag from the tag set if that tag is present"""
        if tag in self.tags:
            self.tags.remove(tag)
            return tag
        return None

    def create(self):
        """get a database connection and create role"""
        pass

    def update(self):
        """get a database connection and update role"""
        pass