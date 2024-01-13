#Romika Chaudhary
#C0921918
#Assignment 8
#Nov 23, 2023


# Function 1: add_two
def add_two(a, b):
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return a + b
    elif isinstance(a, (str, list, tuple)) and isinstance(b, (str, list, tuple)):
        return a + b
    else:
        raise ValueError("Unsupported types for add_two function")

# Function 2: seq_total
def seq_total(seq):
    if all(isinstance(item, (int, float)) for item in seq):
        return sum(seq)
    elif all(isinstance(item, (str)) for item in seq):
        return ''.join(seq)
    else:
        raise ValueError("Unsupported types in the sequence for seq_total function")

# Function 3: seq_split
def seq_split(seq):
    length = len(seq)
    split_index = length // 2 if length % 2 == 0 else length // 2 + 1
    return [seq[:split_index], seq[split_index:]]

# Function 4: safe_list_remove
def safe_list_remove(lst, element):
    if element in lst:
        lst_copy = lst[:]
        lst_copy.remove(element)
        return lst_copy
    else:
        return lst

# Function 5: seq_min_max
def seq_min_max(seq):
    return min(seq), max(seq)