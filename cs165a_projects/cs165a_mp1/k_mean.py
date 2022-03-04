def main():
    x = [[1.0,3.0], [2.0,3.0], [1.0,4.0], [1.0,5.0], [1.0,6.0], [2.0,6.0],[3.0,3.0],[4.0,1.0], [4.0,2.0], [5.0,1.0], [5.0,2.0]]
    clusters = [[1.57,4.29],[4.5,1.5]]
    print(len(x))
    print(len(clusters))


    for i in range(len(x)):
        for c in range(len(clusters)):
            if c == 0:
                print("C1 Distance")
            else:
                print("C2 Distance")

            print("C",clusters[c])
            print("D",x[i])
            xdif = (x[i][0] - clusters[c][0])**2
            ydif = (x[i][1] - clusters[c][1])**2
            dist = ydif + xdif
            print(dist)
            print("\n")

    
        

main()
