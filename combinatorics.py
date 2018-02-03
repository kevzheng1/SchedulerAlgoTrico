import random
import itertools

def course_comb(course_lst):
    combs = []
    for i in range(1,len(course_lst)+1):
        els = [list(x) for x in itertools.combinations(course_lst, i)]
        for j in els:
            for k in j:
                print(str(k))
        print("-----------------------------------------------------------")
        combs.append(els)
    return combs

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n-1)

def expected_combination(num_course, num_obj):
    return int(fac(num_course)/(fac(num_obj)*fac(num_course-num_obj)))
