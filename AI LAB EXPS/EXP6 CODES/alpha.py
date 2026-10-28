def alpha_beta(node, depth, alpha, beta, maximizing):
    if depth == 0:
        return node

    if maximizing:
        value = float('-inf')

        for child in node:
            value = max(value, alpha_beta(
                child, depth - 1, alpha, beta, False))
            alpha = max(alpha, value)

            if alpha >= beta:
                break

        return value

    else:
        value = float('inf')

        for child in node:
            value = min(value, alpha_beta(
                child, depth - 1, alpha, beta, True))
            beta = min(beta, value)

            if beta <= alpha:
                break

        return value


def create_tree(depth):
    if depth == 0:
        return int(input("Enter leaf value: "))

    n = int(input("Enter number of child nodes: "))
    return [create_tree(depth - 1) for _ in range(n)]


depth = int(input("Enter depth of tree: "))
tree = create_tree(depth)

result = alpha_beta(
    tree, depth, float('-inf'), float('inf'), True
)

print("Optimal Value:", result)