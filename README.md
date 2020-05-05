# pdf-to-csv

## Setup

`Using Python 3.6+`

### Environment Setup

* **`Linux`** Systems:

    ```shell
    sudo pip3 install virtualenv

    virtualenv -p python3 venv --no-site-packages

    source venv/bin/activate

    pip3 install -r requirements.txt
    ```

    ```shell
    deactivate
    ```

* **`Windows`** Systems:

    ```shell
    pip3 install virtualenv

    virtualenv -p python3 venv --no-site-packages

    venv\Scripts\activate

    pip3 install -r requirements.txt
    ```

    ```shell
    venv\Scripts\deactivate
    ```

    If getting issue in installing virtualenv on `windows`, use administrator privileges

### SQL Setup

Run `dump.sql` to setup sql

## Running

1. Activate your `venv`
2. Go to `./app` and run `app.py`
3. Open `http://127.0.0.1:5000/` in browser.

To change any default variables go to `./app/params.py` and change any of the following
```Python
# parameters used throughout the program

# SQL connection
host = "localhost"
username = "root"
password = ""
db_name = "bsdb"
# table name in SQL
table_name = "BalanceSheet"

# file location for upload and download temps
local_pdf = r'in.pdf'
local_csv = r'out.csv'
```
