hours = int(input("Enter hours: "))
minutes = int(input("Enter minutes: "))
duration = int(input("Enter duration in minutes: "))

end_hour = (hours + (minutes + duration) // 60) % 24
end_minute = (minutes + duration) % 60

print(f"End time: {end_hour}:{end_minute}")
