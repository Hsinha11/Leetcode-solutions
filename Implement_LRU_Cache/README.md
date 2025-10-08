# Implement LRU Cache

## 🧠 Problem Statement
Design a data structure that supports:
- get(key)
- put(key, value)
Both operations in **O(1)** time using **Least Recently Used (LRU)** strategy.

## 🪄 Approach
Use:
- **HashMap** to store key-node mapping.
- **Doubly Linked List** to track usage order.

## 🧩 Test Cases
- Input: put(1,1), put(2,2), get(1), put(3,3), get(2)  
  Output: 1, -1  

## ⚙️ Edge Cases
- Repeated keys
- Cache size = 1

## 🎯 Expected Outcome
Efficient O(1) operations for get/put.

## 💻 C++ Solution
```cpp
#include <bits/stdc++.h>
using namespace std;

class LRUCache {
    int cap;
    list<pair<int,int>> dq;
    unordered_map<int, list<pair<int,int>>::iterator> mp;
public:
    LRUCache(int capacity) { cap = capacity; }

    int get(int key) {
        if (mp.find(key) == mp.end()) return -1;
        auto it = mp[key];
        int val = it->second;
        dq.erase(it);
        dq.push_front({key, val});
        mp[key] = dq.begin();
        return val;
    }

    void put(int key, int value) {
        if (mp.find(key) != mp.end()) dq.erase(mp[key]);
        else if (dq.size() == cap) {
            mp.erase(dq.back().first);
            dq.pop_back();
        }
        dq.push_front({key, value});
        mp[key] = dq.begin();
    }
};

int main() {
    LRUCache cache(2);
    cache.put(1,1);
    cache.put(2,2);
    cout << cache.get(1) << endl;
    cache.put(3,3);
    cout << cache.get(2) << endl;
}
```

## ☕ Java Solution
```java
import java.util.*;

class LRUCache {
    private final int cap;
    private final LinkedHashMap<Integer, Integer> map;

    public LRUCache(int capacity) {
        this.cap = capacity;
        this.map = new LinkedHashMap<>(capacity, 0.75f, true);
    }

    public int get(int key) {
        return map.getOrDefault(key, -1);
    }

    public void put(int key, int value) {
        if (map.size() >= cap && !map.containsKey(key)) {
            int firstKey = map.keySet().iterator().next();
            map.remove(firstKey);
        }
        map.put(key, value);
    }

    public static void main(String[] args) {
        LRUCache cache = new LRUCache(2);
        cache.put(1,1);
        cache.put(2,2);
        System.out.println(cache.get(1));
        cache.put(3,3);
        System.out.println(cache.get(2));
    }
}
```
