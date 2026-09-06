def find_log_entries(file, type):
    with open(file) as f:
        for line in f:
            if type in line:
                print(line)


find_log_entries('../../data_test/application.log', 'ERROR')
