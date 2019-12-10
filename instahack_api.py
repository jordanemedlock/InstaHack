import instagram_web_api 
import instagram_private_api 
import hashlib
import string
import random
import json


class MyClient(instagram_web_api.Client):
    @staticmethod
    def _extract_rhx_gis(html):
        options = string.ascii_lowercase + string.digits
        text = ''.join([random.choice(options) for _ in range(8)])
        return hashlib.md5(text.encode()).hexdigest()
    
# Without any authentication
web_api = MyClient(auto_patch=True, drop_incompat_keys=False)
private_api = instagram_private_api.Client('jordanemedlock', 'kGcBKXFbAnjdcp79gq!V')
jem_id = '5564617835'

def get_user_followings(user_id):
    uuid = private_api.generate_uuid()
    following_users = private_api.user_following(user_id, uuid)
    return following_users['users']

def get_username_info(username):
    print('getting username info: {}'.format(username))
    info = private_api.username_info(username)
    return info['user']