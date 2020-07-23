import random


def generate_example_report(export_params):
    array_length = export_params.get("length", None)
    x = []
    for i in range(array_length if array_length else 9999999):
        x.append(random.randint(1, 99999))

    x = x.sort()
    tmp_dir = "testproject/tmp"

    return tmp_dir + "/my_export.txt"
