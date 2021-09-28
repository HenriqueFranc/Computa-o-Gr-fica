  (((Tx+maxX) <= t_2[0] and (Tx+maxX) >= t_1[0]) or ((Tx+minX) <= t_2[0] and (Tx+minX) >= t_1[0])) 
        and 
        (((Ty+maxY) <= t_2[1] and (Ty+minY) >= t_1[1]) or ((Ty+maxY) >= t_2[1] and (Ty+minY) <= t_1[1]))

         if(Tx+maxX) < t_1[0]:
            break
        if (Tx+minX) > t_2[0]:
            break
        if (Ty+maxY) < t_1[1]:        
            break
        if (Ty+minY) > t_2[1]:       
            break