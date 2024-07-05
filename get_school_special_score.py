import requests
import time

def get_school_special_score(db):
    columns = [
        'batch_type', 'year', 'school_id', 'special_id', 'type', 'batch', 'zslx', 'max',
        'min', 'average', 'min_section', 'province', 'spe_id', 'info', 'special_group', 'first_km',
        'sp_type', 'sp_fxk', 'sp_sxk', 'sp_info', 'sp_xuanke', 'is_score_range', 'min_range',
        'min_rank_range', 'level1_name', 'level2_name', 'level3_name', 'level1', 'level2', 'level3',
        'spname', 'zslx_name', 'local_batch_name', 'sg_fxk', 'sg_sxk', 'sg_type', 'sg_name',
        'sg_info', 'sg_xuanke', 'range_max_rank'
    ]
    years = [2019, 2020, 2021, 2022, 2023]
    school_ids = get_all_school_ids(db)
    table_name = 'school_special_score'

    for school_id in school_ids:
        for year in years:
            url = f"https://static-data.gaokao.cn/www/2.0/schoolspecialscore/{school_id}/{year}/35.json"
            data = fetch_data_with_retry(url)
            if data:
                create_table(db, table_name, columns)
                insert_data(db, table_name, data, columns, year)
                print(f"学校 {school_id} 年份 {year} 数据已入库")
            else:
                print(f"学校 {school_id} 年份 {year} 无数据")

def get_all_school_ids(db):
    select_sql = "SELECT school_id FROM school_code2"
    rows = db.fetch_all(select_sql)
    return [row[0] for row in rows]

def fetch_data_with_retry(url, max_retries=5):
    delay = 1
    for _ in range(max_retries):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                data = response.json()
                if data.get('message') == "成功":
                    return data.get('data', [])
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
    for key, value in data.items():
        if 'item' in value and value['item']:
            for item in value['item']:
                item['batch_type'] = key
                item['year'] = year
                insert_sql = f'''INSERT INTO {table_name} ({", ".join(columns)}) VALUES
                                ({", ".join(["?" for _ in columns])})'''
                db.insert_data(insert_sql, [tuple([item.get(col, '') for col in columns])])
