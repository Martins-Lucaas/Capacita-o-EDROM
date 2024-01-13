def main():
    n = int(input())
    arr = list(map(int, input().split()))
    listaOrdenada = sorted(set(arr), reverse=True)

    if len(listaOrdenada) >= 2:
        runnerup = listaOrdenada[1]
        print(runnerup)
    else:
        print("Não há runner-up, pois todos os elementos são iguais.")

main()
