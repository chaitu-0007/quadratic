
a = 0.02  
b = -0.5 
c = 25  

def quadratic(x, a, b, c):
    return a * x**2 + b * x + c

time_of_day = 12  

predicted_temperature = quadratic(time_of_day, a, b, c)
print(f"Predicted temperature at {time_of_day} hours: {predicted_temperature:.2f}°C")
