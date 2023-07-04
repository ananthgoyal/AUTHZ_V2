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

role_id = None

def test_create_role_with_perm():
    """Tests a valid creation of role object"""
    global role_id
    response = client.post("/roles/", json={})
    assert response.status_code == 201
    resp = response.json()
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 1
    assert resp["isEnabled"] == True
    assert is_valid_uuid(resp["id"])
    role_id = resp["id"]
    assert resp["tags"] == []
    assert resp["name"] == ""
    assert resp["description"] == ""
    assert resp["createdBy"] == None
    assert resp["lastModifiedOn"] == None
    assert resp["effectiveFrom"] == None
    response = client.post("/permissions/", json = {"role": role_id, "can_create": True})
    response.status_code = 201
    resp = response.json()
    assert resp["role"] == role_id
    assert resp["can_create"]
    assert not resp["can_read"]

def test_read_role_with_perm():
    """Tests a valid read of role object"""

    pass

def test_update_role_with_perm():
    """Tests a valid update of the role object"""

    pass

def test_delete_role_with_perm():
    pass

def test_error_read_404():
    pass

def test_error_assign_invalid_role():
    """Test for assigning a permission to a role that DNE"""
    response = client.post("/permissions/", json={"role" : "11111111-1111-1111-1111-111111111111"})
    assert response.status_code == 404

def test_error_assign_invalid_role_update():
    """Test for assigning a permission to a role that DNE"""
    response_role = client.post("/roles/", json={})
    assert response_role.status_code == 201
    resp_role = response_role.json()
    role_id = resp_role["id"]

    response_perm = client.post("/permissions/", json = {"role": role_id})
    assert response_perm.status_code == 201
    resp_perm = response_perm.json()
    perm_id = resp_perm["id"]


    response = client.put("/permissions/" + perm_id, json={"role" : "11111111-1111-1111-1111-111111111111"})
    assert response.status_code == 404
    



