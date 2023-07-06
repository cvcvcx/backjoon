n = int(input())
count = 1
sum_ = 1
start_idx = 1
end_idx = 1

while end_idx<n:
    if sum_ == n:
        count += 1
        end_idx += 1
        sum_ += end_idx
        
    elif sum_ < n:
        end_idx += 1
        sum_ += end_idx
        
    elif sum_ > n:
        sum_ -= start_idx
        start_idx += 1
        
print(count)