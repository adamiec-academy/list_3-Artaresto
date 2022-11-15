def tower(n):
    a = 1    
    for i in range(n):
        for _ in range(3):
                print(" " * (n - (i))  + "#" * (i + a) + " " * (n - (i + 1))) 
        a+=1
        
        
def towers(data):
    max_size = max(data)
    shift = 1
    for i in range(1, max_size+1):
        for _ in range(3):
            for idx in range(len(data)):
                
                total_width = 2 * data[idx] - 1
                current_width = total_width - (max_size - (2 * i - (data[idx])))
                
                spaces = total_width//2 - (current_width - shift)

                if 2 * spaces > total_width:
                    print(" " * total_width + " ", end="")
                else:
                    print(" " * spaces + "#" * (current_width - (max_size - data[idx])) + " " * spaces, end=" " )
            
            print()
        shift += 1
        
