import requests

def get_school_info(db):
    url = "https://static-data.gaokao.cn/www/2.0/school/list_v2.json"

    data = fetch_data(url)

    if data:
        processed_data = process_school_info_data(data)
        create_table_sql = '''CREATE TABLE IF NOT EXISTS school_info
                             (id INTEGER PRIMARY KEY,
                              name TEXT,
                              f985 TEXT,
                              f211 TEXT,
                              province TEXT,
                              city TEXT,
                              qj TEXT,
                              answerurl TEXT,
                              dual_class TEXT,
                              nature TEXT,
                              level TEXT)'''
        insert_sql = '''INSERT INTO school_info (id, name, f985, f211, province, city, qj, answerurl, dual_class, nature, level) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)'''
        db.create_table(create_table_sql)
        db.insert_data(insert_sql, processed_data)
        print("学校基本信息已成功入库")

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

def process_school_info_data(data):
    processed_data = []
    for key, value in data.items():
        processed_data.append((key, value['name'], value['f985'], value['f211'], value['p'], value['c'], value['qj'], value['answerurl'], value['dual_class'], value['nature'], value['level']))
    return processed_data
