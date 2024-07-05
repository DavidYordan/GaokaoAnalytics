import requests
import time

def get_score_section(db):
    columns = [
        'year', 'score', 'num', 'total', 'rank_range', 'batch_name', 'controlscore', 'rank'
    ]
    table_name = 'score_section'

    create_table(db, table_name, columns)

    for year in [2024, 2023, 2022, 2021]:
        url = f"https://static-data.gaokao.cn/www/2.0/section2021/{year}/35/2073/3/lists.json"
        data = fetch_data_with_retry(url)
        insert_data(db, table_name, data, columns, year)
        print(f"{year} 数据已入库")

    for year in [2020, 2019]:
        url = f"https://static-data.gaokao.cn/www/2.0/section2021/{year}/35/1/3/lists.json"
        data = fetch_data_with_retry(url)
        insert_data(db, table_name, data, columns, year)
        print(f"{year} 数据已入库")

def fetch_data_with_retry(url, max_retries=5):
    delay = 1
    for _ in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get('message') == "成功":
                    return data.get('data', {}).get('search', {})
                else:
                    print("请求未成功，响应内容：", data)
            elif response.status_code == 404:
                print("请求失败，状态码： 404")
                print("响应内容：", response.text)
                return None
            else:
                print("请求失败，状态码：", response.status_code)
                print("响应内容：", response.text)
        except requests.exceptions.RequestException as e:
            print("请求异常：", e)
        
        time.sleep(delay)
        delay *= 2
    return None

def create_table(db, table_name, columns):
    create_table_sql = f'''CREATE TABLE IF NOT EXISTS {table_name}
                            (id INTEGER PRIMARY KEY, {", ".join([f"{col} TEXT" for col in columns])})'''
    db.create_table(create_table_sql)

def insert_data(db, table_name, data, columns, year):
    for _, item in data.items():
        item['year'] = year
        insert_sql = f'''INSERT INTO {table_name} ({", ".join(columns)}) VALUES
                        ({", ".join(["?" for _ in columns])})'''
        db.insert_data(insert_sql, [tuple([item.get(col, '') for col in columns])])