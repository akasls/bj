# -*- coding: utf-8 -*- # <<< 添加此行解决编码错误
import requests
import time
import random
import string # <<< 添加此行，因为 ranEmail 函数中使用了 string 模块

def ranEmail(): # <<< 建议使用这个更通用的邮箱生成函数
    random_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5, 8)))
    email = random_str + "@gmail.com"
    return email

def ranDeviceId(): # <<< 建议使用这个更通用的设备ID生成函数
    device_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(len("rk_dbf7a4a5b8294d988ea07ccd1b06e82b")))
    return device_id

bj = '8V1L2Z'  # <<< 邀请码已更新为 8V1L2Z >>>

# 邀请的人数，每次运行随机邀请1到5个
times = random.randint(1, 5) # <<< 邀请人数已修改为随机1-5个 >>>

def a():
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
    # 保持你原有的邮箱生成方式，但移除了冗余的 email 变量初始化
    # 如果你喜欢，可以使用 `email = ranEmail()` 来生成更标准的邮箱
    email_user = "".join(random.choice("1234567890") for i in range(10))
    email_domain_suffix = "".join(random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(4))
    email_address = email_user + '%40' + email_domain_suffix + '.com'  # 随机挑选十个数字和四个字母组成邮箱

    data = 'passwd=e10adc3949ba59abbe56e057f20f883e&email='+email_address+'&invite_code='+bj  # 发送的内容，密码我就写的123456，想改自己MD5加密一下

    #  获取时间戳
    t = str(int(round(time.time() * 1000)))
    # 随机获取id
    # 保持你原有的id生成方式
    device_id_suffix = "".join(random.choice("123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") for i in range(32))

    # 拼接网页
    # WARNING: 这个URL (https://sm01.googls.net/account/register) 很可能已失效！
    # 你会遇到 504 Gateway Time-out 错误。强烈建议你用 F12 找到有效 URL。
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
        'Content-Length': str(len(data)), # <<< 修正 Content-Length，非常重要！>>>
        'Host': 'sm01.googls.net', # 与URL主机保持一致
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.5.0'
    }
    
    # <<< 添加请求发送和日志打印，这对于调试至关重要 >>>
    try:
        response = requests.post(url=url, data=data, headers=header, timeout=10)
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during request: {e}")


if __name__ == '__main__':
    # print("\n\tThis script will only invite users. It does NOT implement daily limits or state management.")
    print(f"Script will attempt to invite {times} users.")
    for i in range(1, times+1):
        print(f"\nAttempting invitation {i} of {times}...")
        a()
        # <<< 添加随机延迟，模拟人类行为，降低被检测风险 >>>
        sleep_time = random.uniform(2, 5) # 随机等待2-5秒
        print(f"Waiting for {sleep_time:.2f} seconds before next invitation...")
        time.sleep(sleep_time)

    print(f"\nFinished trying to invite {times} users.")
