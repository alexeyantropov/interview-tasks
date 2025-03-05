# Deploy a big file among many servers as fast as possible. Bottleneck is network bandwidth.

servers = [ 'host-{}'.format(x) for x in range(30) ] # host-0, host-1, host-2, ..., host-30

last_seed = 0 # a pointer to the first server with the file
step = 0 # just a counter of steps for pretty results prining 

while last_seed < len(servers) - 1: # the last pointer value is len(servers)-1

    print('Step no\t{}'.format(step))

    i = 0

    while i <= last_seed and last_seed + 1 + i < len(servers): # works while it can make pairs between seeds and destinations

      src = servers[i]
      dst = servers[last_seed + 1 + i]

      i += 1

      print('\t# scp -A u@{}:/path/file u@{}:/path/file &'.format(src, dst))

    last_seed += i
    step += 1

print('\nResult:\n\t{} step(s) with parallel copying for {} host(s)'.format(step - 1, len(servers))) 
