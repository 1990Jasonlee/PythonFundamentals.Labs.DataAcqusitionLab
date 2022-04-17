import urllib.request
import os
file = 0

while file < 39:
    url = 'https://www.ncdc.noaa.gov/cdo-web/api/v2/locations/'
    header = {'token': 'hPxdeiarThkOjtyXSiykGemaretddPq'}
    req = urllib.request.Request(url, headers=header)
    file_name = '.locations'+str(file)+'.json'