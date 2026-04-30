def solution(numbers):
    answer = ""
    s_number = {"zero" : "0", "one" : "1", "two": "2", "three":"3", "four":"4", "five":"5", "six" : "6", "seven" : "7", "eight" : "8", "nine":"9"}
    numbers = list(numbers)
    word = ""
    for i in range(len(numbers)):

        word += numbers[i]
        if word in s_number.keys():
            answer += s_number[word]
            word = ''
          
    return int(answer)