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

    return False



if __name__ == '__main__':
    assert_answer(False, check_if_pangram("leetcode"))
