# -*- coding: utf-8 -*-
import requests
import time
import random
import string

def ranEmail():
    random_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5, 8)))
    email = random_str + "@gmail.com"
    return email

def ranDeviceId():
    device_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(len("rk_dbf7a4a5b8294d988ea07ccd1b06e82b")))
    return device_id

# 定义多个邀请码的列表
# 请在这里替换成你自己的邀请码
INVITE_CODES = [
    '8V1L2Z',
    'T9LVRV', # 你的第二个邀请码
    '9ZDH8', 
    'KLHX7', 
    'xw3gs', 
    '8AAR3Q', 
    'MNNL6', 
    '1H2MZ', 
    '5N6A8', 
    'KA4B8', 
    'ADWPS', 
    'AT5EN', 
    # 可以继续添加更多邀请码
]

def a(invite_code): # 函数a现在接收一个邀请码参数
    #  随机手机
    Phone_name = ["oppo-pedm00","oppo-peem00","oppo-peam00","oppo-x907","oppo-x909t",
                      "vivo-v2048a","vivo-v2072a","vivo-v2080a","vivo-v2031ea","vivo-v2055a",
                      "huawei-tet-an00","huawei-ana-al00","huawei-ang-an00","huawei-brq-an00","huawei-jsc-an00",
                      "xiaomi-mi 10s","xiaomi-redmi k40 pro+","xiaomi-mi 11","xiaomi-mi 6","xiaomi-redmi note 7",
                      "meizu-meizu 18","meizu-meizu 18 pro","meizu-mx2","meizu-m355","meizu-16th plus",
                      "samsung-sm-g9910","samsung-sm-g9960","samsung-sm-w2021","samsung-sm-f7070","samsung-sm-c7000",
                      "oneplus-le2120","oneplus-le2110","oneplus-kb2000","oneplus-hd1910","oneplus-oneplus a3010",
                      "sony-xq-as72","sony-f8132","sony-f5321","sony-i4293","sony-g8231",
                      "google-pixel","google-pixel xl","google-pixel 2","google-pixel 2 xl","google-pixel 3"]
    Phone = random.choice(Phone_name)

    #  邮箱的实现
    email_user = "".join(random.choice("1234567890") for i in range(10))
    email_domain_suffix = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(4))
    email_address = email_user + '%40' + email_domain_suffix + '.com'

    # 使用传入的 invite_code
    data = 'passwd=e10adc3949ba59abbe56e057f20f883e&email='+email_address+'&invite_code='+invite_code

    #  获取时间戳
    t = str(int(round(time.time() * 1000)))
    device_id_suffix = "".join(random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(32))

    url = 'https://sm01.googls.net/account/register?' \
               'platform=2&api_version=14&' \
               'app_version=1.44&lang=zh&_key=&' \
               'market_id=1000&' \
               'pkg=com.bjchuhai&' \
               'device_id=rk_'+device_id_suffix+'&' \
               'model= '+Phone+'&' \
               'sys_version=7.1.2&' \
               'ts='+t+'&' \
               'sub_pkg=com.bjchuhai&' \
               'version_code=44'

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(data)),
        'Host': 'sm01.googls.net',
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.5.0'
    }
    
    try:
        response = requests.post(url=url, data=data, headers=header, timeout=10)
        print(f"Invite Code: {invite_code}, Status Code: {response.status_code}")
        print(f"Invite Code: {invite_code}, Response Text: {response.text}")
    except requests.exceptions.RequestException as e:
        print(f"Invite Code: {invite_code}, An error occurred during request: {e}")


if __name__ == '__main__':
    total_invitations = 0
    # 遍历邀请码列表
    for current_invite_code in INVITE_CODES:
        # 每个邀请码随机邀请1到3个用户
        times = random.randint(1, 3)
        total_invitations += times
        print(f"\n--- Using Invite Code: {current_invite_code} ---")
        print(f"Attempting to invite {times} users for this code.")
        
        for i in range(1, times + 1):
            print(f"\nAttempting invitation {i} of {times} for code {current_invite_code}...")
            a(current_invite_code) # 将当前邀请码传递给函数a
            
            sleep_time = random.uniform(2, 8) # 随机等待2-5秒
            print(f"Waiting for {sleep_time:.2f} seconds before next invitation...")
            time.sleep(sleep_time)
            
    print(f"\nFinished processing all invite codes. Total invitations attempted: {total_invitations}")
