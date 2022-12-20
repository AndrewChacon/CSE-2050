def solve_puzzle(puzzle): # Make sure to add input parameters here
    index = 0
    return _solve_puzzle(puzzle, index, None)

def _solve_puzzle(List, index, visited):
    if visited == None: visited = set()
    if index == len(List) - 1: return True 
    if index > len(List) - 1: index = index - len(List) 
    if index < 0 and index == -1: return True
    if index in visited: return False
    if index < 0 and index != -1: index = index + len(List) 
    visited.add(index)
    solutions_1 = _solve_puzzle(List,index - List[index],visited)
    solutions_2 = _solve_puzzle(List, index + List[index], visited)

    return solutions_1 or solutions_2
