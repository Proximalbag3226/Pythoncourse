def find_median_sorted_arrays(nums1: list[int], nums2: list[int]) -> float:
    if not nums1 and not nums2:
        raise ValueError("Both input arrays are empty.")

    merged = sorted(nums1 + nums2)
    total = len(merged)

    if total % 2 == 1: 
        return float(merged[total // 2]) 

    middle1 = merged[total // 2 - 1]
    middle2 = merged[total // 2]
    return (float(middle1) + float(middle2)) / 2.0

#Falta comentar pero ya es noche 