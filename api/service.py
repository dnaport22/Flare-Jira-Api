import requests
from requests.auth import HTTPBasicAuth
import datetime
import json
import re

class Service():

  BASE_URL = 'https://maddna.atlassian.net/rest/api/2'
  SUCCESS_CODE = 201
  PROJECT_ALIAS = 'TP'

  def log_time(self, data):
    ticket_number = self.parse_ticket_number(data['issue'])
    time_worked = self.parse_time(int(data['timeSpent']))
    url = Service.BASE_URL + '/issue/' + ticket_number + '/worklog'
    body = json.dumps({"comment": data['comment'], "started": data['date'], "timeSpentSeconds": time_worked})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == Service.SUCCESS_CODE:
      print True
      return True

    print True
    return False

  def leave_comment(self, data):
    url = Service.BASE_URL + '/issue/' + self.parse_ticket_number(data['issue']) + '/comment'
    body = json.dumps({"body": data['comment']})
    header = {"Content-Type": "application/json"}
    re = requests.post(url, data=body, headers=header, auth=HTTPBasicAuth(self.get_user_email(), self.get_user_pass()))

    if re.status_code == Service.SUCCESS_CODE:
      return True

    return False

  def parse_ticket_number(self, issue):
    number = re.search(r'\d+', issue).group()
    return Service.PROJECT_ALIAS + '-' + number

  def parse_time(self, time):
    if time < 8:
      return time * 3600
    else:
      return time * 60


  def test(self, data):
    return data

  def get_user_email(self):
    return 'nav8699@gmail.com'

  def get_user_pass(self):
    return 'navdeep.dhuti@atlassianservice'