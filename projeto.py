def desbloquear_celular():
  senha_correta = "1234"  
  tentativas_restantes = 3

  while tentativas_restantes > 0:
    senha_digitada = input("Digite sua senha: ")

    if senha_digitada == senha_correta:
      return "Bem vindo!"
    else:
      tentativas_restantes -= 1
      print(f"Senha incorreta. Você tem {tentativas_restantes} tentativas até o bloqueio.")

  return "Celular bloqueado!"

resultado = desbloquear_celular()
print(resultado)