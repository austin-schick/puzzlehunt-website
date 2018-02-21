#################################################
# Colab1
#################################################

import cs112_s18_week1_linter
import math

#################################################
# Helper functions
#################################################

def almostEqual(d1, d2, epsilon=10**-7):
    # note: use math.isclose() outside 15-112 with Python version 3.5 or later
    return (abs(d2 - d1) < epsilon)

import decimal
def roundHalfUp(d):
    # Round to nearest with ties going away from zero.
    rounding = decimal.ROUND_HALF_UP
    # See other rounding options here:
    # https://docs.python.org/3/library/decimal.html#rounding-modes
    return int(decimal.Decimal(d).to_integral_value(rounding=rounding))

#################################################
# Colab1 problems
#################################################

def isPerfectSquare(n):
    return

def perfectSquareHandler():
    return

def nearestOdd(n):
    return

def rectanglesOverlap(x1, y1, w1, h1, x2, y2, w2, h2):
    return

def getKthDigit(n, k):
    return

def setKthDigit(n, k, d=0):
    return

#################################################
# Colab1 Test Functions
################################################

def testIsPerfectSquare():
    print('Testing isPerfectSquare()... ', end='')
    assert(isPerfectSquare(0) == True)
    assert(isPerfectSquare(1) == True)
    assert(isPerfectSquare(16) == True)
    assert(isPerfectSquare(1234**2) == True)
    assert(isPerfectSquare(15) == False)
    assert(isPerfectSquare(17) == False)
    assert(isPerfectSquare(-16) == False)
    assert(isPerfectSquare(1234**2+1) == False)
    assert(isPerfectSquare(1234**2-1) == False)
    assert(isPerfectSquare(4.0000001) == False)
    assert(isPerfectSquare('Do not crash here!') == False)
    print('Passed.')

def ioTest(test):
    import sys, io
    myOut = io.StringIO()
    myIn = io.StringIO(test)
    sys.stdout = myOut
    sys.stdin = myIn
    perfectSquareHandler()
    return myOut.getvalue()

def testPerfectSquareHandler():
    import sys
    print('Testing perfectSquareHandler()... ', end='')
    tmpOut = sys.stdout
    tmpIn = sys.stdin
    fourTest = ioTest("4\n")
    sevenTest = ioTest("7\n")
    sys.stdout = tmpOut
    sys.stdin = tmpIn
    # Note: when you test this yourself, you should see:
    # Enter a number:4
    # The number 4 is a perfect square
    # in the interpreter.
    assert(fourTest == "Enter a number:The number 4 is a perfect square\n")
    assert(sevenTest == "Enter a number:The number 7 is not a perfect square\n")
    print('Passed!')

def testNearestOdd():
    print('Testing nearestOdd()... ', end='')
    assert(nearestOdd(13) == 13)
    assert(nearestOdd(12.001) == 13)
    assert(nearestOdd(12) == 11)
    assert(nearestOdd(11.999) == 11)
    assert(nearestOdd(-13) == -13)
    assert(nearestOdd(-12.001) == -13)
    assert(nearestOdd(-12) == -13)
    assert(nearestOdd(-11.999) == -11)
    print('Passed.')

def testRectanglesOverlap():
    print('Testing rectanglesOverlap()...', end='')
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, -2, -2, 6, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3, 3, 1, 1) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3.1, 3, 1, 1) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 1.9) == False)
    assert(rectanglesOverlap(1, 1, 1, 1, 1.9, -1, 0.2, 2) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 2, 2, 2, 6) == True)
    assert(rectanglesOverlap(1, 1, 2, 2, 3,4,5,6) == False)
    print('Passed.')

def testGetKthDigit():
    print('Testing getKthDigit()... ', end='')
    assert(getKthDigit(809, 0) == 9)
    assert(getKthDigit(809, 1) == 0)
    assert(getKthDigit(809, 2) == 8)
    assert(getKthDigit(809, 3) == 0)
    assert(getKthDigit(0, 100) == 0)
    assert(getKthDigit(-809, 0) == 9)
    print('Passed.')

def testSetKthDigit():
    print('Testing setKthDigit()... ', end='')
    assert(setKthDigit(809, 0, 7) == 807)
    assert(setKthDigit(809, 1, 7) == 879)
    assert(setKthDigit(809, 2, 7) == 709)
    assert(setKthDigit(809, 3, 7) == 7809)
    assert(setKthDigit(0, 4, 7) == 70000)
    assert(setKthDigit(-809, 0, 7) == -807)
    assert(setKthDigit(809, 0) == 800)
    print('Passed.')

#################################################
# Colab1 Main
################################################

def testAll():
    testIsPerfectSquare()
    testPerfectSquareHandler()
    testNearestOdd()
    testRectanglesOverlap()
    testGetKthDigit()
    testSetKthDigit()

def main():
    cs112_s18_week1_linter.lint() # check style rules
    testAll()

if __name__ == '__main__':
    main()
