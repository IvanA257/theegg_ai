

def get_maximum_milk(n_cows, max_weight, cow_weight_list, cow_milk_production):

    # Generate a list of tuples containing the weight, milk production and efficiency of each cow.
    cow_list = [(milk_prod/weight, weight, milk_prod) for weight, milk_prod in zip(cow_weight_list, cow_milk_production)]

    # Sort the created list by efficiency
    cow_list.sort(key = lambda tup: tup[0], reverse = True)
    print("Sorted cow list")
    print(cow_list)

    # Pick the most efficient cows that fit into the truck.
    picked_cows = []
    weight = 0
    for cow in cow_list:
        if (weight + cow[1]) <= max_weight:
            picked_cows.append(cow)
            weight += cow[1]

    n_cow_list = []
    for cow in cow_list:
        if cow not in picked_cows:
            n_cow_list.append(cow)

    print(n_cow_list)
    print(picked_cows)
    print("Total weight: ", weight)

    not_picked = 0
    picked = 0
    while not_picked < len(n_cow_list):
        while picked < len(picked_cows):
            # If it fits the truck.
            picked_cow = picked_cows[picked]
            not_picked_cow = n_cow_list[not_picked]
            added_weight = not_picked_cow[1] - picked_cow[1]
            available_weight = max_weight - weight
            if added_weight <= available_weight:
                # If it increases the production
                if n_cow_list[not_picked][2] > picked_cows[picked][2]:
                    del picked_cows[picked]
                    picked_cows.append(not_picked_cow)
                    weight += added_weight
                    picked = 0
                    not_picked = 0
            picked += 1
        not_picked += 1

    print(picked_cows)
    print("Total weight: ", weight)
    return sum((i[2] for i in picked_cows))

print(get_maximum_milk(10, 2000, (340,355,223,243,130,240,260,155,302,130), (45,50,34,39,29,40,30,52,31,1)))