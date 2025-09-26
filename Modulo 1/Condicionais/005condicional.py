# crie um codigo python que verifique se senha esta correta
# pelo usuario for "1234", exiba "acesso permitido". 





senha_usuario = "1234"

senha = input("digite sua senha: ")

if senha == senha_usuario:
 print("acesso liberado")
else:
 print("acesso negado. tente novamente")