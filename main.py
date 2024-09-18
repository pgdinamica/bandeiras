import os
from PIL import Image
from cores import VERDE, AMARELO, AZUL, BRANCO
from formas import pintar_losango, pintar_circulo, pintar_faixa

IMG_DIR = "img"
filename = os.path.join(IMG_DIR, "brasil.png")

def bandeira_brasileira(largura):
    M = largura / 14
    comprimento = int(20 * M)
    img = Image.new("RGB", (comprimento, largura), VERDE)
    dist_vertices = 1.7 * M
    vertices_losango = [
        (dist_vertices, largura / 2),
        (comprimento / 2, dist_vertices),
        (comprimento - dist_vertices, largura / 2),
        (comprimento / 2, largura - dist_vertices)
    ]
    print(vertices_losango)
    pintar_losango(img, vertices_losango, AMARELO)
    centro = (comprimento // 2, largura // 2)
    raio = 3.5 * M
    pintar_circulo(img, centro, raio, AZUL)
    centro_arcos = (comprimento / 2 - 2 * M, largura - 1)
    rmenor = 8 * M
    rmaior = 8.5 * M
    pintar_faixa(img, centro_arcos, 
                  (rmenor, rmaior), (centro, raio),
                  BRANCO)
    return img

if __name__ == '__main__':
    img = bandeira_brasileira(1400)
    img.save(os.path.join(IMG_DIR, "br-passo4.png"))