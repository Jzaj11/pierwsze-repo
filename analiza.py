import statistics

wyniki = [4.5, 3.0, 5.0, 4.0, 3.5]

print("Liczba ocen:", len(wyniki))
print("średnia:", statistics.mean(wyniki))

najwyzsza_ocena=(max(wyniki))

print("Mediana:", statistics.median(wyniki))
