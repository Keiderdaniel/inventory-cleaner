def read_file(file_name):
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            data = []
            for l in f:
                clean_line = l.strip().upper()
                if clean_line:
                    data.append(clean_line)
            return data
    except FileNotFoundError:
        print(f'The file {file_name} was not found')
        return []

def save_file(output_filename, data_list):
    with open("output_filename", "w", encoding="utf-8") as f:
        for i in data_list:
            f.write(i + "\n" )
