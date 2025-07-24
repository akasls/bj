import requests
import time
import random
import string
import datetime
import os
import sys

# --- ���� ---
bj = '8V1L2Z'  # ���������
MIN_INVITES = 1
MAX_INVITES = 5

# ���ڼ�¼�ϴ��������ڵ��ļ�·��������GitHub Actions�������д���
# ע�⣺����ļ���Ҫ���ύ�زֿ⣬ÿ�����ж������µ��ύ��
# ���ߣ����Կ���ʹ��GitHub Gist��Actions��artifact������״̬�����ǻ�����ӡ�
# �������һ���򵥵ķ��������ᵼ���ύ��ʷ����һЩ�Զ��ύ��
LAST_RUN_FILE = "last_run_date.txt"

# --- �������� ---
def ranEmail():
    random_str = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(random.randint(5, 8)))
    email = random_str + "@gmail.com"
    return email

def ranDeviceId():
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

    email_address = ranEmail()

    data = 'passwd=e10adc3949ba59abbe56e057f20f883e&email=' + email_address + '&invite_code=' + bj

    t = str(int(time.time() * 1000))
    device_id_val = ranDeviceId()

    # �ٴ�ǿ��������غ˶���ȷ��ע��ӿ�URL��
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
        'Content-Length': str(len(data)),
        'Host': 'co01.jurasic.net', # ��URL��������һ��
        'Connection': 'Keep-Alive',
        'Accept-Encoding': 'gzip',
        'User-Agent': 'okhttp/3.5.0'
    }
    
    try:
        response = requests.post(url=url, data=data, headers=header, timeout=10)
        print(f"Request to {url}")
        # print(f"Data: {data}") # Ϊ������־����������ע�͵���������
        print(f"Headers: {header}")
        print("Status Code:", response.status_code)
        print("Response Text:", response.text)
        return True
    except requests.exceptions.RequestException as e:
        print(f"An error occurred during invitation: {e}")
        return False

# --- ���߼� ---
if __name__ == '__main__':
    today = datetime.date.today()
    last_run_date = None

    # �� LAST_RUN_FILE ��ȡ�ϴ���������
    if os.path.exists(LAST_RUN_FILE):
        with open(LAST_RUN_FILE, 'r') as f:
            try:
                last_run_date_str = f.read().strip()
                last_run_date = datetime.datetime.strptime(last_run_date_str, "%Y-%m-%d").date()
            except ValueError:
                print("Could not parse last run date from file. Will proceed with script.")
    
    if last_run_date == today:
        print(f"Script already successfully ran today ({today}). Exiting.")
        sys.exit(0) # �ɹ��˳��������������ύ
    else:
        # ���δ���й������ڲ�ƥ�䣬��ִ�к��������߼�
        print(f"Script has not run today or last run date is old. Running for {today}...")
        
        # ����ӳ٣�ģ����11�㵽14����������ڵ����ʱ������
        # ����ӳ�����GitHub Actions���������������ģ�
        # ���Լ�ʹ��������11�㴥�����ű�Ҳ������11��X��ִ�С�
        # �����ǻ���Ҫȷ������14��֮ǰ��ɡ�
        # ʵ�ʵ����ʱ�������Ҫ���� cron ���ʽ��Ƶ�ʺͽű��Ķ�ʱ�ӳ١�
        
        times_to_invite = random.randint(MIN_INVITES, MAX_INVITES)
        print(f"Script will attempt to invite {times_to_invite} users.")
        
        all_successful = True
        for i in range(1, times_to_invite + 1):
            print(f"\nAttempting invitation {i} of {times_to_invite}...")
            if not perform_invitation():
                all_successful = False
            
            # ÿ������֮����������ӳ�
            sleep_time = random.uniform(2, 5)
            print(f"Waiting for {sleep_time:.2f} seconds before next invitation...")
            time.sleep(sleep_time)

        print(f"\nFinished trying to invite {times_to_invite} users.")
        
        # ֻ�е��������볢�Զ���ɣ����۳ɹ���񣩣��Ÿ��������ļ�
        # ��ȷ��������ű���ǰ�������������ر��Ϊ�����С�
        with open(LAST_RUN_FILE, 'w') as f:
            f.write(str(today))
        print(f"Recorded last run date as {today}.")
        
        # ������κ�����ʧ�ܣ����Կ��Ƿ����˳��룬��GitHub Actions���Ϊʧ��
        if not all_successful:
            sys.exit(1)
