
import json

def get_timeplan_credentials(platform):
    x={}
    with open("login.json") as f:
        data = json.load(f)
    x[0] = data[0]["Timeplan_User"]
    x[1] = data[0]["Timeplan_Pass"]

    if platform == "Windows":
        x[2] = data[0]["win"]
    elif platform == "Darwin":
        x[2] =  data[0]["mac"]
    return x


def get_google_credentials():
    x={}
    with open("login.json") as f:
        data = json.load(f)
    x[0] = data[0]["Google_User"]
    x[1] = data[0]["Google_Pass"]
    x[2] = data[0]["path"]
    return x