import requests

def get_school_id(db):
    url = "https://static-data.gaokao.cn/www/2.0/school/school_code.json"

    data = fetch_data(url)

    if data:
        processed_data = process_school_data(data)
        create_table_sql = '''CREATE TABLE IF NOT EXISTS school_code1
                             (id INTEGER PRIMARY KEY,
                              school_id TEXT,
                              name TEXT)'''
        insert_sql = '''INSERT INTO school_code1 (id, school_id, name) VALUES (?, ?, ?)'''
        db.create_table(create_table_sql)
        db.insert_data(insert_sql, processed_data)
        print("学校数据已成功入库")

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
    for key, value in data.items():
        processed_data.append((key, value['school_id'], value['name']))
    return processed_data