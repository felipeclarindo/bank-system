from .exceptions import OperationFailed, ClientNotFound, InsuficientFunds
from datetime import datetime


def _depositar(cliente: dict, valor_deposito: float) -> bool:
    try:
        if cliente:
            if "saldo" in cliente:
                saldo = cliente.get("saldo")
                if valor_deposito > 0:
                    saldo += valor_deposito
                else:
                    raise OperationFailed("O valor de deposito minimo é 0.1")
                cliente.update({"saldo": saldo})
                extrato = cliente.get("extrato")
                data = datetime.now().timetuple()
                extrato.append(f"Depositado: R${valor_deposito:.2f} as {data.tm_hour if len(str(data.tm_hour)) > 1  else f"0{data.tm_hour}"}:{data.tm_min if len(str(data.tm_min)) > 1 else f"0"}:{data.tm_sec if len(str(data.tm_sec).strip()) > 1 else f"0{data.tm_sec}"} dia {data.tm_mday if len(str(data.tm_mday).strip()) > 1 else f"0{data.tm_mday}"}:{data.tm_mon if len(str(data.tm_mon).strip()) > 1 else f"0{data.tm_mon}"}:{data.tm_year if len(str(data.tm_year)) > 1 else f"0{data.tm_year}"} ")
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
                    cliente.update({"saldo": valor_saque})
                    extrato = cliente.get("extrato")
                    data = datetime.now().timetuple()
                    extrato.append(f"Sacando: R${valor_saque:.2f} as {data.tm_hour if len(str(data.tm_hour)) > 1  else f"0{data.tm_hour}"}:{data.tm_min if len(str(data.tm_min)) > 1 else f"0"}:{data.tm_sec if len(str(data.tm_sec).strip()) > 1 else f"0{data.tm_sec}"} dia {data.tm_mday if len(str(data.tm_mday).strip()) > 1 else f"0{data.tm_mday}"}:{data.tm_mon if len(str(data.tm_mon).strip()) > 1 else f"0{data.tm_mon}"}:{data.tm_year if len(str(data.tm_year)) > 1 else f"0{data.tm_year}"} ")
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