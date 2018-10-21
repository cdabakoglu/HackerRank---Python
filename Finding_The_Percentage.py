if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
        avgScore = sum(scores) / len(scores)
        student_marks.update({name : avgScore})
    query_name = input()

    print("%.2f" % student_marks[query_name])
    
    
# Caner Dabakoğlu
# GitHub: https://github.com/cdabakoglu
