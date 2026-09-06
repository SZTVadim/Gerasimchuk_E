def find_log_entries(file, type_log):
    with open(file) as f:
        for line in f:
            if type_log in line:
                print(line)


find_log_entries('../../data_test/application.log', 'ERROR')
