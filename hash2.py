def ange_batekele_Hash64(donnees):
    if isinstance(donnees, str):
        donnees = donnees.encode('utf-8')

    # Valeur initiale arbitraire (un nombre premier)
    h = 5381

    # Masque pour rester sur 64 bits
    mask = 0xFFFFFFFFFFFFFFFF

    for byte in donnees:
        # Formule : (h * 31) + byte
        # On utilise le modulo (via le masque) pour simuler un débordement 64 bits
        h = ((h * 31) + byte) & mask

    return h


if __name__ == "__main__":
    messages = ["Ange", "bonjour", "bonjouR", "Bonjour"]
    for m in messages:
        print(f"Message: '{m}' -> Hash: {ange_batekele_Hash64(m):016x}")
