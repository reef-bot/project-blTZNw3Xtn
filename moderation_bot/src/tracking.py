# tracking.py

# Importing necessary libraries
import json

# Function to load tracking data from the JSON file
def load_tracking_data():
    try:
        with open('../data/tracking_data.json', 'r') as file:
            tracking_data = json.load(file)
        return tracking_data
    except FileNotFoundError:
        print("Tracking data file not found.")
        return {}

# Function to save tracking data to the JSON file
def save_tracking_data(tracking_data):
    with open('../data/tracking_data.json', 'w') as file:
        json.dump(tracking_data, file, indent=4)

# Function to track user behavior and issue warnings
def track_user_behavior(user_id, behavior):
    tracking_data = load_tracking_data()
    
    if user_id not in tracking_data:
        tracking_data[user_id] = {'warnings': 0, 'behavior_history': []}
    
    tracking_data[user_id]['behavior_history'].append(behavior)
    
    if behavior == 'inappropriate':
        tracking_data[user_id]['warnings'] += 1
    
    save_tracking_data(tracking_data)

# Function to get user's warning count
def get_user_warnings(user_id):
    tracking_data = load_tracking_data()
    
    if user_id in tracking_data:
        return tracking_data[user_id]['warnings']
    else:
        return 0

# Function to get user's behavior history
def get_user_behavior_history(user_id):
    tracking_data = load_tracking_data()
    
    if user_id in tracking_data:
        return tracking_data[user_id]['behavior_history']
    else:
        return []

# Function to reset user's tracking data
def reset_user_tracking(user_id):
    tracking_data = load_tracking_data()
    
    if user_id in tracking_data:
        del tracking_data[user_id]
        save_tracking_data(tracking_data)