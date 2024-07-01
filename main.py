from collections import OrderedDict

class SIEVECache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.hand = None
        self.visited = {}

    def get(self, key):
        if key not in self.cache:
            return None
        self.visited[key] = True
        return self.cache[key]

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
            self.cache[key] = value
            self.visited[key] = True
        else:
            if len(self.cache) >= self.capacity:
                self.evict()
            self.cache[key] = value
            self.visited[key] = False
            if self.hand is None:
                self.hand = key

    def evict(self):
        while True:
            if self.visited[self.hand]:
                self.visited[self.hand] = False
                self.hand = next(iter(self.cache))
            else:
                del self.cache[self.hand]
                del self.visited[self.hand]
                self.hand = next(iter(self.cache), None)
                break

    def __str__(self):
        return f"Cache: {list(self.cache.keys())}\nHand: {self.hand}\nVisited: {self.visited}"

# Example usage
if __name__ == "__main__":
    cache = SIEVECache(3)
    
    cache.put(1, "one")
    cache.put(2, "two")
    cache.put(3, "three")
    print(cache)

    cache.get(2)
    print(cache)

    cache.put(4, "four")
    print(cache)

    cache.put(5, "five")
    print(cache)