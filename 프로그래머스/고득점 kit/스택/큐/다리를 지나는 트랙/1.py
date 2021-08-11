#실패 다시풀기

def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge_on = [0] * bridge_length
    curr_weight = 0

    while truck_weights:
        answer+=1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

        if curr_weight + truck_weights[0] > weight:
            bridge_on.append(0)
        else :
            truck = truck_weights.pop(0)
            bridge_on.append(truck)
            curr_weight += truck

    while curr_weight > 0 :
        answer+=1
        bridge_out = bridge_on.pop(0)
        curr_weight -= bridge_out

    return answer


bridge_length=[2,100,100]
weight=[10,100,100]
truck_weights=[[7,4,5,6],[10],[10,10,10,10,10,10,10,10,10,10]]