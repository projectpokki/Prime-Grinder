maxInt = 200

seq, vals, primes = [-1], [], 0
for m in range(1, maxInt + 1):
  i = 0
  for n in range(len(seq) + 1):
    if n >= len(seq):
      if (len(seq) * 0.5) % 1 == 0:
        seq.append(seq[-1] - 1 - len(seq))
      else:
        seq.append(seq[-1] - 1 - len(seq) // 2)
      break
    if seq[n] + m < 0:
      break
    if n % 4 <= 1:
      if seq[n] + m == 0:
        i += m
      else:
        i += vals[seq[n] + m - 1]
    else:
      if seq[n] + m == 0:
        i -= m
      else:
        i -= vals[seq[n] + m - 1]
  vals.append(i)
  if i == m + 1:
    primes += 1
    print(m, end=" ")
print(f"\n\nthere are {str(primes)} primes between 0 and {str(maxInt)}")
