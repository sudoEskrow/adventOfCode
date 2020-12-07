input = open('./input').read().split('\n\n')

total_positives = 0
total_common_positives = 0
all_groups = []
for group in input:
    unique_positive_answers = []
    group_positive_answers = set(group.replace('\n', ''))
    for person in group:
        person = person.strip('\n')
        for answers in person:
            for answer in answers:
                if answer not in unique_positive_answers:
                    unique_positive_answers.append(answer)
    for answer in group_positive_answers:
        if group.count(answer) == len(group.split('\n')):
            total_common_positives += 1
    total_positives += len(unique_positive_answers)

print(total_positives)
print(total_common_positives)
