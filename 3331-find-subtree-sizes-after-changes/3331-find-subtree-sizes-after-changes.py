class Solution:
    def findSubtreeSizes(self, parent: List[int], s: str) -> List[int]:
        n = len(parent)

        # Build the original tree
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)

        # Store the closest ancestor with the same character
        new_parent = parent[:]
        last = {}

        def dfs(node):
            ch = s[node]

            # Find the nearest ancestor with the same character
            if ch in last:
                new_parent[node] = last[ch]

            # Update the nearest ancestor for this character
            prev = last.get(ch, -1)
            last[ch] = node

            for child in children[node]:
                dfs(child)

            # Restore the previous ancestor when backtracking
            if prev == -1:
                del last[ch]
            else:
                last[ch] = prev

        dfs(0)

        # Build the modified tree
        new_children = [[] for _ in range(n)]
        for i in range(1, n):
            new_children[new_parent[i]].append(i)

        # Calculate subtree sizes
        answer = [1] * n

        def calculate(node):
            for child in new_children[node]:
                calculate(child)
                answer[node] += answer[child]

        calculate(0)

        return answer