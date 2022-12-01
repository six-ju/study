def price(name,time):
    wage = 9650
    result = wage*time
    print(f"{name}은 {time}시간 일했으므로 월급은 {result}입니다")
    return result

price(name=input("이름"),time=int(input("시간"))) 
