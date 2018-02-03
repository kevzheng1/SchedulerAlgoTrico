from random import *

import itertools

def course_comb(course_lst):
    combs = []
    for i in range(1,len(course_lst)+1):
        combs.append(i)
        els = [list(x) for x in itertools.combinations(course_lst, i)]
        combs.append(els)
    return combs

def main():
    print(course_comb([1,2,3]))

main()
"""
def fac(n):
    # Calculate the combination
    result = 1
    for i in range(1,n+1):
        result = result * i
    return result

def check_distinct(lst_a, lst_b):

def combination(num_obj, num_choose):
    # num_obj is a list of all different items
    # num_choose tells how many items you choose from the list
    comb_lst = []
    added_lst = []
    expected_comb = (fac(num_obj)/fac_num(num_choose))/fac(num_obj-num_choose)
    while comb_lst != expected_comb:
        for i in range(len(comb_lst)):
            if added_lst == comb_lst[i]:
                break
        comb_lst.append(added_lst)
"""
