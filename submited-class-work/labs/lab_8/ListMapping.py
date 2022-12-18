class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str(self.key) + " : " + str(self.value)

class ListMapping:
    def __init__(self):
        self._entries = []

    def put(self, key, value):
        e = self._entry(key)
        if e is not None:
            e.value = value
        else:
            self._entries.append(Entry(key, value))


    def get(self, key):
        e = self._entry(key)
        if e is not None:
            return e.value
        else:
            raise KeyError


    def remove(self, key):
        e = self._entry(key)
        if e is not None:
            self._entries.remove(e)
        else:
            return None


    def _entry(self, key):
        for e in self._entries:
            if e.key == key:
                return e
        return None



    def __len__(self):
        return len(self._entries)

    def __contains__(self, key):
        if self._entry(key) is None:
            return False
        else:
            return True

    def items(self):
        return ((e.key, e.value) for e in self._entries)


if __name__ == "__main__":
    map = ListMapping()
    map.put(1, "one")
    map.put(2, "two")
    map.put(3, "three")
    map.put(4, "four")
    print(map.get(1))
    print(map.get(3))
    print(map.get(4))
