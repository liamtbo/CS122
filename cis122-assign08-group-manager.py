'''
CIS 122 Fall 2021
Author: Liam Bouffard
Partner: Andrew Chan
Objective: creating a list manager to create a group manager.
'''

# part 1: DONE
def create_group(d):
    '''
    Create new group
    '''
    print("*** Create new group *** ")
    while 2 != 4:
        group_prompt = input("\nEnter group name (empty to cancel): ").strip()
        if group_prompt == "":
            break
        elif group_prompt in d:
            print("Invalid Group Name (Group Name Already Exists)")
            continue
        else:
            d[group_prompt] = {"fields":[], "data":[]}
            while 2 != 4:
                field = input("Enter field name (empty to stop): ").strip()
                if field == "":
                    break
                d[group_prompt]["fields"].append(field)
        
def list_groups(d):
    '''
    List groups
    '''
    print("*** List of groups ***")
    for i in d.keys():
        print(i, ":", len(d[i]["fields"]), "properties", "(" + ", ".join(d[i]["fields"]) + ")\n")

def add_group_data(d):
    '''
    Add group data
    '''
    list_groups(d)
    while True:
        prompt = input('Enter group (empty to cancel): ').strip()
        if len(prompt) == 0:
            break
        elif prompt not in d:
            print('Group does not exist in dictionary')
            continue
        else:
            for i in range(len(d[prompt]['fields'])):
                data = input('Enter ' + str(d[prompt]['fields'][i]) + ': ')
                
def list_group_data(d):
    print(" List group data ")
    list_groups(d)
    while True:
        group_name = input("Enter group name (empty to cancel): ")
        if len(group_name) == 0:
            break
        if group_name in d:
            for i in range(len(d[group_name]["data"])):
                temp_string = ""
                for q in d[group_name]["data"][i]:
                    keys = list(d[group_name]["data"][i].keys())
                    vals = list(d[group_name]["data"][i].values())
                for w in range(len(keys)):
                    if w == len(keys) - 1:
                        temp_string += "{} = {}".format(keys[w], vals[w])
                    elif w != len(keys):
                        temp_string += "{} = {}, ".format(keys[w], vals[w])
                print(i, temp_string)
        else:
            print("Group does not exist")
    print("")


# part 2: DONE
d = {}

# part 3: DONE
while 2 != 4:
    prompt = input('Command (empty or X to quit, ? for help): ').strip().upper()

    if len(prompt) == 0:
        break
    if prompt == 'X':
        break

# part 4: help command - DONE
    if '?' in prompt:
        print ('?: list commands')
        print ('C: Create a new group')
        print ('G: List groups')
        print ('A: Add data to a group')
        print ('L: List data for a group')
        print ('X: Exit')

# part 5: guardian code - DONE

# part 6: create new group
    if 'C' in prompt:
        create_group(d)
    if 'G' in prompt:
        list_groups(d)
    if 'A' in prompt:
        add_group_data(d)
    if 'L' in prompt:
        list_group_data(d)
