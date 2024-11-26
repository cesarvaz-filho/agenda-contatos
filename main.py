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
        print("5. Sair")
        choice = input("Escolha uma opção: ")

        if choice == "1":
            create_contact()
        elif choice == "2":
        elif choice == "3":
        elif choice == "4":
        elif choice == "5":
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