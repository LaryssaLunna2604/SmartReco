# main.py

from model import recomendar

print("=== SmartReco ===")
print("Categorias disponíveis:")
print("Tecnologia | Livros | Jogos | Casa")

categoria = input("Digite uma categoria: ")

recomendacoes = recomendar(categoria)

if recomendacoes:
    print("\nProdutos recomendados:")
    for produto in recomendacoes:
        print(f"- {produto}")
else:
    print("\nCategoria não encontrada.")
