import json
import requests

def authorization(query='', var={}):
    """
    This function should NOT be edited ot changed.
    Authentication with our Monday board. 
    """
    api_key = "eyJhbGciOiJIUzI1NiJ9.eyJ0aWQiOjE3NDEyNzUxOCwidWlkIjoyNzgzNjk1NCwiaWFkIjoiMjAyMi0wOC0wNlQwODozNDo0OS42MjdaIiwicGVyIjoibWU6d3JpdGUiLCJhY3RpZCI6MTM5OTE1LCJyZ24iOiJ1c2UxIn0.buBnMyjxxPvPL3Is6OnvifvGqAyYfpxbctrg9Fgjj1c"
    api_url = "https://api.monday.com/v2"
    headers = {"Authorization": api_key}

    data = {'query': query, 'variables': var}
    return execute_request(api_url, data, headers)

def execute_request(url, data, headers):
    """
    This function should NOT be edited ot changed.
    Executing the Post request directly to the Monday board.
    """
    return requests.post(url=url, json=data, headers=headers).json()


def upload_stakes_list_request(stakes_list={}, board="3511354319"):
    """
    You should complete this function. Please use the board variable to access Monday's board.
    Pushing a Dict of stakes to specific board

    :param stakes_list: dict of stakes to push
    :param board: The specific board you would like the fetch data
    """
