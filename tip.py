def calculate_tip(bill, tip_percent, people=1):
    tip = bill * (tip_percent / 100)
    total = bill + tip
    per_person = total / people
    return {"tip": tip, "total": total, "per_person": per_person}


def main():
    print("=== Trinkgeldrechner ===")
    bill = float(input("Rechnungsbetrag (€): "))
    tip_percent = float(input("Trinkgeld (%): "))
    people = int(input("Anzahl Personen: "))

    result = calculate_tip(bill, tip_percent, people)

    print(f"\nTrinkgeld:      €{result['tip']:.2f}")
    print(f"Gesamt:         €{result['total']:.2f}")
    print(f"Pro Person:     €{result['per_person']:.2f}")


if __name__ == "__main__":
    main()
