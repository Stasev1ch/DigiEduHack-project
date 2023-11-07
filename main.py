grades = {
    "Matemātika": [9, 7, 6, 4, 10],
    "Fizika": [7, 7, 6, 8, 5],
    "Angļu valoda": [5, 4, 8, 10, 4],
    "Vācu valoda": [8, 8, 6, 7, 7],
    "Ķīmija": [9, 9, 4, 8, 6],
    "Sports": [10, 10, 9, 8, 8],
    "Latviešu valoda": [7, 7, 8, 7, 9]
}

average_grades = {subject: sum(grades_list) / len(grades_list) for subject, grades_list in grades.items()}

overall_average = sum(average_grades.values()) / len(average_grades)

scholarship_brackets = {
    (9, 10): 50,
    (7, 8): 30,
    (4, 6): 10,
    (0, 3): 0
}

def determine_scholarship(avg):
    for (lower_bound, upper_bound), amount in scholarship_brackets.items():
        if lower_bound <= avg <= upper_bound:
            return amount
    return 0

initial_scholarship = determine_scholarship(overall_average)

missed_days_deductions = {
    14: 0.5,
    9: 0.3,
    4: 0.15,
    0: 0
}

def apply_deduction(scholarship, missed_days):
    for days, deduction in missed_days_deductions.items():
        if missed_days >= days:
            return scholarship * (1 - deduction)
    return scholarship

missed_days = int(input("Lūdzu, ievadiet nokavēto stundu skaitu: "))

final_scholarship = apply_deduction(initial_scholarship, missed_days)

print("Stipendiju kategorijas: ", scholarship_brackets)
print("Studentu atzīmes: ", grades)
print("Studentu vidējās atzīmes semestrī: ", average_grades)
print("Kopējais vidējais vērtējums: {:.2f}".format(overall_average))
print("Sākotnējā piešķirtā stipendija: €{}".format(initial_scholarship))
print("Galīgā saņemtā stipendija pēc atskaitījumiem par {} nokavētām dienām: €{:.2f}".format(missed_days, final_scholarship))