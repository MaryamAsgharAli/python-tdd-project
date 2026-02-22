from cipher import pattern_cipher


def test_none_returns_none():
    assert pattern_cipher(None) is None            #Equalance class 1

def test_empty_string_returns_empty():
    assert pattern_cipher("") == ""              #boundary case

def test_numbers_unchanged():
    assert pattern_cipher("123") == "123"              #2

def test_special_characters_unchanged():
    assert pattern_cipher("!@#") == "!@#"

def test_palindrome_unchanged():
    assert pattern_cipher("level") == "level"

def test_palindrome_case_insensitive_unchanged():
    assert pattern_cipher("Noon") == "Noon"

def test_repeated_letters_reversed():
    assert pattern_cipher("hello") == "olleh"

def test_unique_letters_rotated_left():
    assert pattern_cipher("cat") == "atc"

def test_conflict_palindrome_wins_over_repeated():
    assert pattern_cipher("noon") == "noon"

def test_single_letter_unchanged():
    assert pattern_cipher("a") == "a"

def test_two_letter_unique_rotates():
    assert pattern_cipher("ab") == "ba"

def test_two_letter_same_is_palindrome_unchanged():
    assert pattern_cipher("aa") == "aa"

def test_mixed_alnum_unchanged():
    assert pattern_cipher("abc123") == "abc123"

def test_unique_letters_preserve_casing():
    assert pattern_cipher("Python") == "ythonP"