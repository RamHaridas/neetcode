def groupAnagrams(strs):
    final_result = list()
    
    for item in strs:
        is_added = False
        if len(final_result) == 0:
            final_result.append([item])
            is_added = True
        else:
            for fr in final_result:
                if isAnagram(fr[0], item):
                    fr.append(item)
                    is_added = True
                    continue        
        if not is_added:
            final_result.append([item])
    return final_result
        

def isAnagram(str1, str2):
    if len(str1) != len(str2):
        return False
    str1map = dict()
    str2map = dict()

    for i in range(len(str1)):
        str1map[str1[i]] = str1map.get(str1[i],0) + 1
        str2map[str2[i]] = str2map.get(str2[i],0) + 1
    
    for key in str1map.keys():
        if str1map[key] != str2map.get(key,0):
            return False
    return True


strs = ["act","pots","tops","cat","stop","hat"]

res = groupAnagrams(strs)
print(res)