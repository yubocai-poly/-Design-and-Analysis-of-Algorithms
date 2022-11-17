# -*- coding: utf-8 -*-
import Sat as Sat
import LatinSquarePuzzle as latin

grading_mode = False


def error(msg):
    print(msg)
    assert not grading_mode, msg


grading_mode = False


def test_satisfied():
    sat = Sat.Sat(4, [[-1, 2, -4], [2, 3]])
    sat.values = [0, True, False, True, True]
    print("Assignment x1=True, x2=False, x3=True, x4=True")
    print("Testing on clause ¬x1 ∨ x2 ∨ ¬x4 ...", end="\t", flush=True)
    if sat.is_clause_satisfied([-1, 2, -4]) == None:
        return error("skipping is_clause_satisfied (unimplemented)")
    if not sat.is_clause_satisfied([-1, 2, -4]):
        print("Success!")
    else:
        error("Error, expects False")
    print("Testing on clause x2 ∨ x3 ...", end="\t", flush=True)
    if sat.is_clause_satisfied([2, 3]):
        print("Success!")
    else:
        error("Error, expects True")
    print("Testing on clause ¬x2 ...", end="\t", flush=True)
    if sat.is_clause_satisfied([-2]):
        print("Success!")
    else:
        error("Error, expects False")
    print("Test on conjunction of the two clauses:")
    if not sat.satisfied():
        print("Success!")
    else:
        error("Error, expects False")


def test_walk_sat():
    print("Testing walk_sat...", end="\n\t", flush=True)
    print("Testing on a formula with 8 variables and 24 clauses...",
          end="\t",
          flush=True)
    sat = Sat.Sat(8,
                  [[-1, -5], [-3, -7], [-2, -6], [-4, -8], [-1, -2], [-3, -4],
                   [-5, -6], [-7, -8], [-1, -3], [-5, -7], [-2, -4], [-6, -8],
                   [1, 2], [3, 4], [5, 6], [7, 8], [1, 5], [3, 7], [2, 6],
                   [4, 8], [1, 3], [5, 7], [2, 4], [6, 8]])
    N = 8 * 8**2
    sat.walk_sat(N)
    if sat.satisfied():
        print("Success!", end="\n\t")
    else:
        error("Error: does not satisfy all clauses", end="\n\t")
#  print("")

    print("Testing on a formula with 27 variables and 111 clauses...",
          end="\t",
          flush=True)
    sat = Sat.Sat(
        27,
        [[19], [17], [6], [-1, -10], [-1, -19], [-10, -19], [-4, -13],
         [-4, -22], [-13, -22], [-7, -16], [-7, -25], [-16, -25], [-2, -11],
         [-2, -20], [-11, -20], [-5, -14], [-5, -23], [-14, -23], [-8, -17],
         [-8, -26], [-17, -26], [-3, -12], [-3, -21], [-12, -21], [-6, -15],
         [-6, -24], [-15, -24], [-9, -18], [-9, -27], [-18, -27], [-1, -2],
         [-1, -3], [-2, -3], [-4, -5], [-4, -6], [-5, -6], [-7, -8], [-7, -9],
         [-8, -9], [-10, -11], [-10, -12], [-11, -12], [-13, -14], [-13, -15],
         [-14, -15], [-16, -17], [-16, -18], [-17, -18], [-19, -20],
         [-19, -21], [-20, -21], [-22, -23],
         [-22, -24], [-23, -24], [-25, -26], [-25, -27], [-26, -27], [-1, -4],
         [-1, -7], [-4, -7], [-10, -13], [-10, -16], [-13, -16], [-19, -22],
         [-19, -25], [-22, -25], [-2, -5], [-2, -8], [-5, -8], [-11, -14],
         [-11, -17], [-14, -17], [-20, -23], [-20, -26], [-23, -26], [-3, -6],
         [-3, -9], [-6, -9], [-12, -15], [-12, -18], [-15, -18], [-21, -24],
         [-21, -27], [-24, -27], [1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12],
         [13, 14, 15], [16, 17, 18], [19, 20, 21], [22, 23, 24], [25, 26, 27],
         [1, 10, 19], [4, 13, 22], [7, 16, 25], [2, 11, 20], [5, 14, 23],
         [8, 17, 26], [3, 12, 21], [6, 15, 24], [9, 18, 27], [1, 4, 7],
         [10, 13, 16], [19, 22, 25], [2, 5, 8], [11, 14, 17], [20, 23, 26],
         [3, 6, 9], [12, 15, 18], [21, 24, 27]])
    N = 4 * 27**2
    sat.walk_sat(N)
    if sat.satisfied():
        print("Success!")
    else:
        error("Error: does not satisfy all clauses")


l=latin.LatinSquarePuzzle(3,[['*',2,'*'],['*','*',1],[0,'*','*']])
l.build_generic_clauses()
l.add_fixed_value_clauses()
l.sat.clauses.sort()
print(l.sat.clauses)


