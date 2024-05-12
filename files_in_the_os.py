import os
import time

directory = '/Users/kurdyukov/PycharmProjects'
for dirpath, dirnames, filenames in os.walk(directory):
    print('*' * 27)
    print(dirpath, dirnames, filenames)
    print(os.path.dirname(dirpath))
    for file in filenames:
        full_name_path = os.path.join(dirpath, file)
        secs =  os.path.getmtime(full_name_path)
        file_time = time.gmtime(secs)
        if file_time[0] == 2024:
            print(full_name_path, secs)
print(os.path.getsize(dirpath))