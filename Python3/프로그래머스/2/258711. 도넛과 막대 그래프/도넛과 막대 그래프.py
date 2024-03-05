def solution(edges):
    # node의 특성으로 알 수 있음 (in / out 필요함)
    nodes = set()
    node_in = [0] * 1000001
    node_out = [0] * 1000001
    
    new_node = 0
    num_graphs = 0
    dough = 0
    bar = 0
    palja = 0
    
    for e in edges:
        o, i = e;
        nodes.add(o)
        nodes.add(i)
        
        node_in[i] += 1
        node_out[o] += 1
        
    for n in nodes:
        if (node_in[n] >= 2 and node_out[n] >= 2):
            palja += 1
        elif (node_out[n] == 0):
            bar += 1
        elif (node_in[n] == 0 and node_out[n] >= 2):
            new_node = n
            num_graphs = node_out[n]
        else:
            continue
        # 팔자 : in >=2 out >=2
        # 막대 : out == 0
        # new_node : in == 0, out >= 2
        # 도넛 : num_graphs - (팔자 + 막대)
        
    dough = num_graphs - (palja + bar)
    return [new_node, dough, bar, palja]