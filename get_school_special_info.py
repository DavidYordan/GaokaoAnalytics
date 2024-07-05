import requests

def get_school_special_info(db):
    url = "https://static-data.gaokao.cn/www/2.0/info/linkage.json"

    data = fetch_data(url)

    if data:
        school_data = process_school_data(data['school'])
        special_data = process_special_data(data['special'])

        create_school_table_sql = '''CREATE TABLE IF NOT EXISTS school_code2
                                     (school_id TEXT PRIMARY KEY,
                                      name TEXT)'''
        insert_school_sql = '''INSERT INTO school_code2 (school_id, name) VALUES (?, ?)'''
        
        create_special_table_sql = '''CREATE TABLE IF NOT EXISTS special_id
                                      (school_id TEXT PRIMARY KEY,
                                       name TEXT)'''
        insert_special_sql = '''INSERT INTO special_id (school_id, name) VALUES (?, ?)'''

        db.create_table(create_school_table_sql)
        db.insert_data(insert_school_sql, school_data)

        db.create_table(create_special_table_sql)
        db.insert_data(insert_special_sql, special_data)

        print("学校代码和专业数据已成功入库")

def fetch_data(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("请求失败，状态码：", response.status_code)
        print("响应内容：", response.text)
        return None
    data = response.json()
    if data.get('message') != "成功":
        print("请求未成功，响应内容：", data)
        return None
    return data.get('data', [])

def process_school_data(data):
    processed_data = []
    for item in data:
        processed_data.append((item['school_id'], item['name']))
    return processed_data

def process_special_data(data):
    processed_data = []
    for item in data:
        processed_data.append((item['id'], item['name']))
    return processed_data
