def solution(S):
    n = len(S)
    patches = 0
    i = 0

    while i < n:
        if S[i] == 'X':

        # We encounter a pothole, so we need to apply a patch
         patches += 1
        # Skip the next two segments after applying the patch
        i += 3
    else:
        # Move to the next segment
        i += 1
        
    return patches
# Examples
print(solution(".X..X"))          # Output: 2
print(solution("X.XXXXX.X."))     # Output: 3
print(solution("XX.XXX.."))       # Output: 2
print(solution("XXXX"))           # Output: 2