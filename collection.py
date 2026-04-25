from collections import Counter

if __name__ == '__main__':
    # 1. Read the initial inventory
    num_shoes = int(input())
    shoe_sizes = list(map(int, input().split()))
    
    # Create the inventory counter: {size: quantity}
    inventory = Counter(shoe_sizes)
    
    # 2. Process customer orders
    num_customers = int(input())
    total_revenue = 0
    
    for _ in range(num_customers):
        size, price = map(int, input().split())
        
        # Check if the size is in stock
        if inventory[size] > 0:
            total_revenue += price
            # Reduce the stock by one
            inventory[size] -= 1
            
    print(total_revenue)
