def hackerrankInString(s):
    ans = 'YES'
    for item in 'hackerrank':
        count = s.count(item)
        if count < 1:
            ans = 'NO'
            break
        index = s.find(item)
        s = s[index+1:]
    return ans