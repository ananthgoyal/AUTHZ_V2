from datetime import datetime
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


def test_create_empty_role():
    response = client.post("/roles/", json={})

    assert response.status_code == 201
    resp = response.json()
    assert is_valid_date_format(resp["createdOn"])
    assert resp["lastModifiedBy"] == None
    assert resp["version"] == 1
    assert resp["isEnabled"] == True
    assert is_valid_uuid(resp["id"]) 
    assert resp["tags"] == []
    assert resp["name"] == ""
    assert resp["description"] == ""
    assert resp["createdBy"] == None
    assert resp["lastModifiedOn"] == None
    assert resp["effectiveFrom"] == None

    
