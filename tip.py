def calculate_tip(bill, tip_percent, people=1):
    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people
    return {"tip": tip, "total": total, "per_person": per_person}


def get_float(prompt):
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Bitte eine positive Zahl eingeben.")
                continue
            return value
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")


def get_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Bitte eine positive Ganzzahl eingeben.")
                continue
            return value
        except ValueError:
            print("Ungültige Eingabe. Bitte eine ganze Zahl eingeben.")


def main():
    print("=== Trinkgeldrechner ===")
    bill = get_float("Rechnungsbetrag (€): ")
    tip_percent = get_float("Trinkgeld (%): ")
    people = get_int("Anzahl Personen: ")

    result = calculate_tip(bill, tip_percent, people)

    print(f"\nTrinkgeld:      €{result['tip']:.2f}")
    print(f"Gesamt:         €{result['total']:.2f}")
    print(f"Pro Person:     €{result['per_person']:.2f}")


if __name__ == "__main__":
    main()
