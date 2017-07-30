import os

with open('state') as fi:
    state = fi.readline()

if state == 'open':
    os.system("youtube-dl -o - https://youtu.be/oTRZOYTev4g | castnow --quiet -")
elif state == 'closed':
    os.system("youtube-dl -o - https://youtu.be/3znZk8BXN9Q | castnow --quiet -")
