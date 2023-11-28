FILEPATH = "todo.txt"
def read_file(filepath=FILEPATH):
    with open(filepath, "r") as file_read:
        local_todos = file_read.readlines()
    return local_todos


def write_file(list_arg, filepath=FILEPATH):
    with open(filepath, "w") as file_write:
        file_write.writelines(list_arg)
