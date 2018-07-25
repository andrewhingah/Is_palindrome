import unittest
import palindrome

class TestPalindrome(unittest.TestCase):
	def test_palindrome_with_normal_string (self):
		assert palindrome.check_if_Palindrome('level') is True
	def test_palindrome_mixed_case (self):
		assert palindrome.check_if_Palindrome('Bob') is True
	def test_palindrome_with__white_spaces(self):
		assert palindrome.check_if_Palindrome('bush saw sununu swash sub.') is True
	def test_palindrome_with_panctuations(self):
		assert palindrome.check_if_Palindrome('racecar?') is True
	def test_non_palindrome_string_is_false(self):
		assert palindrome.check_if_Palindrome('xyzz') is False

	# def test_user_input_record_is_kept(self):
	# 	self.assertIn(palindrome.user_input,palindrome.user_entry)


if __name__ == '__main__':
	unittest.main()