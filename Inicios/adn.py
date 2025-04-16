import re
import timeit

def adn(dna: str) -> str:
    if len(re.findall("[ATCG]", dna)) != len(dna):
        raise ValueError("La cadena contiene caracteres no validos para la complementacion del adn")

    return dna.translate(dna.maketrans("ATCG", "TAGC"))

print(adn("ACGT"))

def obtener_complemento(dna):
    complemento = {
       'A': 'T',
       'T': 'A',
       'C': 'G',
       'G': 'C'
    }
    return''.join([complemento[base]for base in dna]) 
secuencia="GGGT"
print("secuencia original", secuencia)
complemento= obtener_complemento(secuencia) 
print("secuencia complementaria",complemento)

ejecucion1 = timeit.timeit(lambda: adn("ACGT"), number=1000)
print(f"La ejecuciuon fue de: {ejecucion1 / 1000:.6f} segundos")

ejecucion2 = timeit.timeit(lambda: obtener_complemento("ACGT"), number=1000)
print(f"La ejecuciuon fue de: {ejecucion2 / 1000:.6f} segundos")