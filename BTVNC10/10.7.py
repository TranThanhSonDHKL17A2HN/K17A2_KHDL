s=input("Nhập chuỗi s: ")
s_sub=input("Nhập chuỗi con s_sub: ")
s_find=input("Nhập chuỗi s_find: ")
s_replace=input("Nhập chuỗi thay thế s_replace: ")
print("Chuỗi s :",s)
print("Loại bỏ khoảng trắng ở đầu và cuối: ",s.strip())
print("Chuỗi s_find với kí tự đầu viết hoa: ",s_find.capitalize())
print("Số lần s_sub xuất hiện trong s :",s.count(s_sub,0,16))
print("Thay thế s_find bằng s_replace : ",s.replace(s_find,s_replace))