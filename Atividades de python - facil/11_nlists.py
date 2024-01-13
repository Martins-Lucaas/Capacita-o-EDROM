def main():
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

    unique_scores = sorted(set(score for _, score in records))
    second_lowest_students = []

    for person in records:
        if person[1] == unique_scores[1]:
            second_lowest_students.append(person[0])

    second_lowest_students = sorted(second_lowest_students)

    for student in second_lowest_students:
        print(student)

main()
