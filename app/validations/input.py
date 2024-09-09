from ..modules.exceptions import ValueInvalid, ValueIsEmpty

def validate_value(value:float, option:str) -> bool:
    try:
        if value:
            if value > 0:
                return True
            elif value < 0:
                raise ValueInvalid("O valor não pode ser negativo.")
            else:
                raise ValueIsEmpty(f"O valor mínimo de {option.lower()} é R$ 0.1.")
    except ValueInvalid as e:
        print(f"Erro de valor: {e}.")
    return False