def KSA(key):
	l = len(key)

	S = range(256)
	
	j = 0 # initial permutation
	for i in range(256):
		j = (j + S[i] + key[i % l]) % 256
		S[i], S[j] = S[j], S[i]

	return S


def SGA(S):
	i, j = 0, 0
	while True:
		i = (i + 1) % 256
		j = (j + S[i]) % 256
		S[i], S[j] = S[j], S[i]

		T = (S[i] + S[j]) % 256
		K = S[T]
		yield K


def RC4(key):
	return SGA(KSA(key))



if __name__ == "__main__":
	key1 = [0] * 256
	key2 = [15, 202, 33, 6, 8]
	res1, res2 = [], []

	keystream1 = RC4(key1)
	keystream2 = RC4(key2)

	for i in range(20):
		res1.append(keystream1.next())
		res2.append(keystream2.next())

	print(res1)
	print(res2)


# output:
# [222, 24, 137, 65, 163, 55, 93, 58, 138, 6, 30, 103, 87, 110, 146, 109, 199, 26, 127, 163]
# [248, 184, 102, 54, 212, 237, 186, 133, 51, 238, 108, 106, 103, 214, 39, 242, 30, 34, 144, 49]