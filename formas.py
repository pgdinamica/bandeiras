def pintar_diagonal(img, cor):
    canva = img.load()
    width, height = img.size
    a = (height - 1) / (width - 1)
    for i in range(width): # x
        for j in range(height): # y
            if  a * i <= j:
                canva[i, j] = cor

def pintar_losango(img, vertices, cor):
    canva = img.load()
    width, height = img.size

    coefs_a = []
    coefs_b = []
    for n in range(len(vertices)):
        p = vertices[n]
        q = vertices[(n + 1) % len(vertices)]
        a = (p[1]- q[1]) / (p[0] - q[0])
        b = p[1] - (p[0] * a)
        coefs_a.append(a)
        coefs_b.append(b)
    # print("M:", m)
    for i in range(width): # x
        for j in range(height): # y
            if (
                (j >= coefs_a[0] * i + coefs_b[0]) 
                and (j >= coefs_a[1] * i + coefs_b[1])
                and (j <= coefs_a[2] * i + coefs_b[2])
                and (j <= coefs_a[3] * i + coefs_b[3])
                ):
                canva[i, j] = cor

def pintar_circulo(img, centro, raio, cor):
    canva = img.load()
    width, height = img.size
    cx, cy = centro
    r2 = raio**2
    for i in range(width):
        for j in range(height):
            d2 = (cx - i)**2 + (cy - j)**2
            if d2 <= r2:
                canva[i, j] = cor

def pintar_faixa(img, centro, raios, circ_ext, cor):
    canva = img.load()
    width, height = img.size
    cx, cy = centro
    r2_menor = raios[0]**2
    r2_maior = raios[1]**2
    c_ext = circ_ext[0]
    r2_ext = circ_ext[1]**2
    for i in range(width):
        for j in range(height):
            d2 = (cx - i)**2 + (cy - j)**2
            d2_ext = (c_ext[0] - i)**2 + (c_ext[1] - j)**2
            if (d2 <= r2_maior and
                d2 >= r2_menor and
                # GAMBIARRA
                d2_ext <= r2_ext
                ):
                canva[i, j] = cor
