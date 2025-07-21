from Crypto.PublicKey import RSA
with open("p.pem", "rb") as f:
    key = RSA.import_key(f.read())
    p, q, n = key.p, key.q, key.n
    print("p =", p)
    print("q =", q)
    print("n =", n)
