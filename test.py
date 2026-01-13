from validate_docbr import CPF

cpf = CPF()

if cpf.validate("04326673001"):
    print("CPF válido")
else:    
    print("CPF inválido")