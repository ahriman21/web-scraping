"""
- to act as a true user when we make a request to a website we can use "fake_useragent" package.
this helps us not to be detected as a robot.
"""

from fake_useragent import UserAgent
import requests

u = UserAgent()

header = {'user-agent' : u.chrome}

page = requests.get('url', header=header)
