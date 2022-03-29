"""
    Week 5 In class Group Activity
    JAY PANCHAL - C0797202
    Abhishek Satyal - C0845420
    Pankaj Chaudhary - C0852469
    Vineet kumar - C0854440
"""

number_of_courses = 6

courses = []
for course_number in range(number_of_courses):
    course_name = input(f'Please enter your course no {course_number + 1} and press enter : ')
    courses.append(course_name)

scores = {}
for course_name in courses:
    score = int(input(f'Please enter your {course_name} score : '))
    scores[course_name] = score


def course_names(*courses_names):
    return courses_names


def get_average_score(**course_and_scores):
    total_score = sum(course_and_scores.values())
    average = total_score / len(course_and_scores.values())
    return average


def get_average_score_with_params(course1, course2, course3, course4, course5, course6):
    total_score = 0
    total_score += course1
    total_score += course2
    total_score += course3
    total_score += course4
    total_score += course5
    total_score += course6

    average = total_score / 6
    return average


def print_average_score_with_params(course1, course2, course3, course4, course5, course6):
    total_score = 0
    total_score += course1
    total_score += course2
    total_score += course3
    total_score += course4
    total_score += course5
    total_score += course6

    average = total_score / 6
    print(f'Average score with params: {average}')


def print_score_by_courses(**course_and_scores):
    for course, score in course_and_scores.items():
        print(f'Student scored {score} in {course} subject')


def print_average_score(**courses):
    total_score = 0
    for _score in courses.values():
        total_score += _score

    average = total_score / len(courses.values())
    print(f'Average score : {average}')


def print_sep():
    print("\n" * 3)
    print("-" * 30)

print_sep()
print(f'Name of courses student took this term : {course_names(*courses)}')
average_with_param = get_average_score_with_params(scores[courses[0]], scores[courses[1]], scores[courses[2]],
                                                   scores[courses[3]], scores[courses[4]], scores[courses[5]])
print_sep()
print(f'Average score with param {average_with_param}')
print_sep()
print_average_score_with_params(scores[courses[0]], scores[courses[1]], scores[courses[2]],
                                                   scores[courses[3]], scores[courses[4]], scores[courses[5]])
print_sep()
print(f'Average score for this term {get_average_score(**scores)}')

print_sep()
print_average_score(**scores)
print_sep()
print_score_by_courses(**scores)
