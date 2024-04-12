def solution(a, b):
    answer = ''
    # 각 달의 일 수를 리스트로 저장
    days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    # 총 일 수를 7로 나눈 나머지에 따라 요일을 결정
    days_of_week = ["THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"]
    
    # 각 달의 일 수를 합산하여 총 일 수 계산
    total_days = sum(days_in_month[:a - 1]) + b
    
    
    answer = days_of_week[total_days % 7]
    
    
    return answer