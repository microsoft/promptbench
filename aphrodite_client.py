import os
import requests
import json

ALEXIARES_URL = os.getenv("ALEXIARES_HOST") 
APHRODITE_URL = os.getenv("APHRODITE_HOST") 

class AphroditeClient:
    username = ""
    password = ""
    token = ""

    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.login()

    def print_request(self, req):
        print('{}\n{}\r\n{}\r\n\r\n{}'.format(
            '-----------START-----------',
            req.method + ' ' + req.url,
            '\r\n'.join('{}: {}'.format(k, v) for k, v in req.headers.items()),
            req.body,
        ))

    def login(self):
        """
        performs a login to Alexiares via the credentials
        """

        data = {
            'username': self.username,
            'password': self.password,
            'grant_type': 'password'
        }

        response = requests.post(
            ALEXIARES_URL + "/auth/users/login",
            headers = {
                'Content-Type': 'application/json'
            },
            data = json.dumps(data)
        )

        if response.status_code != 200:
            raise Exception("Login failed")

        payload = response.json()
        self.token = payload["access_token"]


    def do_aphrodite_query(self, company_id, question, start_date, end_date, report_type):
        """
        Send an inference request to Aphrodite
         company_id: the ID of the company, for example f7197f6c-e765-4b3d-abba-820725344726
         question: question for Aphrodite to make an inference
         start_date: statement info start date, in format YYYY-MM-DD
         end_date: statement info end date, in format YYYY-MM-DD
         report_type: must be one of: income_statement, balance_sheet, cashflow_statement
        """

        endpoint = APHRODITE_URL + f"/graph-inference/api/v1/companies/{company_id}/inference/financials"

        headers = {
            'accept': 'application/json',
            'Authorization': f'Bearer {self.token}',
            'Content-Type': 'application/json'
        }

        data = {
            'question': question,
            'start_date': start_date,
            'end_date': end_date,
            'report_type': report_type
        }

        response = requests.post(endpoint, headers=headers, data=json.dumps(data))

        if response.status_code == 401:
            self.login()
            headers["Authorization"] = f'Bearer {self.token}'
            response = requests.post(endpoint, headers=headers, data=json.dumps(data))

        if response.status_code != 200:
            raise Exception("Request to Aphrodite failed")

        payload = response.json()
        aphrodite_response = payload["text"]

        return aphrodite_response

