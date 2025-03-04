servers = [ 'host-{}'.format(x) for x in range(30) ] # host-0, host-1, host-2, ..., host-30
seeds = [servers[0]]

i = 0
while i < len(servers) and len(seeds) < len(servers):

    print('Step {}, copy from {} hosts:'.format(i, len(seeds)))

    j = 0
    while j < len(seeds) and len(seeds) + j < len(servers):

        src_host = seeds[j]
        dst_host = servers[len(seeds) + j]

        j += 1

        print('    Pair: {} -> {}'.format(src_host, dst_host)) # or run copy data in parallel

    seeds += servers[len(seeds):len(seeds)+j]

    i += 1

print('\nFinal result is {} steps'.format(i))
