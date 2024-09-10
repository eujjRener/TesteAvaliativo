def completar_sequencias():
    # a) 1, 3, 5, 7, ___ (Números ímpares)
    seq_a = [1, 3, 5, 7]
    seq_a.append(seq_a[-1] + 2)
    
    # b) 2, 4, 8, 16, 32, 64, ____ (Cada número é o dobro do anterior)
    seq_b = [2, 4, 8, 16, 32, 64]
    seq_b.append(seq_b[-1] * 2)
    
    # c) 0, 1, 4, 9, 16, 25, 36, ____ (Quadrados perfeitos)
    seq_c = [0, 1, 4, 9, 16, 25, 36]
    seq_c.append((len(seq_c)) ** 2)
    
    # d) 4, 16, 36, 64, ____ (Quadrados de números pares)
    seq_d = [4, 16, 36, 64]
    next_num_d = (2 * len(seq_d)) ** 2
    seq_d.append(next_num_d)
    
    # e) 1, 1, 2, 3, 5, 8, ____ (Sequência de Fibonacci)
    seq_e = [1, 1, 2, 3, 5, 8]
    seq_e.append(seq_e[-1] + seq_e[-2])
    
    # f) 2, 10, 12, 16, 17, 18, 19, ____ (Números sem dígito '3')
    seq_f = [2, 10, 12, 16, 17, 18, 19]
    next_num_f = 20
    while '3' in str(next_num_f):
        next_num_f += 1
    seq_f.append(next_num_f)
    
    print(f"a) {seq_a}")
    print(f"b) {seq_b}")
    print(f"c) {seq_c}")
    print(f"d) {seq_d}")
    print(f"e) {seq_e}")
    print(f"f) {seq_f}")

completar_sequencias()
