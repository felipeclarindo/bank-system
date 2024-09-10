from ..modules.exceptions import ValueInvalid, ValueIsEmpty

def validate_value(value:str, option:str) -> bool:
    try:
        if value.replace(".", "").isdigit():
            if float(value) > 0:
                return True
            else:
                raise ValueInvalid(f"O valor minimo para {option.lower()} é R$0.1")
        else:
            raise ValueError("O valor precisa ser um número.")
    except ValueIsEmpty as e:
        print(f"Erro de Captura: {e}")
    except ValueInvalid as e:
        print(f"Erro de valor: {e}.")
    except ValueError as e:
        print(f"Valor Ínvalido: {e}")
    return False