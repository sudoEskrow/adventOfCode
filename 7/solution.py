input = open('./input').read().split('.\n')
# input = open('./testinput').read().split('.\n')

bags = []


class Bag:
    def __init__(self, inputstr):
        self.bag_name = ' '.join(inputstr.split()[:2])
        self.contained_in = None
        self.contains = []
        if len(inputstr.split()) > 4:
            contain = inputstr.split()[4:]
            if contain[0] == 'no':
                pass
            else:
                no = int(len(contain) / 4)
                while contain != []:
                    number = contain[0]
                    bag = ' '.join(contain[1:3])
                    self.contains.append([bag, number])
                    contain = contain[4:]


def find_bag(bagName):
    for bag in bags:
        if bag.bag_name == bagName:
            return bag


def find_direct_container(bagName):
    containers = []
    for bag in bags:
        for contained_bag in bag.contains:
            if contained_bag[0] == bagName:
                containers.append(bag)
    return containers


for bag in input:
    bags.append(Bag(bag))


def make_tree():
    for bag in bags:
        bag.contained_in = find_direct_container(bag.bag_name)
    for bag in bags:
        for contained_bag in bag.contains:
            contained_bag[0] = find_bag(contained_bag[0])


make_tree()


def get_no_of_bags(bag):
    if bag.contains == []:
        return 1
    else:
        count = 1
        for internal_bag in bag.contains:
            count += int(internal_bag[1]) * get_no_of_bags(internal_bag[0])
    return count


# print(get_no_of_bags(find_bag('dark olive')))
# print(get_no_of_bags(find_bag('shiny gold')))


def solution_1(bag_colour):
    container_bags = [find_bag(bag_colour)]
    banned_bags = []
    bag_count = 0
    while(len(container_bags) > 0):
        bag = container_bags.pop()
        if isinstance(bag, list):
            bag = bag[0]
        if bag not in banned_bags:
            banned_bags.append(bag)
            bag_count += 1
            for i in bag.contained_in:
                container_bags.append(i)
    return bag_count-1


def solution_2(bag_colour):
    original_bag = find_bag(bag_colour)
    return get_no_of_bags(original_bag) - 1


print('Solution for part 1 is:', solution_1('shiny gold'))
print('Solution for part 2 is:', solution_2('shiny gold'))
