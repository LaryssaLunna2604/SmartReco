# model.py

produtos_por_categoria = {
    "tecnologia": ["Notebook", "Mouse", "Teclado", "Monitor"],
    "livros": ["Python Básico", "Introdução à IA", "Algoritmos"],
    "jogos": ["Headset", "Controle", "Mouse Gamer"],
    "casa": ["Aspirador", "Ventilador", "Lâmpada Smart"]
}

def recomendar(categoria):
    categoria = categoria.lower()
    return produtos_por_categoria.get(categoria, [])
