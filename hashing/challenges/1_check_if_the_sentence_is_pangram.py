from util import assert_answer


def check_if_pangram(sentence: str) -> bool:
    """
    A pangram is a sentence where every letter of the
    English alphabet appears at least once. 

    Given a string sentence containing only lowercase
    English letters, return true if sentence is a pangram,
    or false otherwise.
    
    Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
    Output: true
    """

    num_letters = 26
    seen = set()

    for letter in sentence:
        seen.add(letter)

    return len(seen) == num_letters


if __name__ == '__main__':
    assert_answer(True, check_if_pangram("thequickbrownfoxjumpsoverthelazydog"))
