import requests
import os

# Replace with your actual API key and external user ID
api_key = 'Dc7JAnS74SyVKe7EzHKnMIKuqF2qYtkg'
external_user_id = '06931013-9ae4-449d-87e8-4224508ba0d0'
session_id = None  # Will store session ID for reuse

# Initializes the session if not already set
def initialize_session():
    global session_id
    if session_id is None:
        create_session_url = 'https://api.on-demand.io/chat/v1/sessions'
        headers = {'apikey': api_key}
        session_data = {
            "pluginIds": ['plugin-1729925443'],
            "externalUserId": external_user_id
        }
        response = requests.post(create_session_url, headers=headers, json=session_data)
        session_id = response.json()['data']['id']
    return session_id

# Processes a query based on user input
def get_response(user_query):
    # Step 1: Initialize session
    session_id = initialize_session()
    
    # Step 6: Submit Query
    submit_query_url = f'https://api.on-demand.io/chat/v1/sessions/{session_id}/query'
    headers = {'apikey': api_key}
    query_body = {
        "endpointId": "predefined-openai-gpt4o",
        "query": user_query,
        "pluginIds": ["plugin-1729925443"],
        "responseMode": "sync"
    }
    response = requests.post(submit_query_url, headers=headers, json=query_body)
    response_data = response.json()

    # Extract and return the answer
    return response_data.get('data', {}).get('answer', "No response available.")