# Sukurkite funkciją, kuri sudaugintų (NxN) matricas (two dimensional arrays) ir gražintų rezultatą.

# 🤷‍♂️ Čia nėra jokių konkrečių nurodymų 🤷‍♂️ Pagalvokite, ką darytumėte, jei jums būtų duota tokia užduotis darbe.

A = [[5, 2], [3,1]]
B = [[4, 6], [5,2]]

def multiply_arrays(a, b):
    result = [[0, 0], [0, 0]]
    for i in range(len(a)):                        # rows a
        for j in range(len(b[0])):                 # columns b
            for k in range(len(b)):                # rows b
                result[i][j] += a[i][k] * b[k][j]
    return result

print(multiply_arrays(A, B))
