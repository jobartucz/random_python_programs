def encode_rail_fence_cipher(string, n):

    if n == 1:
        return string

    encode = ''
    rails = []
    for i in range(n):
        rails.append([])

    count = 0
    counter = -1

    for i in range(len(string)):
        rails[count] += string[i]
        if (count == 0 or count == n - 1):
            counter *= -1
        count += counter

    for i in range(n):
        print(rails[i])
        encode += ''.join(rails[i])
        
    return encode

railss = 32
encoded = encode_rail_fence_cipher("Amet non facere minima iure unde, provident,     veritatis officiis asperiores ipsa eveniet sit! Deserunt     autem excepturi quibusdam iure unde! Porro alias distinctio     ipsam iure exercitationem molestiae. Voluptate fugiat quasi maiores!jk", railss)
print (encoded)

def decode_rail_fence_cipher(string, n):
    if n == 1 or n == len(string):
        return string

    decode = ''
    lengths = []
    for i in range(n):
        lengths.append(0)
    # calculate the lengths
    count = 0
    counter = -1
    for i in string:
        lengths[count] += 1
        if (count == 0 or count == n - 1):
            counter *= -1
        # print (count, lengths[count])
        count += counter
        
    start = 0
    rails = []
    for i in range(n):
        rails.append([])
        rails[i] = list(string[start:start+lengths[i]])
        # print(rails[i])
        start += lengths[i]
        
    count = 0
    counter = -1

    for i in range(len(string)):
        decode += rails[count].pop(0)
        if (count == 0 or count == n - 1):
            counter *= -1
        count += counter

    return decode
 
decoded = decode_rail_fence_cipher(encoded, railss)
print (decoded)
