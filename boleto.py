multa = 2
taxa = 0.05
boleto = float(input("Quanto custa o boleto? "))
dias = int(input("Com quantos dias o boleto está com atraso? "))

total = boleto + multa + (boleto * taxa * dias)

print(f"Seu boleto de R$ {boleto:.2f} agora é de R$ {total:.2f}.")