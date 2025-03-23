dic = {
    "name" : "7D 건조 망고",
    "type" : "당절임",
    "ingerdient" : ["망고","설탕","치자황색소"],
    "origin" : "필리핀"
}

# for key in dic.keys():
#     print(key, dic.get(key)[0])

for key in dic.keys():
    print(key, dic.get(key))

    if type(dic.get(key)) == type([]): # 자료형 타입이 list면 처리
        print("===========")

        for i in dic.get(key):
            print(i, end = " ")
    print("\n =====================")
