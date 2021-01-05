import requests
res = requests.get('https://automatetheboringstuff.com/files/rj.txt')
print(type(res))
print( res.status_code == requests.codes.ok) # Instance of 'LookupDict' has no 'ok' member ??
print(res.text[:250])
res = requests.get('https://inventwithpython.com/page_that_does_not_exist')
try: 
    res.raise_for_status()
except Exception as exc:
    print('There was a problem: %s' % (exc))
print("OKAY!")
