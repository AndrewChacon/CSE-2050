from ListMapping import ListMapping

class HashTable:
    def __init__(self):
        self._htsize = 5     
        self._buckets_array = [ListMapping() for i in range(self._htsize)] 
        self._n = 0        

    def put(self, key, value):
        bucket = self._get_bucket(key)
        if bucket is not None:
            bucket.put(key,value)
            self._n = self._n + 1
        if self._n > self._htsize: self._double()


    def get(self, key):
        bucket = self._get_bucket(key)
        if bucket is not None:
            return bucket.get(key)

    def _get_bucket(self, key):
        return self._buckets_array[hash(key) % self._htsize]

    def remove(self,key):
        e = self._buckets_array(key)
        e.remove(key)
        self._n = self._n - 1


    def _double(self):
        oldbuckets = self._buckets_array
        self._htsize = self._htsize * 2
        for bucket in oldbuckets:
            for key, value in bucket.items():
                bucket.put(key,value)



if __name__ == "__main__":
    HM = HashTable()

    HM.put(1, "one")
    HM.put(2, "two")
    HM.put(3, "three")
    HM.put(4, "four")
    HM.put(5, "five")
    HM.put(6, "six")
    HM.put("ten", 10)

    assert(HM.get(2) == "two")
    assert(HM.get(4) == "four")
    assert(HM.get("ten") == 10)
    assert(HM._htsize == 10)
    assert(HM._n == 7)
    print("PASSED")
