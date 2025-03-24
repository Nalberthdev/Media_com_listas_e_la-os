x = input("Digite sua condição lógica! Ex: P e Q, P ou Q, P se Q, P se somente se (ses) Q:  ")
condicao = [True, False]


for i in range(len(condicao)):
    for l in range(0,2):
        P = condicao[i]
        Q = condicao[l]
        e = P and Q
        ou = P or Q
        se = not P or Q
        ses  = P == Q


        if x == "P ou Q":
            print(f"{P}  {Q}  |========== {ou}")
        if x == "P e Q":
            print(f"{P}  {Q}  |========== {e}")
        if x == "P se Q":
            print(f"{P}  {Q}  |========== {se}")
        if x == "P se somente se Q":
            print(f"{P}  {Q}  |========== {ses}")
else:
    print('Entrada inválida')