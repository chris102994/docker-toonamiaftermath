
'''
Tools (Helper) Class
'''
import json
import os
from os import path
import requests

class Tools:
    def __init__(self):
        pass

    def wrapper(self, file_name, channel_list, episode_list):
        self.check_file_existance(file_name)
        f = self.open_file(file_name)
        self.write_header_to_file(f)
        self.write_list_to_file(f, channel_list)
        self.write_list_to_file(f, episode_list)
        self.write_footer_to_file(f)
        self.close_file(f)

    def check_file_existance(self, file_name):
        if path.exists(file_name):
            os.remove(file_name)
            print('Removing Remnant: ' + file_name)

    def open_file(self, file_name):
        f = open(file_name, 'w+')
        return f

    def write_header_to_file(self, f):
        header = '<?xml version="1.0"?>\n' \
                 '<!DOCTYPE tv SYSTEM "xmltv.dtd">\n\n' \
                 '<tv source-info-url="https://api.toonamiaftermath.com" source-info-name="Toonami Aftermath" generator-info-name="Toonami-Grab" generator-info-url="https://api.toonamiaftermath.com">\n'
        f.write(header)

    def write_footer_to_file(self, f):
        footer = '</tv>\n'
        f.write(footer)

    def write_list_to_file(self, f, media_list):
        for obj in media_list:
            f.write(obj.to_string())

    def close_file(self, f):
        f.close()

