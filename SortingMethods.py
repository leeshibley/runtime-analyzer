#!/usr/bin/env python
# coding: utf-8

"""A class of self-implemented sorting algorithms, including:
    
    * Bubble Sort
    * Selection Sort
    * Insertion Sort
    * Merge Sort
    * Quick Sort
    
    It didn't have to be a class, but I wanted to try it out. :)
    
    """
class SortingMethod:
    
    def __init__(self, nums):
        self.nums = nums
        
    def bubblesort(self):
        """A sorting algorithm.
        
        Runtimes:
        * best case ------- O(n)
        * average case ---  O(n^2)
        * worst case ------ O(n^2)
        
        """
        swap_happened = True
        
        while swap_happened:
            swap_happened = False
            
            for i in range(len(self.nums) - 1):
                if self.nums[i] > self.nums[i + 1]:
                    self.nums[i + 1], self.nums[i] = self.nums[i], self.nums[i + 1]
                    swap_happened = True
                    
        return self.nums
    
    def selectionsort(self):
        """A sorting algorithm.
        
        Runtimes:
        * best case ------- O(n^2)
        * average case ---  O(n^2)
        * worst case ------ O(n^2)
        
        """
        spot_marker = 0
        
        while spot_marker < len(self.nums):
            for i in range(spot_marker, len(self.nums)):
                if self.nums[i] < self.nums[spot_marker]:
                    self.nums[spot_marker], self.nums[i] = self.nums[i], self.nums[spot_marker]
            spot_marker += 1
        
        return self.nums
    
    
    def insertionsort(self):
        """A sorting algorithm.
        
        Runtimes:
        * best case ------- O(n)
        * average case ---  O(n^2)
        * worst case ------ O(n^2)
        
        """
        for i in range(1, len(self.nums)):
            key = self.nums[i]
            working_index = i - 1
            
            while working_index >= 0 and key < self.nums[working_index]:
                self.nums[working_index + 1] = self.nums[working_index]
                working_index -= 1
            
            self.nums[working_index + 1] = key
        
        return self.nums
    
    
    def mergesorted(self, left, right):
        """A helper to the mergesort() function.
        
        Sorts values from two lists (left, right) via Merge Sort.
        """
        
        sorted_nums = []
        i, j = 0, 0
        
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                sorted_nums.append(left[i])
                i += 1
            else:
                sorted_nums.append(right[j])
                j += 1
                
        while i < len(left):
            sorted_nums.append(left[i])
            i += 1
        while j < len(right):
            sorted_nums.append(right[j])
            j += 1
            
        return sorted_nums
    
    def mergesort_split_list(self, nums):
        """A helper to the mergesort() function.
        
        Recursively splits the list of values into a left half and right half.
        
        """
        if len(nums) > 2:
            return nums[:]
        else:
            split_point = len(nums) // 2
            left = self.mergesort_split_list(nums[:split_point])
            right = self.mergesort_split_list(nums[split_point:])
            return self.mergesorted(left, right)
        
        
    def mergesort(self):
        """A sorting algorithm.
        
        Runtimes:
        * best case ------- O(nlog(n))
        * average case ---  O(nlog(n))
        * worst case ------ O(nlog(n))
        
        """
        return self.mergesort_split_list(self.nums)
    
    
    def quicksorted(self, nums):
        """A helper to the quicksort() function.
        
        Recursively sorts and combines the 'smaller than', 'equal to', and 'larger than' lists via Quick Sort.
        
        """
        if len(nums) < 2:
            return nums
        else:
            pivot = nums[-1]
            smaller, equal, larger = [], [], []
            
            for i in nums:
                if i < pivot:
                    smaller.append(i)
                elif i == pivot:
                    equal.append(i)
                else:
                    larger.append(i)
            return self.quicksorted(smaller) + equal + self.quicksorted(larger)


    def quicksort(self):
        """A sorting algorithm.
        
        Runtimes:
        * best case ------- O(nlog(n))
        * average case ---  O(nlog(n))
        * worst case ------ O(n^2) (very rare, often avoidable)
        
        """
        
        return self.quicksorted(self.nums)