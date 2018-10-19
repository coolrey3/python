import urllib3
site = input('What site do you want to grab?')
grab = urllib3.request.urlopen(site)
print(grab.read())


