#Script para calcular as raízes
import math

#Toda essa função foi dada pelo chat GPT
#Essa função valida as entradas numéricas e recebe como parâmetros os números a,
#b e c e a variável de controle
def validar(a, b, c, var):
    #Esse if teste se o A é válido
    if a == '':
        var.set("O coeficiente A é obrigatório")
        return False
    
    #Esse if testa se os termos B e C são, ambos, strings vazias
    #Note que eu não consegui ajustar o código para atribuir automaticamente
    #a um dos dois o número zero
    if b == '' and c == '':
        var.set("É preciso ao menos um termo para B ou C\n" 
        "Caso não exista o termo B ou C, digite zero")
        return False
    
    #Aqui eu testo para ver ser o número é válido
    for valor in (a, b, c):

        #Aqui eu converto o número para float para poder testá-lo
        try:
            float(valor)

        #Aqui eu trato o erro de valor para evitar entradas que não sejam números
        except ValueError:
            var.set('Digite um número válido')
            return False
    return True

#Essa função foi feita metade por mim, metade pelo chat GPT
#Essa função calcula a equação quadrática e recebe como parâmetros a, b e c e também
#A variável de controle.
def calcular(a, b, c, var):
    """Função para calcular as raízes da função quadrática"""
    
    #Aqui eu chamo a função validar para garantir que as contas fiquem corretas
    if not validar(a, b, c, var):
        return
    
    #Aqui eu calculo o delta
    delta = float(b)**2 - 4 * float(a) * float(c)

    #Aqui eu verifico se o delta é maior que zero
    if delta < 0:
        var.set("Não existem raízes reais")
    else:
        #Aqui eu calculo a raiz x'
        x_1 = (-float(b) + math.sqrt(delta)) / 2 * float(a)

        #Aqui eu calculo a raiz x''
        x_2 = (-float(b) - math.sqrt(delta)) / 2 * float(a)

        #Aqui eu atribuo os resultados à variável de controle
        var.set(f"X' = {x_1:.2f} \n X'' = {x_2:.2f}")
