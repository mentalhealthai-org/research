from datetime import datetime, timedelta
import requests


# declaring some api queries/endpoints as constants in a dictionary
# and other utilities/helper functions

# api endpoints
SANDBOX_API_ENDPOINTS = {
    "demographic": "https://sandbox-api.sahha.ai/api/v1/profile/demographic/{user_id}",
    "device_information": "https://sandbox-api.sahha.ai/api/v1/profile/deviceInformation/{user_id}",
    "sleep": ("https://sandbox-api.sahha.ai/api/v1/profile/biomarker/{user_id}?categories=sleep" 
             "&endDateTime={end_datetime}&startDateTime={start_datetime}&types=sleep_start_time&types=sleep_end_time&types=sleep_duration" 
             "&types=sleep_debt&types=sleep_interruptions&types=sleep_light_duration&types=sleep_rem_duration&types=sleep_deep_duration"
             "&types=sleep_regularity&types=sleep_latency&types=sleep_efficiency"),
    "steps": "https://sandbox-api.sahha.ai/api/v1/profile/biomarker/{user_id}?categories=activity&startDateTime={start_datetime}&endDateTime={end_datetime}&types=steps",
    "token" : "https://sandbox-api.sahha.ai/api/v1/oauth/account/token",
    "health": "https://sandbox-api.sahha.ai/api/v1/profile/biomarker/{user_id}?categories=activity&categories=sleep&endDateTime={end_datetime}&startDateTime={start_datetime}&types=steps&types=active_duration&types=sleep_start_time&types=sleep_end_time&types=sleep_duration&types=sleep_light_duration&types=sleep_rem_duration&types=sleep_deep_duration", # fetch activity and sleep data
    # TODO: check why vitals isn't working "vitals": "",
}

# helper functions

def get_headers(token=None):
    """Helper function to build a basic header for a request."""
    headers = {
        "Content-Type": "application/json",
    }
    if token is not None:
        headers["Authorization"] = f"account {token}"
    return headers

def get_dates(end_datetime=None, days_back=5):
    """Helper function to get start and end dates from last 5 days."""
    if end_datetime is None:
        end_datetime = datetime.now() - timedelta(days=1)
    
    start_datetime = end_datetime - timedelta(days=days_back)

    end_datetime = end_datetime.strftime("%Y-%m-%d")
    start_datetime = start_datetime.strftime("%Y-%m-%d")

    return start_datetime, end_datetime


# api requests functions

# Let's declare a helper function `get_auth_token`, which handles authentication with Sahha and returns a token.
# This **token must be included in the header** of every API request as an `Authorization` key, with the value formatted as:

# `account {TOKEN_RECEIVED_FROM_AUTHENTICATION}`

# all api requests must contain the authorization header containing this token

def get_auth_token(client_id, client_secret):
    """Authenticate with sahha to get token"""
    headers = get_headers()
    data = {
        "clientId":client_id,
        "clientSecret": client_secret,
    }
    r = requests.post(url=SANDBOX_API_ENDPOINTS["token"], headers=headers, json=data)
    if r.status_code == 200:
        return r.json()["accountToken"]
    else:
        raise Exception("Failed to get auth token")


def get_steps(token, user_id):
    """Gets steps data from last 3 days"""
    headers = get_headers(token=token)
    start_datetime, end_datetime = get_dates()
    r = requests.get(url=SANDBOX_API_ENDPOINTS["steps"].format(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Failed to get steps")

def get_device_information(token, user_id):
    """Gets patient's device(phone) basic information"""
    headers = get_headers(token=token)
    r = requests.get(url=SANDBOX_API_ENDPOINTS["device_information"].format(user_id=user_id), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Failed to get device information")

def get_demographic(token, user_id):
    """Gets user demographic data"""
    headers = get_headers(token=token)
    r = requests.get(url=SANDBOX_API_ENDPOINTS["demographic"].format(user_id=user_id), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Failed to get demographic data")

def get_sleep(token, user_id):
    """Gets user sleep data"""
    headers = get_headers(token=token)
    start_datetime, end_datetime = get_dates()
    r = requests.get(url=SANDBOX_API_ENDPOINTS["sleep"].format(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Failed to get sleep data")

def get_health(token, user_id, datetime=None):
    """Get users activity and sleep data in one request"""
    headers = get_headers(token=token)
    if datetime is None:
        start_datetime, end_datetime = get_dates()
    else:
        start_datetime = datetime
        end_datetime = datetime
    r = requests.get(url=SANDBOX_API_ENDPOINTS["health"].format(user_id=user_id, start_datetime=start_datetime, end_datetime=end_datetime), headers=headers)
    if r.status_code == 200:
        return r.json()
    else:
        raise Exception("Failed to get health data")
    
    