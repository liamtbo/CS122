'''
CIS 122 Fall 2021
Author: Liam Bouffard
Objective: use input list with commands: add, ?, list, and delete
'''

# part 1 - DONE

def get_max_list_item_size(t): pass

def pad_string(command, command_type, direction):
    '''
    space is multiplied by the total length minus the command str
    '''
    symbol = ' '
    total_length = len('delete') + 5
    command_length = len(command)

    symb_multi = symbol * (total_length - command_length) # subtracts character count of command and command type from total length
    if direction == 'pad_left':
        print (str(command) + symb_multi + command_type)
    if direction == 'pad_right':
        print (str(command) + symb_multi + command_type)

def pad_left(command, command_type, direction):
    direction = 'pad_left'
    pad_string(command, command_type, direction)

def pad_right(command, command_type, direction):
    direction = 'pad_right'
    pad_string(command, command_type, direction)

# -------------------------------------------------------------------
#part 2: List vars - DONE
list = []

# ------------------------------------------------------------------
# part 3: Primary Input Loop - DONE
while 2 != 4:
    prompt = input('Enter a command (? for help): ')
    prompt = prompt.strip()
    prompt = str(prompt)
    prompt = prompt.lower()
    t = prompt
    
    if len(prompt) == 0:
        break
    # -----------------------------------------------------------
    # part 4: Help command - DONE

    if '?' in t:
        admin_list = ['Add', 'Delete', 'List', 'Clear', 'Empty to exit']
        admin_list_info = ['Add to list', 'Delete information', 'List information', 'Clear list', '']
        get_max_list_item_size(prompt)
        print('*** Available commands ***')
        pad_right('Add', 'Add to list', 'pad_right')
        pad_right('Delete', 'Delete information', 'pad_right')
        pad_right('List', 'List information', 'pad_right')
        pad_right('Clear', 'Clear list', 'pad_right')
        pad_right('Empty to exit', '', 'pad_right')
        if len(prompt) == 0: 
            break

    # ------------------------------------------------------------
    # part 5: add command - DONE

    if 'add' in t:
        enter = False 
        while enter == False:
            t = input('Enter information (empty to stop): ')
            if len(t) == 0:
                break
            list += [t]
            print('Added, item count = ', len(list))
    
    # --------------------------------------------------------------
    # part 6: List command -DONE
    if 'list' in t:
        if len(prompt) == 0:
            break
        print('List contains', len(list), 'item(s)')
        for i in range(len(list)):
            print(list[i])
    
    # --------------------------------------------------------------
    # part 7: Clear Command - DONE
    if 'clear' in t:
        print(len(list), 'item(s) removed, list empty')
        for i in range(len(list)):
            del list[0]

    # --------------------------------------------------------------
    # Part 8: delete command - DONE
    if 'del' in t:
        while 2 != 4:
            # list number next to item
            for i in range(len(list)):
                print(i, ' ' + list[i])
                
            # fresh prompt inside del
            t = input('Enter number to delete (empty to stop): ')

            # guardian break
            if len(t) == 0:
                break
                
            # enter num to delete
            del list[int(t)]

            if len(list) == 0:
                print('All numbers deleted')
                break