import pytest
import yaml
import requests

with open("config.yaml") as f:
    data = yaml.safe_load(f)

@pytest.fixture()
def login():
    res1 = requests.post(data["address"] + "gateway/login", data={"username": data["username"], "password": data["password"]})
    print(res1.content)
    return res1.json()["token"]

@pytest.fixture()
def testtext1():
    return "test"

@pytest.fixture()
def create_post(login):
    header = {"X-Auth-Token": login}
    post_data = {"title": "New Post Title", "description": "test", "content": "This is a new post."}
    res = requests.post(data["address"]+"api/posts", json=post_data, headers=header)
    assert res.status_code == 201
    return res.json()["id"]