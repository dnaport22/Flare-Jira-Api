import requests
from requests.auth import HTTPBasicAuth
import datetime
import json

class Service():

  BASE_URL = 'https://maddna.atlassian.net/rest/api/2'

  def log_time(self, data):
    url = Service.BASE_URL + '/issue/' + data['issue'] + '/worklog'
    body = json.dumps({"comment": data['comment'], "started": "2017-05-10T23:43:04.454+0000", "timeSpentSeconds": data['timeSpent']})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == '200':
      return True
    else:
      return False

  def leave_comment(self, data):
    url = Service.BASE_URL + '/issue/' + data['issue'] + '/comment'
    body = json.dumps({"body": data['comment']})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == '200':
      return True
    else:
      return False

  def test(self, data):
    return data

  def get_user_email(self):
    return 'nav8699@gmail.com'

  def get_user_pass(self):
    return 'Nav83573549'