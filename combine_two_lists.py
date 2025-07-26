def overlap_ratio(pos1, pos2):
    left1, right1 = pos1
    left2, right2 = pos2

    overlap = max(0, min(right1, right2) - max(left1, left2))
    len1 = right1 - left1
    len2 = right2 - left2

    if len1 == 0 or len2 == 0:
        return 0

    shorter_len = min(len1, len2)
    return overlap / shorter_len


def combine_lists(list1, list2):
    combined = []
    used_list2 = set()

    for i, item1 in enumerate(list1):
        pos1 = item1["positions"]
        merged = False

        for j, item2 in enumerate(list2):
            if j in used_list2:
                continue

            pos2 = item2["positions"]
            ratio = overlap_ratio(pos1, pos2)

            if ratio > 0.5:
                new_item = {
                    "positions": pos1,
                    "values": item1["values"] + item2["values"]
                }
                combined.append(new_item)
                used_list2.add(j)
                merged = True
                break

        if not merged:
            combined.append(item1)

    for j, item2 in enumerate(list2):
        if j not in used_list2:
            combined.append(item2)

    combined.sort(key=lambda x: x["positions"][0])
    return combined


def get_list_from_user(list_name):
    n = int(input(f"How many elements in {list_name}? "))
    items = []
    for i in range(n):
        left = int(input(f"Enter left position for element {i+1}: "))
        right = int(input(f"Enter right position for element {i+1}: "))
        values = input(f"Enter values for element {i+1} (comma-separated): ").split(",")
        values = [v.strip() for v in values]
        items.append({
            "positions": [left, right],
            "values": values
        })
    return items


if __name__ == "__main__":
    print("Enter data for List 1:")
    list1 = get_list_from_user("List 1")
    print("\nEnter data for List 2:")
    list2 = get_list_from_user("List 2")

    result = combine_lists(list1, list2)
    print("\nCombined list:")
    for item in result:
        print(item)
