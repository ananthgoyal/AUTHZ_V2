from datetime import datetime, date
import datetime
from utils import is_valid_date_format, is_valid_uuid
from fastapi.testclient import TestClient
import sys
import os
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.join(current_dir, "..")
sys.path.append(parent_dir)
from main import app
import utils

client = TestClient(app)

empty_id = None


def test_create_role():
    """Tests a valid creation of role object"""
    global empty_id
    response = client.post("/roles/", json={})
    assert response.status_code == 201
    resp = response.json()
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 1
    assert resp["isEnabled"] == True
    assert is_valid_uuid(resp["id"])
    empty_id = resp["id"]
    assert resp["tags"] == []
    assert resp["name"] == ""
    assert resp["description"] == ""
    assert resp["createdBy"] == None
    assert resp["lastModifiedOn"] == None
    assert resp["effectiveFrom"] == None

def test_read_role():
    "Tests valid read of role"
    global empty_id
    response = client.get("/roles/" + empty_id)
    assert response.status_code == 200 
    resp = response.json()
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 1
    assert resp["isEnabled"] == True
    assert is_valid_uuid(resp["id"])
    empty_id = resp["id"]
    assert resp["tags"] == []
    assert resp["name"] == ""
    assert resp["description"] == ""
    assert resp["createdBy"] == None
    assert resp["lastModifiedOn"] == None
    assert resp["effectiveFrom"] == None


def test_update_role():
    "Tests valid update of role"
    global empty_id
    response = client.put("/roles/" + empty_id, json={"name": "Ananth Goyal", "isEnabled": False, 
    "tags":["tag1, tag2"], "description": "Test Description", "effectiveFrom": str(date.today())})
    response.status_code = 200
    resp = response.json()
   
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 2
    assert resp["isEnabled"] == False
    assert is_valid_uuid(resp["id"])
    empty_id = resp["id"]
    assert resp["tags"] == ["tag1, tag2"]
    assert resp["name"] == "Ananth Goyal"
    assert resp["description"] == "Test Description"
    assert resp["createdBy"] == None
    assert is_valid_date_format(resp["lastModifiedOn"])
    assert is_valid_date_format(resp["effectiveFrom"])

def test_delete_role():
    "Tests valid delete of role"
    global empty_id
    response = client.delete("/roles/" + empty_id)
    response.status_code = 200

    resp = response.json()
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 2
    assert resp["isEnabled"] == False
    assert is_valid_uuid(resp["id"])
    empty_id = resp["id"]
    assert resp["tags"] == ["tag1, tag2"]
    assert resp["name"] == "Ananth Goyal"
    assert resp["description"] == "Test Description"
    assert resp["createdBy"] == None
    assert is_valid_date_format(resp["lastModifiedOn"])
    assert is_valid_date_format(resp["effectiveFrom"])
    response = client.get("/roles/" + empty_id)
    assert response.status_code == 404
    


def test_error_read_404():
    """Tests an invalid get request because ID doesn't exist"""
    response = client.get("/roles/11111111-1111-1111-1111-111111111111")
    assert response.status_code == 404

def test_error_delete_404():
    """Tests an invalid delete request because ID doesn't exist"""
    response = client.put("/roles/" + empty_id, json={})
    assert response.status_code == 404

def test_error_delete_404():
    """Tests an invalid delete request because ID doesn't exist"""
    response = client.delete("/roles/" + empty_id)
    assert response.status_code == 404


