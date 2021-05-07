class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered_list = [restaurant for restaurant in restaurants 
                         if (veganFriendly == 0 or
                         restaurant[2] == veganFriendly) and 
                         restaurant[3]<=maxPrice and 
                         restaurant[4]<=maxDistance]
        
        print(filtered_list)
        filtered_list.sort(reverse=True, key=itemgetter(1,0))
        
        res = list(zip(*filtered_list))
        
        if res:
            return res[0]
        return res