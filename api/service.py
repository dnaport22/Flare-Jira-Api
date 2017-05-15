import requests
from requests.auth import HTTPBasicAuth
import datetime
import json

class Service():

  BASE_URL = #BASE_URL
  SUCCESS_CODE = 201

  def log_time(self, data):
    url = Service.BASE_URL + '/issue/' + data['issue'] + '/worklog'
    body = json.dumps({"comment": data['comment'], "started": data['date'], "timeSpentSeconds": data['timeSpent']})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == Service.SUCCESS_CODE:
      return True

    return False

  def leave_comment(self, data):
    url = Service.BASE_URL + '/issue/' + data['issue'] + '/comment'
    body = json.dumps({"body": data['comment']})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == Service.SUCCESS_CODE:
      return True

    return False

  def test(self, data):
    return data

  def get_user_email(self):
    return #GET USER NAME | Hardcode it or get it from db

  def get_user_pass(self):
    return #GET PASSWORD | Hardcode it or get it from db