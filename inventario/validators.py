from django.core.exceptions import ValidationError


def validar_minimo_caracteres(value):
    if len(value) < 5:
        raise ValidationError("No se permite menos de 5 caracteres")

def validar_maximo_caracteres(value):
    if len(value) > 100:
        raise ValidationError("No se permite mas de 100 caracteres")


def validar_no_campo_vacio(value):
    if not value:
        raise ValidationError("El %(value)s no puede estar vacio", params={'value':value}, )


def contiene_numero(string):
    return any(char.isdigit() for char in string)

def validar_campo_string(value):
    if contiene_numero(value):
        raise ValidationError(
            '%(value)s no debe contener numeros',
            params={'value': value}
        )