
numero01=int(input("me de o primeiro numero para efetuar a conta..."))

numero02=int(input("me de o segundo numero para concluir o calculo..."))

conta= numero01 + numero02
print(f"{conta}")

if conta >= 50:
    print("vc ganhou 5 reais de desconto...")
    conta03=conta - 5 
    print(f"seu valor final é de {conta03}")

if conta >= 100:
    print("vc ganhou 10 reais de desconto..")
    conta02=conta - 10
    print(f"seu valor final é de {conta02} ")
else :
    print(f"sua conta tinha dado {conta}")