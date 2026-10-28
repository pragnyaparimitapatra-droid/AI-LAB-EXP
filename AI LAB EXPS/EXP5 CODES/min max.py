def minmax(depth, nodeIndex, is_max, scores, height):
    if depth == height:
        return scores[nodeIndex]
    if is_max:
        return max(
            minmax(depth + 1, nodeIndex * 2, False, scores, height),
            minmax(depth + 1, nodeIndex * 2 + 1, False, scores, height),
        )
    else:
        return min(
            minmax(depth + 1, nodeIndex * 2, True, scores, height),
            minmax(depth + 1, nodeIndex * 2 + 1, True, scores, height),
        )


scores = list(map(int, input("Enter the leaf node values separated by spaces: ").split()))
height = 3
result = minmax(0, 0, True, scores, height)
print("The optimal value is:", result)