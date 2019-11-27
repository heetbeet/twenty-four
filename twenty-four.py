#!/usr/bin/env python
import itertools

while 1:
    digits = input("Enter four digits [0-9]: ")
    answers = set()

    # Loop through all permutations of 4 digits out of 4:
    for A, B, C, D in itertools.permutations(digits):

        # Loop through all combinations of 3 operations out of 4:
        for x, y, z in itertools.product(*['+-*/']*3):

            # There are only two possible BODMAS structures. Test both.
            for cmd in (
                    f"({A} {x} {B}) {y} ({C} {z} {D})",
                    f"(({A} {x} {B}) {y} {C}) {z} {D}"
            ):
                try:
                    # Evaluate "cmd" as Python code.
                    ans = eval(cmd)
                except ZeroDivisionError as e:
                    pass
                else:
                    # noinspection PyUnresolvedReferences
                    if ans == 24:                        
                        answers.add(cmd)
                        print(cmd)

    print('Number of answers: ≤', len(answers))
    print()
