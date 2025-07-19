max_profit = 0
best_x = 0
best_y = 0
for x in range(101):      
    for y in range(101):   
        wood = 5 * x + 20 * y
        labor = 10 * x + 15 * y
        if wood <= 400 and labor <= 600:
            profit = 20 * x + 50 * y
            if profit > max_profit:
                max_profit = profit
                best_x = x
                best_y = y

print("Best number of Chairs:", best_x)
print("Best number of Tables:", best_y)
print("Maximum Profit: $", max_profit)
