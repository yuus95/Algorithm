def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length
    cur_weight= 0

    while truck_weights:
        answer+=1
        cur_weight -= bridge_on.pop(0)

        if cur_weight+ truck_weights[0] > weight:
            bridge_on.append(0)

        else :
            truck = truck_weights.pop(0)
            bridge_on.append(truck)
            cur_weight+= truck

    while 0 < cur_weight:
        answer+=1
        cur_weight-= bridge_on.pop(0)


    return answer


