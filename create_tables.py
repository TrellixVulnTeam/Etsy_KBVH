_author_ = 'arichland'

import pymysql
import pydict

# SQL DB Connection Fields
sql = pydict.sql_dict.get
user = sql('user')
password = sql('password')
host = sql('host')
charset = sql('charset') + host
cusrorType = pymysql.cursors.DictCursor

print(charset)
def create_tbl_receipts():
    db = sql('db_etsy')
    con = pymysql.connect(user=user,
                          password=password,
                          host=host,
                          database=db,
                          charset=charset,
                          cursorclass=cusrorType)

    with con.cursor() as cur:
        qry_tbl_receipts = """CREATE TABLE IF NOT EXISTS tbl_Etsy_Receipts(
            id INT AUTO_INCREMENT PRIMARY KEY,
            receipt_id BIGINT,adjusted_grandtotal DOUBLE,
            buyer_adjusted_grandtotal DOUBLE,
            buyer_email TEXT,
            buyer_user_id BIGINT,
            city TEXT,
            creation_est DATETIME,
            currency_code TEXT,
            days_from_due_date INT,
            day INT,
            discount_amt DOUBLE,
            first_line TEXT,
            gift_message TEXT,
            grandtotal DOUBLE,
            is_gift TEXT,
            import_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            last_modified_est DATETIME,
            message_from_buyer TEXT,
            message_from_payment TEXT,
            message_from_seller TEXT,
            month INT,
            name TEXT,
            needs_gift_wrap TEXT,
            order_id BIGINT,
            payment_email TEXT,
            payment_method TEXT,
            quarter INT,
            receipt_type TEXT,
            second_line TEXT,
            shipped_date DATETIME,
            state TEXT,
            subtotal DOUBLE,
            total_price DOUBLE,
            total_shipping_cost DOUBLE,
            total_tax_cost DOUBLE,
            total_vat_cost DOUBLE,
            was_paid TEXT,
            was_shipped TEXT,
            week_num INT,
            year INT,
            zip TEXT)
            ENGINE=INNODB;"""
        cur.execute(qry_tbl_receipts)
    con.commit()

def create_tbl_transactions():
    db = sql('db_etsy')
    con = pymysql.connect(user=user,
                          password=password,
                          host=host,
                          database=db,
                          charset=charset,
                          cursorclass=cusrorType)

    with con.cursor() as cur:
        qry_tbl_transactions = """CREATE TABLE IF NOT EXISTS tbl_Etsy_Trans(
            id INT AUTO_INCREMENT PRIMARY KEY,
            buyer_user_id BIGINT,
            currency_code TEXT,
            creation_est DATETIME,
            day INT,
            import_timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
            listing_id BIGINT,
            month INT,
            price DOUBLE,
            paid_est DATETIME,
            quantity INT,
            quarter INT,
            receipt_id BIGINT,
            transaction_id BIGINT,
            week_num INT,
            year INT)
            ENGINE=INNODB;"""
        cur.execute(qry_tbl_transactions)
    con.commit()

def create_tbl_api_log():
    db = sql('db_rtc')
    con = pymysql.connect(user=user,
                          password=password,
                          host=host,
                          database=db,
                          charset=charset,
                          cursorclass=cusrorType)

    with con.cursor() as cur:
        qry_updates = """CREATE TABLE IF NOT EXISTS tbl_API_Log(
        id INT AUTO_INCREMENT PRIMARY KEY,
        timestamp DATETIME,
        api TEXT,
        data TEXT,
        api_code TEXT,
        code_descr TEXT)
        ENGINE=INNODB;"""
    cur.execute(qry_updates)
    con.commit()


def create_tables():
    create_tbl_receipts()
    create_tbl_transactions()
    create_tbl_api_log()
create_tables()