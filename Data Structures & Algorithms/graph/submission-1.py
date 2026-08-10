class Graph:
    
    def __init__(self):
        self.adj_list = {}

    def addEdge(self, src: int, dst: int) -> None:
        if src not in self.adj_list:
            self.adj_list[src] = set()
        if dst not in self.adj_list:
            self.adj_list[dst] = set()
        
        self.adj_list[src].add(dst)

    def removeEdge(self, src: int, dst: int) -> bool:
        if src not in self.adj_list or dst not in self.adj_list[src]:
            return False
        
        self.adj_list[src].remove(dst)
        return True

    def hasPath(self, src: int, dst: int) -> bool:
        return self.hasPathBFS(src, dst)

    def _dfs(self, src: int, dst: int, visit: set) -> bool:
        if src == dst:
            return True
        
        visit.add(src)
        for neighbor in self.adj_list.get(src, []):
            if neighbor not in visit:
                if self._dfs(neighbor, dst, visit):
                    return True

        visit.remove(src)
        return False

    def hasPathBFS(self, src: int, dst: int) -> bool:
        visit = set()
        queue = deque([src])
        
        while queue:
            curr  = queue.popleft()
            if curr == dst:
                return True
            visit.add(curr)
            for neighbor in self.adj_list.get(curr, []):
                if neighbor not in visit:
                    queue.append(neighbor)
                    visit.add(neighbor)

        return False