from time import time


def get_maximum_milk(n_cows, max_weight, cow_weight_list, cow_milk_production):
    """
    This function takes a list of cows and their weights and milk production rates. Then finds which group of cows
    produces the highest amount of milk without exceding the maximum total weight.

    The implemented algorithm consists in two stages:
        - Decent solution stage: Here the cows are sorted by efficiency (milk production/weight rate), then the most
                 efficient cows are selected (without exceding the max weight).
                 Two groups are created:
                     - The picked cows: These form part of the proposed solution.
                     - The non picked cows: These are the ones we did not select.

        - Solution improvement: Here we try to obtain a better solution by comparing the cows who were not picked in the
                                first solution with those picked.
                                If one of those comparisons reveals that we can exchange a non picked cow and a picked
                                one while:
                                    - We keep the total weight below the maximum.
                                    - The exchange increases the total milk production of the picked cow set.
                                Then we make that exchange and start comparing the picked and not picked cow sets.

    It is interesting to note that the first stage is not completely necessary. However, begining the improvement stage
    with a better solution than a random one may reduce the amount of operations needed to complete the improvement
    stage. That is why it was included.

    :param n_cows: Total amount of cows in the market.
    :param max_weight: Maximum weight the truck can handle.
    :param cow_weight_list: List of cow weights.
    :param cow_milk_production: List of the milk production of each cow.
    :return: The total milk production from the picked cows.
    """

    # GETTING A DECENT SOLUTION ----------------------------------------------------------------------------------------

    # Generate a list of tuples containing the weight, milk production and efficiency of each cow.
    cow_list = [(milk_prod/weight, weight, milk_prod) for weight, milk_prod in zip(cow_weight_list, cow_milk_production)]

    # Sort the created list by efficiency. We sort the list here expecting it to save work when improving the solution
    # a few lines down.
    cow_list.sort(key = lambda tup: tup[0], reverse = True)
    print("Sorted cow list")
    print(cow_list)

    # Pick the most efficient cows that fit into the truck.
    picked_cows = []
    n_cow_list = [] # These cows are not picked at first.
    weight = 0
    for cow in cow_list:
        if (weight + cow[1]) <= max_weight:
            picked_cows.append(cow)
            weight += cow[1]
        else:
            n_cow_list.append(cow)


    print(n_cow_list)
    print(picked_cows)
    print("Total weight: ", weight)

    # IMPROVING THE SOLUTION -------------------------------------------------------------------------------------------
    not_picked = 0
    picked = 0
    while not_picked < len(n_cow_list):
        while picked < len(picked_cows):
            # Take the cows instead of working with indexes
            picked_cow = picked_cows[picked]
            not_picked_cow = n_cow_list[not_picked]

            # Calculate the extra weight the cow exchange would imply
            added_weight = not_picked_cow[1] - picked_cow[1]

            # Calculate the spare weight in the truck
            available_weight = max_weight - weight

            # Now, the cow has to fit into the truck
            if added_weight <= available_weight:
                # And it has to increase the production
                if not_picked_cow[2] > picked_cow[2]:
                    # If both conditions are met we exchange the cows.
                    del picked_cows[picked]
                    picked_cows.append(not_picked_cow)
                    # And update the current weight loaded into the truck.
                    weight += added_weight

                    # Finally we reset both indices to avoid issues due to changing elements while iterating.
                    picked = 0
                    not_picked = 0
            picked += 1
        not_picked += 1

    print(picked_cows)
    print("Total weight: ", weight)
    return sum((i[2] for i in picked_cows))

start_time = time()
print(get_maximum_milk(10, 2000, (340,355,223,243,130,240,260,155,302,130), (45,50,34,39,29,40,30,52,31,1)))
end_time = time()
print("--- %s seconds ---" % (end_time - start_time))