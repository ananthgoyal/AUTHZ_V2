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






