import re

## Método 1
cpf = "098.531.136-78"
cpf_limpo = cpf.replace(".","").replace("-","")
print(cpf_limpo)


## Método 2

cpf_limpo2 = re.sub(r"\D","",cpf)
print(cpf_limpo2)