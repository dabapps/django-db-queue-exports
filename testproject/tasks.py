import random

tmp_dir = 'testproject/tmp'

def generate_example_report(export_params):
    array_length = export_params.get('length', None)
    x = []
    for i in range(array_length if array_length else 9999999):
        x.append(random.randint(1, 99999))


    x = x.sort()
    with open(tmp_dir + '/my_export.txt', 'w') as f:
        f.write(f"It worked! We created a sorted array of length {array_length} \n")


    return tmp_dir + "/my_export.txt"