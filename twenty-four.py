#!/usr/bin/env python


def four_digits_permutations(digits):
    for i in range(4):
        for j in range(4):
            if j not in (i,):
                for k in range(4):
                    if k not in (i, j):
                        for l in range(4):
                            if l not in (i, j, k):
                                yield (digits[i], digits[j], digits[k], digits[l])


def three_operations_combinations():
    ops = '+-*/'
    for i in range(4):
        for j in range(4):
            for k in range(4):
                yield (ops[i], ops[j], ops[k])


while 1:
    digits = input("Enter four digits [0-9]: ")
    answers = set()

    # Loop through all permutations of 4 digits out of 4:
    for A, B, C, D in four_digits_permutations(digits):

        # Loop through all combinations of 3 operations out of 4:
        for o1, o2, o3 in three_operations_combinations():

            # There are only two possible BODMAS structures. Test both.
            for cmd in (
                    f"ans = ({A} {o1} {B}) {o2} ({C} {o3} {D})",
                    f"ans = (({A} {o1} {B}) {o2} {C}) {o3} {D}"
            ):
                try:
                    # Running exec will set the "ans" variable.
                    exec(cmd)
                except ZeroDivisionError as e:
                    pass
                else:
                    # noinspection PyUnresolvedReferences
                    if ans == 24:
                        if cmd not in answers:
                            answers.add(cmd)
                            print(cmd)

    print('Number of answers:', len(answers))
    print()
