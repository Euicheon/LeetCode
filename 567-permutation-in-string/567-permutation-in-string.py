from itertools import permutations
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1) > len(s2)):
            return False
        elif (len(s1) == len(s2)):
            counts = collections.Counter(s1)
            count_window = collections.Counter(s2)
            # print(counts,count_window)
            
            a = counts.subtract(count_window)
            # print(counts)
            c = 0
            for val in counts.values():
                c += 1
                if val != 0:
                    break
                elif c == len(counts):
                    return True
            return False
        else:
            counts = collections.Counter(s1)
            count_window = collections.Counter(s2[:len(s1)])

            for i in range(len(s2)-len(s1)+1):
                # print(s2[i:i+len(s1)])
                counts_real = collections.Counter(s1)
                # print(counts_real)
                a = counts_real.subtract(count_window)
                # print(counts_real)
                c = 0
                for val in counts_real.values():
                    c += 1
                    if val != 0:
                        # print("BREAK!")
                        break
                    elif c == len(counts_real):
                        return True
                # print(counts_real.values(),len(counts_real))
                try:
                    count_window[s2[i]] -= 1
                    count_window[s2[i+len(s1)]] += 1
                except:
                    break
            counts_real = collections.Counter(s1)
            # print(counts_real)
            a = counts_real.subtract(count_window)
            # print(counts_real)   
            return False