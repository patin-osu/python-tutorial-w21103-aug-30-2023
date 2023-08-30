score = int(input("คะเเนน: "))
status = input("สถานะการส่งงาน (ส่ง, ไม่ส่ง): ")

if (score>=90 and status=="ส่ง") : print("ดีเยื่ยม")
elif (score>=70 and status =="ส่ง") : print("ดี")
elif (score>=50 and status =="ส่ง") : print("ผ่าน")
elif (score>=0 and status =="ส่ง") : print("ไม่ผ่าน")
elif (score>=0 and status =="ไม่ส่ง") : print("ติด ร")
else: print("ข้อมูลไม่ถูกต้อง")
