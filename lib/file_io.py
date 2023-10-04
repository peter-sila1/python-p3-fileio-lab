def write_file(file_name, file_content):
    
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as file_text:
        file_text.write(file_content)

def append_file(file_name, append_content):
    
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file_text:
        file_text.write(append_content)

def read_file(file_name):
    
    with open(f"{file_name}.txt", mode='r', encoding='utf-8') as file_text:
        return file_text.read()
write_file(file_name="logfile", file_content="Log 1: 5 bananas added" )
append_file(file_name="logfile", append_content="Log 2: 3 bananas subtracted")

read_file(file_name="logfile")
