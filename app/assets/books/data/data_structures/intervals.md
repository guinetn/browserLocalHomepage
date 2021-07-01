# intervals


Single interval
Non-overlapping intervals
An interval totally consumed within another interval
Duplicate intervals

interval array: [[1, 2], [4, 7]]

def is_overlap(a, b):
  return a[0] < b[1] and b[0] < a[1]

def merge_overlapping_intervals(a, b):
  return [min(a[0], b[0]), max(a[1], b[1])]