import requests
import hashlib

def requests_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError (f'Error Fetching: {res.status_code}, check the API and try again')
    return res

def get_pass_leaks_count(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h==hash_to_check:
            return print(f'The password has been hacked {count} times, You should probably change that...')
    return 0


def pwned_api_check():
    password = input('Enter The Password to check: ')
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5, tails = sha1password[:5],sha1password[5:]
    response = requests_api_data(first5)
    return get_pass_leaks_count(response,tails)

def run_pass_check():
    count = pwned_api_check()
    if count == 0:
        print('You are good to go')

run_pass_check()