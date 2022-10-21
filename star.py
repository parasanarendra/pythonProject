totalSeconds = 400

secondsPerMinute = 60
secondsPerHour = 60 * secondsPerMinute
secondsPerDay = 24 * secondsPerHour

days = totalSeconds // secondsPerDay
hours = (totalSeconds - days * secondsPerDay) // secondsPerHour
minutes = (totalSeconds - days * secondsPerDay - hours * secondsPerHour) // secondsPerMinute
seconds = totalSeconds - days * secondsPerDay - hours * secondsPerHour - minutes * secondsPerMinute

if days > 0:
    print(days, 'Days', end=' ')
if hours > 0:
    print(hours, 'Hours', end=' ')
if minutes > 0:
    print(minutes, 'Minutes', end=' ')
if seconds > 0:
    print(seconds, 'Seconds', end=' ')
print()
print("popup displayed in bottom sections")
print("hello")