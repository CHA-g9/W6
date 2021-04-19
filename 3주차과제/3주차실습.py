# 중첩 리스트 만들기
list_a = [1,2,3,["a","b","c"]]
print(list_a)
# 중첩된 리스트 요소에 접근하기
print(list_a[3])
print(list_a[3][2])
#리스트 길이 구하기
print(len(list_a))
#리스트 요소 추가하기
list_a = list_a + [4]
print(list_a)
#리스트 요소 삽입하기
list_a = [5] + list_a
print(list_a)
# 리스트 요소 제거하기
list_a = list_a[0:3] + list_a[4:]
print(list_a)
# 딕셔너리 만들기
dict_a = {1:'하나', 2:"둘", 3:"셋"}
print(dict_a)
# 딕셔너리 추가하기
dict_a[4] = "넷"
print(dict_a)
# 딕셔너리 삭제하기
del(dict_a[1])
print(dict_a)
