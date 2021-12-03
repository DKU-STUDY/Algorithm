class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        # 시계 방향으로 start에서 destination까지
        clockwise_start = start
        clockwise_distance = 0
        while clockwise_start != destination:
            clockwise_distance += distance[clockwise_start]
            clockwise_start += 1
            clockwise_start = (clockwise_start % len(distance))
            print(clockwise_distance)

        # 반시계 방향으로 start에서 destination까지
        counterclockwise_start = start
        counterclockwise_distance = 0
        while counterclockwise_start != destination:
            counterclockwise_start -= 1
            counterclockwise_distance += distance[counterclockwise_start]
            counterclockwise_start = (counterclockwise_start % len(distance))
        return min(clockwise_distance, counterclockwise_distance)