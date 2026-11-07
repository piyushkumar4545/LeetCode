class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(w, i) for i, w in enumerate(servers)]
        heapify(available)

        occupied = []
        time = 0
        ans = []

        def release() -> None:
            while occupied and occupied[0][0] <= time:
                _, i = heappop(occupied)
                heappush(available, (servers[i], i))

        for i, duration in enumerate(tasks):
            time = max(time, i)
            release()

            if not available:
                time = occupied[0][0]
                release()

            _, server = heappop(available)
            heappush(occupied, (time + duration, server))
            ans.append(server)

        return ans