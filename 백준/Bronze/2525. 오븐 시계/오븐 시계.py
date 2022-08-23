# 시 분
hour, minute = map(int, input().split())
needTime = int(input())

# 끝나는 시각
endMinute = hour*60 + minute + needTime
hour = endMinute // 60
minute = endMinute % 60
if hour > 23 : hour -= 24

print(hour, minute)