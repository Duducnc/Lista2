taxas_de_cambio = {
    'DOLAR': 5.06,
    'EURO': 5.37,
    'PESO':0.14,
    'LIBRA': 6.22,
}
def converter_moeda(v, moeda_destino):
    if moeda_destino in taxas_de_cambio:
        taxa_dest = taxas_de_cambio[moeda_destino]
        v_convertido = v / taxa_dest
        return v_convertido
    else:
        return "Moeda de destino não suportada."
def main():
    print("Bem-vindo ao Conversor Plus!")
    while True:
        v = float(input("Digite o valor em Reais (BRL)para ser convertido: "))
        moeda_destino = input("Digite a moeda de destino (ex: DOLAR,EURO,PESO,LIBRA): ").upper()
        resultado = converter_moeda(v, moeda_destino)
        if isinstance(resultado, float):
            print(f"R${v:.2f} equivalem a {resultado:.2f} {moeda_destino}")
        else:
            print(resultado)
        continuar = input("Deseja fazer outra conversão? (SIM/NÃO): ").strip().lower()
        if continuar != "SIM":
            print("Obrigado por usar o Conversor Plus.!")
            break
if __name__ == "__main__":
    main()