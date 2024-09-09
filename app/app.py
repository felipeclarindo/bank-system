from .utils.utils import clear
from .modules.bank_operations import _depositar, _sacar
from .validations.input import validate_value


class App:
    def __init__(self) -> None:
        self.usuario = {
            "nome": "Teste",
            "saldo": 200,
            "extrato": []
        }

    def menu(self) -> None:
        clear()
        print("-" * 24)
        print("--------- Bank ---------")
        print("-" * 24)
        print("[1] Deposito")
        print("[2] Saque")
        print("[3] Extrato")

    def menu_option(self, option: str) -> None:
        clear()
        print("-" * (20 + len(option)))
        print(f"--------- {option.title()} ---------")
        print("-" * (20 + len(option)))

    def deposito(self):
        try:
            value_valid = False
            while not value_valid:
                self.menu_option("Deposito")
                valor = float(input("Informe o valor para deposito: "))
                value_valid = validate_value(valor, "deposito")
                if not value_valid:
                    input("APERTE ENTER PARA CONTINUAR")
            _depositar(self.usuario, valor)
        except Exception as e:
            print(f"Erro: {e}.")

    def saque(self):
        value_valid = False
        while not value_valid:
            self.menu_option("Saque")
            valor = float(input("Informe o valor para deposito: "))
            value_valid = validate_value(valor, "deposito")
            if not value_valid:
                input("APERTE ENTER PARA CONTINUAR")
        _sacar(self.usuario, valor)

    def extrato(self):
        self.menu_option("Extrato")
        input("APERTE ENTER PARA CONTINUAR")



    def run(self) -> None:
        try:
            while True:
                self.menu()
                op = input("Informe a opção desejada: ")
                match op:
                    case "1":
                        self.deposito()
                    case "2":
                        self.saque()
                    case "3":
                        self.extrato()
                    case "4":
                        print("Programa Finalizado!")
                        input("APERTE ENTER PARA CONTINUAR")
                        break
                    case _:
                        print("Opção Invalida!")
                        input("APERTE ENTER PARA CONTINUAR")
                        continue
        finally:
            self.menu_option("Finalizado")
