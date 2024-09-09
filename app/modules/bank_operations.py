from .exceptions import OperationFailed, ClientNotFound, InsuficientFunds
from datetime import time


def _depositar(cliente: dict, valor_deposito: float) -> bool:
    try:
        if cliente:
            if "saldo" in cliente:
                saldo = cliente.get("saldo")
                cliente.update("saldo", saldo + valor_deposito)
                extrato = cliente.get("extrato")
                extrato.append(f"Depositado: {valor_deposito} as {time()}")
                return True
            else:
                raise OperationFailed("Saldo não encontrado.")
        else:
            raise ClientNotFound("Cliente não encontrado.")
    except ClientNotFound as e:
        print(f"Erro do Sistema: {e}")
    except OperationFailed as e:
        print(f"Erro de Operação: {e}")
    return False


def _sacar(cliente: dict, valor_saque: float) -> bool:
    try:
        if cliente:
            if "saldo" in cliente:
                saldo = cliente.get("saldo")
                if saldo >= valor_saque:
                    cliente.update("saldo", saldo - valor_saque)
                    return True
                else:
                    raise InsuficientFunds("Saldo insuficiente.")
            else:
                raise OperationFailed("Saldo não encontrado.")
        else:
            raise ClientNotFound("Cliente não encontrado.")
    except InsuficientFunds as e:
        print(f"Erro ao Sacar: {e}")
    except ClientNotFound as e:
        print(f"Erro do Sistema: {e}")
    except OperationFailed as e:
        print(f"Erro de Operação: {e}")
    return False


def _extrato(cliente: dict) -> None:
    try:
        if cliente:
            if "extrato" in cliente:
                extrato = cliente.get("extrato")
                if extrato:
                    for dado in extrato:
                        print(dado)
                else:
                    raise OperationFailed("Extrato está vazio.")
            else:
                raise OperationFailed("Extrato não encontrado.")
        else:
            raise ClientNotFound("Cliente não encontrado.")
    except InsuficientFunds as e:
        print(f"Erro ao Sacar: {e}")
    except ClientNotFound as e:
        print(f"Erro do Sistema: {e}")
    except OperationFailed as e:
        print(f"Erro de Operação: {e}")
