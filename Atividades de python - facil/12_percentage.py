def main():
    num_students = int(input())
    student_scores = {}

    for _ in range(num_students):
        student_info = input().split()
        name, scores = student_info[0], list(map(float, student_info[1:]))
        student_scores[name] = scores

    query_name = input()
    total_score = sum(student_scores[query_name])
    average_score = total_score / len(student_scores[query_name])

    print("{:.2f}".format(average_score))

main()
