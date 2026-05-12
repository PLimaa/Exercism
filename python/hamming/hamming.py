def distance(strand_a, strand_b):
    distance = 0
    if len(strand_a) == len(strand_b):
        for i in range(len(strand_a)):
            if strand_a[i] != strand_b[i]:
                distance += 1
        return distance
    else: raise ValueError("Strands must be of equal length.")


