'''
Questo file è lo scheletro per risolvere la prima parte del giorno 5 dell'Advent of Code 2025 (https://adventofcode.com/2025/day/5).
La funzione `parse_exercise` converte il file prodotto dal portale dell'AoC in un dizionario organizzato come segue:
    {
        id_fresh: list[tuple[int, int]]
        ingredienti: list[int]
    }
dove:
    - `id_fresh` è la lista dei range di ID dei prodotti freschi;
    - `ingredienti` è la lista degli ID degli ingredienti disponibili.
'''


from parser import ExerciseInput, parse_exercise


def main():
    database: ExerciseInput = parse_exercise("./demo.txt")

    fresh_ranges = database["id_fresh"]
    ingredients = database["ingredienti"]
    fresh_count = 0

    for ingredient_id in ingredients:
        is_fresh = False
        for start, end in fresh_ranges:
            if start <= ingredient_id <= end:
                is_fresh = True
                break
        
        if is_fresh:
            fresh_count += 1

    print(f"Fresh ingredients: {fresh_count}")


if __name__ == "__main__":
    main()
