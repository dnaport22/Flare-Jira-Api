import requests
from requests.auth import HTTPBasicAuth
import datetime
import json

class Service():

  BASE_URL = 'https://maddna.atlassian.net/rest/api/2'
  SUCCESS_CODE = 201
  PROJECT_ALIAS = 'TP'

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
      return self.parse_ticket_number(data['issue'])

    return self.parse_ticket_number(data['issue'])

  def parse_ticket_number(self, issue):
    return issue


  def test(self, data):
    return data

  def get_user_email(self):
    return 'nav8699@gmail.com'

  def get_user_pass(self):
    return 'Nav83573549'