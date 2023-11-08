# Escreva um programa para resolver o seguinte problema: você tem dois jarros:
# um de 4 litros e outro de 3 litros. Nenhum dos jarros tem marcações.
# Existe uma torneira que pode ser usada para encher os jarros com água.
# Como você pode obter exatamente dois litros de água no jarro de 4 litros?


def EncherJarro4L(j4, j3):
    if j4 == 2:
        return j4, j3
    if j4 == 4:
        j4 = 0
    else:
        j4 = 4
    return EsvaziarJarro3L(j4, j3)

def EsvaziarJarro3L(j4, j3):
    if j3 == 0:
        return j4, j3
    j3 = 0
    return EncherJarro4L(j4, j3)

j4, j3 = EncherJarro4L(0, 0)

print(f"Resultado: Jarro de 4 litros contém {j4} litros, Jarro de 3 litros contém {j3} litros.")
