#!/bin/env python

import json
import os
import sys
import time
import urllib

SECOND = 1
MINUTE = 60
HOUR = 3600
DAY = 86400

current_time = lambda: int(time.time())

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.age = current_time()
        self.next = None
        self.prev = None
        self.size = sys.getsizeof(val)
    
    def details(self, include_value=False):
        d = {
            'key': self.key,
            'bust': urllib.urlencode({'key': self.key}),
            'age': current_time() - self.age
        }
        if include_value:
            d['val'] = self.val
        return d

class Cache(object):
    def __init__(self, max_items=100, max_age=-1, max_size=-1, **kwargs):
        self.max_items = max_items
        self.max_age = max_age
        self.max_size = max_size
        self.size = 0
        self.clear()

    def clear(self):
        self.cache = {}
        self.head = None
        self.tail = None
        
    def contains(self, key):
        return self.cache.has_key(key)
    
    def details(self, include_values=False):
        keys = []
        current = self.head
        while current:
            keys.append(current.details(include_values))
            current = current.next

        return json.dumps({
            'count': len(self.cache),
            'size': self.size,
            'max_size': self.max_size,
            'max_items': self.max_items,
            'max_age': self.max_age,
            'keys': keys
        })

    def get(self, key):
        obj = self.cache.get(key)
        if obj:
            if self.max_age < 0 or obj.age + self.max_age >= current_time():
                self.put(key, obj.val)
                return obj.val
            self.remove(key)
        return None

    def put(self, key, val):
        if self.contains(key):
            self.remove(key)
        obj = Node(key, val)
        self.size += obj.size
        self.cache[key] = obj

        if self.head:
            obj.next = self.head
            self.head.prev = obj
        self.head = obj

        if not self.tail:
            self.tail = obj

        # check max items constraint
        if self.max_items > 0 and len(self.cache) > self.max_items:
            self.remove(self.tail.key)

        # check max_size constraint
        while self.max_size > 0 and self.size > self.max_size:
            self.remove(self.tail.key)

    def remove(self, key):
        if self.contains(key):
            obj = self.cache[key]
            if obj.prev:
                obj.prev.next = obj.next
            else:
                self.head = obj.next
            if obj.next:
                obj.next.prev = obj.prev
            else:
                self.tail = obj.prev
            self.size -= obj.size
            del self.cache[key]
            

   
