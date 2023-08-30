queries = [[2, 3], [1, 2], [2, 1], [2, 3], [2, 2]] # [type, index]

def answerQueries(queries, N):
  data = [False] * N
  output = []

  for i in range(len(queries)):
    # SET
    if queries[i][0] == 1:
      data[queries[i][1]-1] = True
      continue
    # GET
    output.append(-1)
    for j in range(queries[i][1]-1, len(queries)):
      if data[j]:
        output[-1] = j + 1
        break
  return(output)

print(answerQueries(queries, 5))