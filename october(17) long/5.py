##author="shubhambind"
from sys import stdin,stdout
def find_distance(parameters, vertex1, cycle1, vertex2, cycle2):
    # first handle cases where both vertex in same cycle
    if cycle1 == cycle2:
        return find_distance_within_cycle(parameters['edges'][cycle1-1], vertex1, vertex2)
    else:
        # we will calculate 2 paths: clock_path and anti_clock_path
        if cycle1 > cycle2:
            (cycle1, cycle2) = (cycle2, cycle1)
            (vertex1, vertex2) = (vertex2, vertex1)
 
        # clock_path
        clock_path_start = find_distance_within_cycle(parameters['edges'][cycle1-1],
                                                      parameters['cycle_links'][cycle1 - 1][1],
                                                      vertex1)
        clock_path_end = find_distance_within_cycle(parameters['edges'][cycle2-1],
                                                    parameters['cycle_links'][cycle2-1][0],
                                                    vertex2)
        clock_path_cycle = parameters['links'][cycle2-1] - parameters['links'][cycle1-1]
        clock_path_inner = parameter['link_inner'][cycle2-1] - parameter['link_inner'][cycle1]
        clock_path = clock_path_start + clock_path_cycle + clock_path_inner + clock_path_end
 
        # anti_clock_path: will be using previous results here
        anti_clock_path_start = find_distance_within_cycle(parameters['edges'][cycle1 - 1],
                                                           parameters['cycle_links'][cycle1 - 1][0],
                                                           vertex1)
        anti_clock_path_end = find_distance_within_cycle(parameters['edges'][cycle2 - 1],
                                                         parameters['cycle_links'][cycle2 - 1][1],
                                                         vertex2)
        anti_clock_path_cycle = parameters['links'][-1] - clock_path_cycle
        anti_clock_path_inner = parameter['link_inner'][-1] - \
                                parameter['link_inner'][cycle2] + \
                                parameter['link_inner'][cycle1-1]
        anti_clock_path = anti_clock_path_start + anti_clock_path_cycle + \
                          anti_clock_path_inner + anti_clock_path_end
 
        if clock_path < anti_clock_path:
            return clock_path
        return anti_clock_path
 
 
def find_distance_within_cycle(cycle, vertex1, vertex2):
    dist1 = abs(cycle[vertex2-1] - cycle[vertex1-1])
    dist2 = cycle[-1] - dist1
 
    if dist1 < dist2:
        return dist1
    return dist2
 
 
t = int(stdin.readline())
while t > 0:
    t -= 1
    n, q = map(int,stdin.readline().split())
 
    cnt = []
    edges = []
    links = [0]
    link_vertex = []
    link_inner = [0]
    cycle_links = []
 
    for i in range(n):
        inp = list(map(int, stdin.readline().split()))
        cnt.append(inp.pop(0))
        tmp = [0]
        for j in range(cnt[i]):
            tmp.append(tmp[j] + inp[j])
        edges.append(tmp)
 
    for i in range(n):
        link = list(map(int, stdin.readline().split()))
        links.append(links[i] + link.pop(2))
        link_vertex.append(link)
 
    # calculating inner paths distance
    start_node = link_vertex[-1][1]
    for i in range(n):
        end_node = link_vertex[i][0]
        dist = find_distance_within_cycle(edges[i], start_node, end_node)
        link_inner.append(link_inner[i] + dist)
        cycle_links.append([start_node, end_node])
        start_node = link_vertex[i][1]
 
    # prepare parameter for queries
    parameter = {'edges': edges,
                 'cycle_links': cycle_links,
                 'link_inner': link_inner,
                 'links': links}
 
    for _ in range(q):
        (v1, c1, v2, c2) = map(int, stdin.readline().split())
        print find_distance(parameter, v1, c1, v2, c2) 
