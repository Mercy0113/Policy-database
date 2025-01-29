import requests
from bs4 import BeautifulSoup
from airtable import Airtable
import time

# Airtable API 配置信息
API_KEY = 'your_api_key'
BASE_ID = 'your_base_id'
TABLE_NAME = '北京市互联网行业政策'

# 初始化 Airtable 客户端
at = Airtable(BASE_ID, TABLE_NAME, API_KEY)

def get_policy_data():
    url = 'https://www.example.gov.cn/policies'  # 修改为实际抓取的网址
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    policies = soup.find_all('div', class_='policy')

    for policy in policies:
        policy_name = policy.find('h2').text
        publish_date = policy.find('span', class_='date').text
        institute = policy.find('span', class_='institution').text
        summary = policy.find('p', class_='summary').text
        link = policy.find('a')['href']

        at.insert({
            '政策名称': policy_name,
            '颁布机构': institute,
            '发布日期': publish_date,
            '适用范围': '互联网行业',
            '关键内容摘要': summary,
            '原文链接': link
        })

# 定期运行该函数
get_policy_data()
