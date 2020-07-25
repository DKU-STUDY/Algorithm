def solution(heights) :
    reception=[0]
    
    for i in range(1,len(heights)) :
        for j,v in enumerate(heights[i-1::-1]) :
            if heights[i]<v :
                reception.append(i-j)
                break
        if i==len(reception) :
            reception.append(0)
    return reception

#100점
