from model import model_lead
import control
def add_lead():
    name = input("Informe o nome do Lead")
    email = input("Informe o email do Lead")
    stage = input("Etapa do Funil:")

    print(model_lead(name,email,stage))

    control.create_lead(model_lead(name,email,stage))

    print("Lead Adicionado (func)")

def list_leads():
    leads = control.read_leads()
    print(leads)

def main():
    while True:
        print("\nMini CRM de Leads")
        print("[1] Adicionar Lead")
        print("[2] Listar Lead")
        print("[0] Sair do Programa")

        opt = input("Escolha uma opção")

        if opt == "1":
            add_lead()
        elif opt == "2":
            list_leads()
        elif opt == "0":
            print("Até Mais...")
            break
        else:
            print("Opção invalida!")

if __name__ == "__main__":
    main()