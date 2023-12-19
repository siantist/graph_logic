# existence of twins
def exist_twins(A):
  n = len(A)
  twins= []
  for i in range(n): # u
    for j in range(n): # v
      u = np.array(A[i])
      v = np.array(A[j])
      # nbrs of u , v
      unbr = np.where(u == 1)
      vnbr = np.where(v ==1)
      if unbr == vnbr and i != j:
        # save
        twins.append((i,j))

    return twins
