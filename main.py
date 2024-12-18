import csv
import os

FILE_NAME = "contacts.csv"

def initialize_csv():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["ID", "Nome", "Telefone", "Email"])

def main_menu():
    while True:
        print("\nAgenda de Contatos")
        print("1. Criar Contato")
        print("2. Listar Contatos")
        print("3. Atualizar Contato")
        print("4. Deletar Contato")
        print("5. Buscar Contato")  # Nova opção
        print("6. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
            list_contacts()
        elif choice == "3":
            update_contact()
        elif choice == "4":
            delete_contact()
        elif choice == "5":  # Nova funcionalidade
            search_contacts()
        elif choice == "6":
            print("Saindo da Agenda. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

def create_contact():
    print("\n--- Criar Novo Contato ---")
    name = input("Nome: ")
    phone = input("Telefone: ")
    email = input("Email: ")

    with open(FILE_NAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        id = sum(1 for _ in open(FILE_NAME)) 
        writer.writerow([id, name, phone, email])
    print("Contato adicionado com sucesso!")

def list_contacts():
    print("\n--- Lista de Contatos ---")
    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader) 
            for row in reader:
                print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}, Email: {row[3]}")
    except FileNotFoundError:
        print("Nenhum contato encontrado. O arquivo ainda não foi criado.")

def update_contact():
    print("\n--- Atualizar Contato ---")
    id_to_update = input("Digite o ID do contato que deseja atualizar: ")
    updated = False

    with open(FILE_NAME, mode="r") as file:
        rows = list(csv.reader(file))

    for row in rows:
        if row[0] == id_to_update:
            print(f"Contato Atual: Nome: {row[1]}, Telefone: {row[2]}, Email: {row[3]}")
            row[1] = input("Novo Nome: ") or row[1]
            row[2] = input("Novo Telefone: ") or row[2]
            row[3] = input("Novo Email: ") or row[3]
            updated = True
            break

    if updated:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")

def delete_contact():
    print("\n--- Deletar Contato ---")
    id_to_delete = input("Digite o ID do contato que deseja deletar: ")
    deleted = False

    with open(FILE_NAME, mode="r") as file:
        rows = list(csv.reader(file))

    new_rows = [row for row in rows if row[0] != id_to_delete]

    if len(new_rows) < len(rows):
        deleted = True

    if deleted:
        with open(FILE_NAME, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerows(new_rows)
        print("Contato deletado com sucesso!")
    else:
        print("Contato não encontrado.")

def search_contacts():
    print("\n--- Buscar Contato ---")
    keyword = input("Digite o termo de busca (Nome, Telefone ou Email): ").lower()
    found = False

    try:
        with open(FILE_NAME, mode="r") as file:
            reader = csv.reader(file)
            next(reader)
            print("\nResultados da busca: ")
            for row in reader:
                if keyword in row[1].lower() or keyword in row[2].lower() or keyword in row[3].lower():
                    print(f"ID: {row[0]}, Nome: {row[1]}, Telefone: {row[2]}, Email: {row[3]}")
                    found = True
        if not found:
            print("Nenhum contato encontrado com o termo informado.")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

if __name__ == "__main__":
    initialize_csv()
    main_menu()