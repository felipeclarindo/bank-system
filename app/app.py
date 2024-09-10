from .utils.utils import clear
from .modules.bank_operations import _depositar, _sacar, _extrato
from .validations.input import validate_value
from time import sleep

class App:
    def __init__(self) -> None:
        self.cliente = {
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

    def menu_option(self, operation: str) -> None:
        clear()
        print("-" * (20 + len(operation)))
        print(f"--------- {operation.title()} ---------")
        print("-" * (20 + len(operation)))

    def deposito(self, operation:str):
        try:
            value_valid = False
            while not value_valid:
                try:
                    self.menu_option(operation)
                    valor = str(input("Informe o valor para deposito: "))
                    value_valid = validate_value(valor, operation)
                    if not value_valid:
                        input("APERTE ENTER PARA CONTINUAR")
                except Exception as e:
                    print(f"Erro: {e}")
                    input("APERTE ENTER PARA CONTINUAR")
            valor = float(valor)
            deposito_valido = _depositar(self.cliente, valor)
            if deposito_valido:
                self.menu_option(operation)
                print("Realizando deposito...")
                sleep(1)
                self.menu_option(operation)
                print("Deposito efetuado com sucesso.")
                input("APERTE ENTER PARA CONTINUAR")
            else:
                input("APERTE ENTER PARA CONTINUAR")
                self.confirmar_saida()
        except Exception as e:
            print(f"Erro: {e}.")
            input("APERTE ENTER PARA CONTINUAR")

    def saque(self, operation:str) -> bool:
        try:
            value_valid = False
            while not value_valid:
                self.menu_option(operation)
                valor = str(input("Informe o valor para saque: "))
                value_valid = validate_value(valor, operation)
                if not value_valid:
                    input("APERTE ENTER PARA CONTINUAR")
            valor = float(valor)
            saque_valid = _sacar(self.cliente, valor)
            if saque_valid:
                self.menu_option("operation")
                print("Realizando saque...")
                sleep(1)
                self.menu_option(operation)
                print("Saque efetuado com sucesso.")
                input("APERTE ENTER PARA CONTINUAR")
            else:
                input("APERTE ENTER PARA CONTINUAR")
        except ValueError as e:
            print(f"Erro de valor: {e}")
            input("APERTE ENTER PARA CONTINUAR")
        except Exception as e:
            print(f"Erro: {e}")
            input("APERTE ENTER PARA CONTINUAR")

    def extrato(self, operation: str):
        try:
            self.menu_option(operation)
            _extrato(self.cliente)
            input("APERTE ENTER PARA CONTINUAR")
        except Exception as e:
            print(f"Erro: {e}")
            input("APERTE ENTER PARA CONTINUAR")

    def confirmar_saida(self, operation: str) -> bool:
        saida_valida = False
        while not saida_valida:
            self.menu_option(operation)
            saida = str(input("Deseja voltar para o menu? "))
            if saida.lower() in ["sim", "s", "n", "não", "nao"]:
                return True, saida
            else:
                print("Resposta com sim ou não.")
            if not saida_valida:
                input("APERTE ENTER PARA CONTINUAR")
        return False
    
    def run(self) -> None:
        try:
            continuar = False
            while not continuar:
                self.menu()
                op = input("Informe a opção desejada: ")
                match op:
                    case "1":
                        sair = False
                        while not sair:
                            operation = "deposito"
                            self.deposito(operation)
                            confirm = False
                            while not confirm:
                                confirm, response = self.confirmar_saida(operation)
                            if response.lower() in ["sim", "s"]:
                                sair = True
                                self.menu_option(operation)
                                print("Voltando para o menu...")
                                sleep(1)
                            else:
                                continue   
                    case "2":
                        sair = False
                        while not sair:
                            operation = "saque"
                            self.saque(operation)
                            confirm = False
                            while not confirm:
                                confirm, response = self.confirmar_saida(operation)
                            if response.lower() in ["sim", "s"]:
                                sair = True
                                self.menu_option(operation)
                                print("Voltando para o menu...")
                                sleep(1)
                            else:
                                continue    
                    case "3":
                        sair = False
                        while not sair:
                            operation = "extrato"
                            self.extrato(operation)
                            confirm = False
                            while not confirm:
                                confirm, response = self.confirmar_saida(operation)
                            if response.lower() in ["sim", "s"]:
                                sair = True
                                self.menu_option(operation)
                                print("Voltando para o menu...")
                                sleep(1)
                            else:
                                continue   
                    case "4":
                        continuar = True
                        print("Programa Finalizado!")
                        input("APERTE ENTER PARA CONTINUAR")
                        break
                    case _:
                        print("Opção Invalida!")
                        input("APERTE ENTER PARA CONTINUAR")
                        continue
        except Exception as e:
            print(f"Erro: {e}")