def test_build_clauses():
    print("Testing build_generic_clauses...", end="\t", flush=True)
    l = latin.LatinSquarePuzzle(2, [['*', '*'], ['*', '*']])
    l.build_generic_clauses()
    m = l.sat.clauses
    if len(m) == 0:
        return error("skipping build_generic_clauses (unimplemented)")
    #print(m)
    for x in m:
        x.sort()
    m.sort()
    expected = [[-8, -7], [-8, -6], [-8, -4], [-7, -5], [-7, -3], [-6, -5],
                [-6, -2], [-5, -1], [-4, -3], [-4, -2], [-3, -1], [-2, -1],
                [1, 2], [1, 3], [1, 5], [2, 4], [2, 6], [3, 4], [3, 7], [4, 8],
                [5, 6], [5, 7], [6, 8], [7, 8]]
    if (m == expected):
        print("Success!")
    else:
        print("Error, expects")
        print(expected)
        print(len(expected))
        print("but list of clauses is")
        print(m)
        print(len(m))
        error("Error in test_build_clauses")


def test_1clauses():
    print("Testing add_fixed_value_clauses...", end="\t", flush=True)
    l = latin.LatinSquarePuzzle(4, [['*', 1, '*', 2], ['*', '*', 3, 1],
                                    [0, '*', '*', '*'], [1, '*', 2, '*']])
    l.add_fixed_value_clauses()
    m = l.sat.clauses
    if len(m) == 0:
        return error("skipping add_fixed_value_clauses (unimplemented)")
    m.sort()
    expected = [[6], [15], [28], [30], [33], [50], [59]]
    if (m == expected):
        print("Success!")
    else:
        print("Error, expects")
        print(expected)
        print("but list of clauses is")
        print(m)
        error("Error in test_1clauses")


def transpose(matrix):
    N = len(matrix)
    output = [['*' for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            output[i][j] = matrix[j][i]
    return output


def check_row(row):
    status = [False for _ in range(len(row))]
    for number in row:
        if status[number]:
            return False
        else:
            status[number] = True

    for number in status:
        if not number: return False

    return True


def check_rows(matrix):
    for row in matrix:
        if not check_row(row):
            return False
    return True


def is_Latin_square(l):
    if not check_rows(l.final):
        return False

    transposed = transpose(l.final)
    return check_rows(transposed)


def display_and_solve(l, prefix=""):
    l.display_before_solving(prefix)
    l.solve()
    if len(l.final) == 0:
        error(prefix + "skipping solve (unimplemented)")
        return False

    l.display_after_solving(prefix)
    if not is_Latin_square(l):
        error(prefix + "not a Latin square!")
        return False

    return True


def test_solve():
    print("Testing solve...", end="\n", flush=True)
    l = latin.LatinSquarePuzzle(
        3, [['*', 2, '*'], ['*', '*', 2], ['*', '*', '*']])
    if not display_and_solve(l, "\t"):
        return

    print("\t******************************************")

    k = 4
    l = latin.LatinSquarePuzzle(k,
                                [['*' for _ in range(k)] for __ in range(k)])
    if not display_and_solve(l, "\t"):
        return

    print("\t*****************************************")

    l = latin.LatinSquarePuzzle(4, [['*', 1, '*', 2], ['*', '*', 3, 1],
                                    [0, '*', '*', '*'], [1, '*', 2, '*']])
    if not display_and_solve(l, "\t"):
        return

    print("\t*****************************************")

    l = latin.LatinSquarePuzzle(4, [['*', 1, '*', '*'], ['*', '*', 3, '*'],
                                    [0, '*', '*', '*'], ['*', '*', 2, '*']])
    if not display_and_solve(l, "\t"):
        return

    print("\tSuccess!")


def test_propagate():
    print("Testing simplify_formula_by_propagation...", end="\t", flush=True)
    l = latin.LatinSquarePuzzle(4, [[3, 1, '*', 2], [2, '*', 3, '*'],
                                    [0, '*', '*', 3], [1, '*', '*', '*']])
    l.build_generic_clauses()
    l.add_fixed_value_clauses()
    l.sat.simplify_formula_by_propagation()
    if len(l.sat.fixed) == 0:
        return error(
            "skipping simplify_formula_by_propagation (unimplemented)")
    if (len(l.sat.fixed) < 64):
        error("Error: propagation should fix all variables")
    else:
        if (l.sat.satisfied):
            print("Success!")
        else:
            error(
                "Error: propagated all variables, but did not reach a solution"
            )


def test_solve_harder():
    print("Testing sudoku (medium)...", end="\n", flush=True)
    medium = [[2, '*', 5, '*', 4, '*', '*', 6, '*'],
              ['*', 3, '*', '*', 6, '*', '*', 2, '*'],
              [8, '*', 6, 1, '*', '*', '*', 4, '*'],
              ['*', '*', '*', '*', 5, '*', '*', 1, '*'],
              ['*', 1, '*', 3, 8, '*', 4, '*', '*'],
              [5, '*', '*', '*', '*', 6, '*', '*', 8],
              ['*', 6, '*', 5, '*', '*', 1, '*', 0],
              [0, '*', 8, '*', '*', '*', 3, '*', '*'],
              [1, '*', '*', '*', 3, '*', '*', '*', 2]]

    l = latin.LatinSquarePuzzle(9, medium)
    display_and_solve(l, "\t")


''' CALLS TO THE TEST FUNCTIONS '''

test_satisfied()
test_walk_sat()
test_build_clauses()
test_1clauses()
test_solve()
test_propagate()
test_solve_harder()
