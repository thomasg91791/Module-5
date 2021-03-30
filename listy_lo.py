if __name__ == "__main__":

    # food = ['rice','beans']
    # food.append('broccoli')
    # food.extend(['bread', 'pizza'])
    # print(food [0:2])
    # print(food[4])

    # food = ("eggs,fruit,orange juice")
    # breakfast = food.split(',')
    # print(len(breakfast))

    numlist = []
    while True:

        input_list = input('Enter a number: ')
        if input_list == 'stop':
            break
        else:
            numlist.append(float(input_list)) 
    
            min_input = min(numlist)
    
            max_input = max(numlist)
    
            average_input =sum(numlist) / len(numlist)
    print(f'average: {average_input} max: {max_input} min: {min_input}')
        
    

        