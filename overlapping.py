def combine_lists(list1, list2):
    combined = sorted(list1 + list2, key=lambda x: x['positions'][0])
    result = []

    def overlap(p1, p2):
        # Calculate overlap length
        l1, r1 = p1
        l2, r2 = p2
        overlap_len = max(0, min(r1, r2) - max(l1, l2))
        len1 = r1 - l1
        len2 = r2 - l2
        return overlap_len > 0.5 * min(len1, len2)
    
    for elem in combined:
        if not result:
            result.append(elem)
        else:
            last = result[-1]
            if overlap(last['positions'], elem['positions']):
                # Merge values
                last['values'] += elem['values']
            else:
                result.append(elem)
    return result

# Example usage:
list1 = [{"positions": [0, 5], "values": [1, 2]}]
list2 = [{"positions": [3, 8], "values": [3, 4]}]
print(combine_lists(list1, list2))
