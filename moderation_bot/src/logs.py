# logs.py

import json

class Logs:
    def __init__(self, log_file):
        self.log_file = log_file
        
    def log_message(self, message):
        try:
            with open(self.log_file, 'a') as file:
                file.write(message + '\n')
        except Exception as e:
            print(f"Error logging message: {e}")
            
    def get_logs(self):
        try:
            with open(self.log_file, 'r') as file:
                logs = file.readlines()
                return logs
        except Exception as e:
            print(f"Error reading logs: {e}")
            return []