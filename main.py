import unittest
import pytest


def palindrome(s):
  if (len(s) <= 1):
    return True
  if (len(s) > 1):
    if(s[0] == s[-1]):
      return palindrome(s[1:-1])
    else:
      return False

assert palindrome("Hello") == False
assert palindrome("") == True
assert palindrome("saippuakivikauppias") == True

def test_palindrome():
  assert palindrome("Hello") == False
  assert palindrome("") == True
  assert palindrome("saippuakivikauppias") == True

def wordcount(s):
  return len(s.split())

assert wordcount("") == 0
assert wordcount("word") == 1
assert wordcount("’Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe. ") == 23

def test_wordcount():
  assert wordcount("") == 0
  assert wordcount("word") == 1
  assert wordcount("’Twas brillig, and the slithy toves Did gyre and gimble in the wabe: All mimsy were the borogoves, And the mome raths outgrabe. ") == 23  