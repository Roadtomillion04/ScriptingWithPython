import requests
import hashlib
import sys

'''always use raw string if string has backslash else it can take them as escape sequence'''

def request_api_data(query_char:str):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    response = requests.get(url)

    if response.status_code != 200:
        raise RuntimeError(f'unauthorised response {response.status_code}')

    return response


def read_response(response):
    print(response.text) # Because as it is an api we can read text


def get_password_leaks_count(hashes, tail):
    hashes = (lines.split(':') for lines in hashes.text.splitlines() ) # we get generator object here
    '''Now we gonna unpack the tuple'''

    for h, count in hashes:
#        print(h ,count)
         if h == tail:
            return count
    return 0

'''hash sha1 works same as sha1 generator online'''
def pwned_api_check(password:str):
                    #unicode objects must be encoded before hashing
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper() #hexdigest gives values in hexadecimal digits
    '''we used upper to match with sha1 generator online'''
                    #grabs first 5 char , grabs rest
    first5_char, tail = sha1password[:5], sha1password[5:]
    print(first5_char, tail)

    res = request_api_data(first5_char)
    ''' Because we don't want to give our full hexadecimal values to servers we can't trust'''

    #read_response(res)
    return get_password_leaks_count(res, tail)


def run_program(args:list):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was found {count} times!')
        else:
            print(f'{password} is super strong!')


if __name__ == '__main__':
    run_program(sys.argv[1:])
    sys.exit() # similar to break in while loop
    #print('hi')
