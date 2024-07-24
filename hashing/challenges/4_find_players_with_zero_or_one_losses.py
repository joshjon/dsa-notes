from util import assert_answer


def problem(matches: list[int]) -> list[int]:
    """
    You are given an integer array matches where matches[i] =
    [winneri, loseri] indicates that the player winneri defeated
    player loseri in a match.

    Return a list answer of size 2 where:

        - answer[0] is a list of all players that have not lost any
          matches.
        - answer[1] is a list of all players that have lost exactly
          one match.

    The values in the two lists should be returned in increasing
    order.
    
    Note:

        - You should only consider the players that have played at
          least one match.
        - The testcases will be generated such that no two matches
          will have the same outcome.
    """
    undefeated = set()
    loss_counts = {}
    
    for m in matches:
        winner = m[0]
        loser = m[1]
        
        if winner not in loss_counts:
            undefeated.add(winner)
        
        undefeated.discard(loser)
        
        if loser in loss_counts:
            loss_counts[loser] += 1
        else:
            loss_counts[loser] = 1
    
    result = [list(undefeated), []]
    
    for num, count in loss_counts.items():
        if count == 1:
            result[1].append(num)

    # sort for assertion
    result[0] = sorted(result[0])
    result[1] = sorted(result[1])

    return result



if __name__ == '__main__':
    data = [[1,3],[2,3],[3,6],[5,6],[5,7],[4,5],[4,8],[4,9],[10,4],[10,9]]
    want = [[1,2,10],[4,5,7,8]]
    
    assert_answer(want, problem(data), data)
    
    print()
    
    data = [[2,3],[1,3],[5,4],[6,4]]
    want = [[1,2,5,6],[]]
    assert_answer(want, problem(data), data)
    
