s = "azyxyyzaaandjefhdjfbejufkfbuwdgqygdwuirgwsjcxnskferpge"
q = ["d", "a", "x", "y", "f", "p"]

# hash array for 26 letters
hash_list = [0] * 26

# build frequency
for ch in s:
    index = ord(ch) - ord('a')
    hash_list[index] += 1

# answer queries
for ch in q:
    index = ord(ch) - ord('a')
    print(ch, "→", hash_list[index])
