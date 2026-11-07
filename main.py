from functions import read_file , save_file

if __name__ == "__main__":
    clean_data = read_file("estoque_sujo.txt")

    if clean_data:
        save_file("produtos_limpos.txt", clean_data)
        print("Arquivo processado com sucesso")