import requests, uuid, random
attempts = 0


def dmspam(target):
    Headers = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q=0.9",
    "cache-control": "max-age=0",
    "cookie": "ig_cb=2; ig_did=98A65825-0D8A-47BD-88A1-BEB47ADA2558; mid=YEx5KgALAAEqEYHsJ6VKhzYIMyDf; csrftoken=eQk6HEDyXYgAjiAQVpg1KSCjFuhazzxU; ds_user_id=6963644797; shbid=18338; shbts=1615624514.8718474; rur=FRC",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
    "upgrade-insecure-requests": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    }
    req = requests.get(f"https://www.instagram.com/{target}/?__a=1", headers=Headers)
    response = req.json()
    uid = response['graphql']['user']['id']
    while True:
        msg = f'I am Keng Enistagram-{random.randint(1111, 9999)} '
        sendmsg(uid, msg)

def sendmsg(target,msg):
    global attempts
    api = 'https://i.instagram.com/api/v1/direct_v2/threads/broadcast/text/'

    ctx = uuid.uuid1()

    data = f'recipient_users=[[{target}]]&mentioned_user_ids=[]&action=send_item&client_context={ctx}&_csrftoken=9kugaGIMcKzLGIKK0NyqNc6oyVpb7GPU&text={msg}&device_id=3067fdf6-4d1a-44af-8935-0b5da1f4d1a3&mutation_token=35c762b8-5811-5811-a199-0fa0203d639d&_uuid=3067fdf6-4d1a-44af-8935-0b5da1f4d1a3'

    head = {
        'Cookie': 'is_starred_enabled=yes; sessionid=229000934%3AORSKRXy32EuPyV%3A27; ds_user=; ds_user_id=229000934; csrftoken=9kugaGIMcKzLGIKK0NyqNc6oyVpb7GPU; igfl=; rur=PRN;',
        'User-Agent': 'Instagram 23.0.0.15.68 Android (24/5.0; 515dpi; 1440x2416; huawei/google; Nexus 6P; angler; angler; en_US)',
        'Accept-Language': 'ar;q=1, en;q=0.9',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'host': 'i.instagram.com'
    }

    k = requests.post(api, headers=head, data=data)
    print(k.text)
target = input('target: ')
dmspam(target)
