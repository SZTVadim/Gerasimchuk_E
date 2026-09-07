from pathlib import Path

def find_log_entries(file, type_log):
    with open(file) as f:
        for line in f:
            if type_log in line:
                print(line)

BASE_ROOT = Path(__file__).resolve().parent.parent.parent
find_log_entries(str(BASE_ROOT / 'data_test' / 'application.log'), 'ERROR')
