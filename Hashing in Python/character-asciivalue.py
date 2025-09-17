s = "azyxyyzaaandjefhdjfbejufkfbuwdgqygdwuirgwsjcxnskferpge"
q = ["d", "a", "x", "y", "f", "p"]

# make hash list for ASCII codes up to 'z'
hash_list = [0] * 123   # index 0..122, we only use 97–122

# build frequency
for ch in s:
    ascii_val = ord(ch)      # ASCII code of character
    hash_list[ascii_val] += 1

# answer queries
for ch in q:
    ascii_val = ord(ch)
    print(ch, "→", hash_list[ascii_val])
