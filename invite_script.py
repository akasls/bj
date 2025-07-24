# -*- coding: utf-8 -*-
import requests
import time
import random
import string
import datetime
import os
import sys

# --- 配置 ---
bj = '8V1L2Z'  # <<< 你的邀请码已更新为 8V1L2Z >>>
MIN_INVITES = 1
MAX_INVITES = 5 # <<< 每次运行随机邀请1到5人 >>>

# 用于记录上次运行日期的文件路径
LAST_RUN_FILE = "last_run_date.txt"

# --- 辅助函数 ---
def ranEmail():
    random_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5, 8)))
    email = random_str + "@gmail.com"
    return email

def ranDeviceId():
    # 生成随机设备ID，长度与示例device_id一致
    device_id = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(len("rk_dbf7a4a5b8294d988ea07ccd1b06e82b")))
    return device_id

def perform_invitation():
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

    email_address = ranEmail() # 使用 ranEmail 函数生成更标准的邮箱

    data = 'passwd=e10adc3949ba59abbe56e057f20f883e&email=' + email_address + '&invite_code=' + bj # 注意这里的 email 变量

    # 获取时间戳
    t = str(int(time.time() * 1000))
    # 随机获取id
    device_id_val = ranDeviceId() # 使用 ranDeviceId 函数生成

    # !!! 重要：请务必核对正确的注册接口URL！
    # 你上次的错误信息显示 https://co01.jurasic.net 504 Gateway Time-out
    # 这意味着这个URL可能也失效了。
    # 你需要通过F12抓包找到当前最新的、有效的注册API接口URL。
    url = 'https://co01.jurasic.net/account/register?' \
               'platform=2&api_version=14&' \
               'app_version=1.45&lang=zh&_key=&' \
               'market_id=1000&' \
               'pkg=com.bjchuhai&' \
               'device_id=' + device_id_val + '&' \
               'model=' + Phone + '&' \
               'sys_version=9&' \
               'ts=' + t + '&' \
               'sub_pkg=com.bjchuhai&' \
               'version_code=45'

    header = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': str(len(data)), # <<< 动态计算 Content-Length >>>
        'Host': 'co01.jurasic.net', # <<< 与URL主机保持一致 >>>
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.5.0'
    }
    
    try:
        response = requests.post(url=url, data=data, headers=header, timeout=10)
        print(f"Request to {url}")
        # print(f"Data: {data}") # 为避免日志过长，可以注释掉敏感数据
        print(f"Headers: {header}")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        return True # 返回成功状态
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during invitation: {e}")
        return False # 返回失败状态

# --- 主逻辑 ---
if __name__ == '__main__':
    today = datetime.date.today()
    last_run_date = None

    # 从 LAST_RUN_FILE 读取上次运行日期
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, 'r') as f:
            try:
                last_run_date_str = f.read().strip()
                last_run_date = datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Could not parse last run date from file. Will proceed with script.")
    
    # 检查今天是否已运行
    if last_run_date == today:
        print(f"Script already successfully ran today ({today}). Exiting.")
        sys.exit(0) # 成功退出，不触发后续提交
    else:
        # 如果未运行过或日期不匹配，则执行核心邀请逻辑
        print(f"Script has not run today or last run date is old. Running for {today}...")
        
        times_to_invite = random.randint(MIN_INVITES, MAX_INVITES)
        print(f"Script will attempt to invite {times_to_invite} users.")
        
        all_successful = True # 标记所有邀请是否都成功
        for i in range(1, times_to_invite + 1):
            print(f"\nAttempting invitation {i} of {times_to_invite}...")
            if not perform_invitation(): # 如果任一邀请失败
                all_successful = False
            
            # 每次邀请之间增加随机延迟
            sleep_time = random.uniform(2, 5)
            print(f"Waiting for {sleep_time:.2f} seconds before next invitation...")
            time.sleep(sleep_time)

        print(f"\nFinished trying to invite {times_to_invite} users.")
        
        # 只有当所有邀请尝试都完成，才更新日期文件
        # 这确保了如果脚本提前崩溃，不会错误地标记为已运行。
        with open(LAST_RUN_FILE, 'w') as f:
            f.write(str(today))
        print(f"Recorded last run date as {today}.")
        
        # 如果有任何邀请失败，可以考虑非零退出码，让GitHub Actions标记为失败
        if not all_successful:
            sys.exit(1) # 表示脚本执行有部分失败
