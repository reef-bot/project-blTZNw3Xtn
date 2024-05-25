# filtering.py

import json

class MessageFilter:
    def __init__(self, filter_data_file):
        self.filter_data_file = filter_data_file
        self.load_filter_data()

    def load_filter_data(self):
        with open(self.filter_data_file, 'r') as file:
            self.filter_data = json.load(file)

    def save_filter_data(self):
        with open(self.filter_data_file, 'w') as file:
            json.dump(self.filter_data, file, indent=4)

    def add_word_to_filter(self, word):
        self.filter_data['filtered_words'].append(word)
        self.save_filter_data()

    def remove_word_from_filter(self, word):
        if word in self.filter_data['filtered_words']:
            self.filter_data['filtered_words'].remove(word)
            self.save_filter_data()

    def filter_message(self, message):
        for word in self.filter_data['filtered_words']:
            if word in message:
                return True
        return False

# Initialize the MessageFilter
filter_obj = MessageFilter('../data/filtering_data.json')