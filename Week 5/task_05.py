import sys
length_args= len(sys.argv)

try: 

    if length_args <=1:
        print("No arguments were provided.")

    else:
        total=0
        while length_args> 1:
            length_args -= 1
            total += float(sys.argv[length_args])

        print("MIN TEMP: ",min(sys.argv[1:]))
        print("MAX TEMP: ",max(sys.argv[1:]))
        print("AVG TEMP: ",total/len(sys.argv[1:]))

except ValueError:
        print("Error processing data.")

