def lengthOfLongestSubstring(s: str) -> int:
    i = 0

    while i <= (len(str)-1):
        h = i+1
        found = False
        count = 1
        subs = []

        while not found:
            subs.append(s[h])
            hit = False
            j = 0
            
            while (j <= len(subs)-1) and (not hit):
                if subs[j] == s[h]:
                    found = True
                    hit = True

            c += 1

        i += 1

    