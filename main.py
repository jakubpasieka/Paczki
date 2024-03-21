def get_valid_packages_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Wprowadzono niedozwolony znak/wartość, spróbuj jeszcze raz.")
            else:
                return value
        except ValueError:
            print("Wprowadzono niedozwolony znak/wartość, spróbuj jeszcze raz.")

def get_valid_weight_input(prompt):
    while True:
        try:
            weight = int(input(prompt))
            if weight < 1 or weight > 10:
                print("Podano nieprawidłową wagę. Koniec dodawania paczek, dotychczasowe produkty zostaną wysłane.")
                return None
            else:
                return weight
        except ValueError:
            print("Wprowadzono niedozwolony znak, spróbuj jeszcze raz.")

def main():
    num_packages = get_valid_packages_input("Ile produktów chcesz wysłać? ")
    packages = []
    current_package = []

    for i in range(num_packages):
        weight = get_valid_weight_input(f"Podaj wagę produktu {i + 1} [1-10 kg]: ")

        if weight is None:
            break

        if sum(current_package) + weight > 20:
            packages.append(current_package[:])
            current_package.clear()

        current_package.append(weight)

    if current_package:
        packages.append(current_package)

    total_packages = len(packages)
    total_weight = sum(sum(package) for package in packages)
    unused_weight = total_packages * 20 - total_weight

    def calculate_unused_weight(package):
        return 20 - sum(package)

    max_unused_package = max(packages, key=calculate_unused_weight)
    max_unused_weight = calculate_unused_weight(max_unused_package)

    print("\nPodsumowanie")
    print(f"Liczba wysłanych paczek: {total_packages}")
    print(f"Suma wysłanych łącznie kilogramów: {total_weight}kg")
    print(f"Suma niewykorzystanych łącznie kilogramów: {unused_weight}kg")
    print(f"Najwięcej niewykorzystanych kilogramów ma paczka {packages.index(max_unused_package) + 1} "
          f"({max_unused_weight}kg)")

if __name__ == "__main__":
    main()
