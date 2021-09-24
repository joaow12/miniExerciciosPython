#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

nome = input("Digite um nome de usuário: ")
senha = input("Digite a senha do usuário: ")

while(senha == nome):
    print("A senha não pode ser igual o nome do usuário")
    senha = input("Digite a senha do usuário: ")
 
print('Ciclo encerrado. \nNome de usuário: {0} \nSenha: {1}'.format(nome, senha))