from sqliteDB import SQLiteDB
from get_school_id import get_school_id
from get_school_info import get_school_info
from get_school_special_info import get_school_special_info
from get_school_special_score import get_school_special_score
from get_school_special_plan import get_school_special_plan
from get_score_section import get_score_section

def main():
    db = SQLiteDB('data/gaokao.db')

    # get_school_id(db)
    # get_school_info(db)
    # get_school_special_info(db)
    # get_school_special_score(db)
    # get_school_special_plan(db)
    get_score_section(db)
    
    db.close()

if __name__ == "__main__":
    main()

# 疑似职业 https://mnzy.gaokao.cn/api/cp/queryAllList