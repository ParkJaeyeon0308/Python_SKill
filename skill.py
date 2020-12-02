import tkinter
import tkinter as tk
import time
import datetime
from datetime import datetime
from tkinter import *
import pytz
import os
from tkinter import messagebox as msg

#전체를 통괄하는 클래스
class Planerlist:
    def __init__(self):

        #시간체크 화면으로 넘어가는 함수
        def count():

            #글로벌 변수 begin, end 선언
            global begin
            global end

            #시간체크 윈도우 창 생성
            window = tk.Toplevel()
            window.title("시간체크")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 시작버튼을 눌렀을 때 발생하는 이벤트
            def startClick():
                global begin
                now = datetime.now()
                begin = now
                return tk.Label(window, text=now.strftime("%H:%M:%S")).place(x="295", y="350")

            # 종료버튼을 눌렀을 때 발생하는 이벤트
            def endClick():
                global begin
                global end
                now2 = datetime.now()
                end = now2
                re = end - begin
                label1 = tk.Label(window, text=now2.strftime("%H:%M:%S")).place(x="605", y="350")
                label2 = tk.Label(window, text=re, width="30", height="5").place(x="370", y="180")
                return label1, label2

            #타이머를 시작, 종료하는 버튼
            buttonA = tk.Button(window, text="시작", bg="RosyBrown3", fg="white", width="20", height="2",
                                     command=startClick).place(x="250", y="300")
            buttonB = tk.Button(window, text="종료", bg="RosyBrown3", fg="white", width="20", height="2",
                                     command=endClick).place(x="555", y="300")

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()



        #월요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                     overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                     overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            mondayPlanWrite = tk.Text(window, height=22)
            mondayPlanWrite.place(x=340, y=140)

            #월요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addMon():
                monPlan_file = open("Mon_studyPlan.txt", "a+", encoding="utf-8")
                text1 = mondayPlanWrite.get(1.0, tk.END + "-1c")
                monPlan_file.write(text1)

                monPlan_file.read()
                monPlan_file.close()

            #생성된 파일을 삭제하는 이벤트
            def deleteMon():
                #파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Mon_studyPlan.txt"):
                    monPlanRemove = os.remove('Mon_studyPlan.txt')
                #존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                       overrelief="solid", command=addMon)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                       overrelief="solid", command=deleteMon)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        #화요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window2():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                     overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                     overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                     overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            tuedayPlanWrite = tk.Text(window, height=22)
            tuedayPlanWrite.place(x=340, y=140)

            # 화요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addTues():
                tuePlan_file = open("Tue_studyPlan.txt", "a+", encoding="utf-8")
                text2 = tuedayPlanWrite.get(1.0, tk.END + "-1c")
                tuePlan_file.write(text2)

                tuePlan_file.read()
                tuePlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteTues():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Tue_studyPlan.txt"):
                    tuePlanRemove = os.remove('Tue_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                       overrelief="solid", command=addTues)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                       overrelief="solid", command=deleteTues)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        # 수요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window3():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            weddayPlanWrite = tk.Text(window, height=22)
            weddayPlanWrite.place(x=340, y=140)

            # 수요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addWed():
                wedPlan_file = open("Wed_studyPlan.txt", "a+", encoding="utf-8")
                text3 = weddayPlanWrite.get(1.0, tk.END + "-1c")
                wedPlan_file.write(text3)

                wedPlan_file.read()
                wedPlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteWed():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Wed_studyPlan.txt"):
                    wedPlanRemove = os.remove('Wed_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=addWed)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=deleteWed)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        # 목요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window4():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            thudayPlanWrite = tk.Text(window, height=22)
            thudayPlanWrite.place(x=340, y=140)

            # 목요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addThu():
                thuPlan_file = open("Thu_studyPlan.txt", "a+", encoding="utf-8")
                text4 = thudayPlanWrite.get(1.0, tk.END + "-1c")
                thuPlan_file.write(text4)

                thuPlan_file.read()
                thuPlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteThu():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Thu_studyPlan.txt"):
                    thuPlanRemove = os.remove('Thu_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=addThu)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=deleteThu)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        # 금요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window5():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            fridayPlanWrite = tk.Text(window, height=22)
            fridayPlanWrite.place(x=340, y=140)

            # 금요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addFri():
                friPlan_file = open("Fri_studyPlan.txt", "a+", encoding="utf-8")
                text5 = fridayPlanWrite.get(1.0, tk.END + "-1c")
                friPlan_file.write(text5)

                friPlan_file.read()
                friPlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteFri():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Fri_studyPlan.txt"):
                    friPlanRemove = os.remove('Fri_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=addFri)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=deleteFri)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        # 토요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window6():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            satdayPlanWrite = tk.Text(window, height=22)
            satdayPlanWrite.place(x=340, y=140)

            # 토요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addSat():
                satPlan_file = open("Sat_studyPlan.txt", "a+", encoding="utf-8")
                text6 = satdayPlanWrite.get(1.0, tk.END + "-1c")
                satPlan_file.write(text6)

                satPlan_file.read()
                satPlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteSat():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Sat_studyPlan.txt"):
                    satPlanRemove = os.remove('Sat_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=addSat)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=deleteSat)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        # 일요일 플래너 작성화면으로 넘어가는 함수
        def generate_new_window7():
            window = tk.Toplevel()
            window.title("스터디플래너")
            window.geometry("942x542")
            window.resizable(width="False", height="False")

            # 상단 메뉴 버튼
            button1 = tk.Button(window, text="시간 체크", bg="gray", fg="white", width="70", height="2",
                                overrelief="solid", command=count).place(x=0, y=0)
            button2 = tk.Button(window, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",
                                overrelief="solid").place(x=471, y=0)

            # 왼쪽 '스터디 플래너 작성' 버튼
            buttonA = tk.Button(window, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonB = tk.Button(window, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonC = tk.Button(window, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonD = tk.Button(window, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonE = tk.Button(window, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonF = tk.Button(window, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")
            buttonG = tk.Button(window, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2",
                                overrelief="solid")

            # 왼쪽 '스터디 플래너 작성' 버튼 이벤트
            buttonA.place(x=70, y=140)
            buttonB.place(x=70, y=190)
            buttonC.place(x=70, y=240)
            buttonD.place(x=70, y=290)
            buttonE.place(x=70, y=340)
            buttonF.place(x=70, y=390)
            buttonG.place(x=70, y=440)

            # 오른쪽 '스터디 플래너 입력칸'
            sundayPlanWrite = tk.Text(window, height=22)
            sundayPlanWrite.place(x=340, y=140)

            # 일요일 플래너를 생성, 작성, 읽어오기를 수행하는 이벤트
            def addSun():
                sunPlan_file = open("Sun_studyPlan.txt", "a+", encoding="utf-8")
                text7 = sundayPlanWrite.get(1.0, tk.END + "-1c")
                sunPlan_file.write(text7)

                sunPlan_file.read()
                sunPlan_file.close()

            # 생성된 파일을 삭제하는 이벤트
            def deleteSun():
                # 파일이 디렉터리 안에 있다면, 파일 삭제
                if os.path.isfile("Sun_studyPlan.txt"):
                    sun_PlanRemove = os.remove('Sun_studyPlan.txt')
                # 존재하지 않는다면, 로직 종료
                else:
                    False

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd = tk.Button(window, text="내용 등록", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=addSun)
            buttonDel = tk.Button(window, text="내용 삭제", bg="RosyBrown3", fg="white", width="30", height="2",
                                  overrelief="solid", command=deleteSun)

            # 오른쪽 하단 스터디 플래너 등록, 삭제 버튼
            buttonAdd.place(x=380, y=440)
            buttonDel.place(x=630, y=440)

            # 배경 색 지정
            window.configure(background="RosyBrown")
            window.mainloop()

        #월요일 스터디플래너 보기
        def monPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Mon_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50, text=readTxt, wraplength=300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 화요일 스터디플래너 보기
        def tuesPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Tue_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50, text=readTxt, wraplength=300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 수요일 스터디플래너 보기
        def wedPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Wed_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50, text=readTxt, wraplength=300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 목요일 스터디플래너 보기
        def thursPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Thu_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50,text=readTxt, wraplength = 300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 금요일 스터디플래너 보기
        def friPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Fri_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50,text=readTxt, wraplength = 300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 토요일 스터디플래너 보기
        def satPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Sat_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50, text=readTxt, wraplength=300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 일요일 스터디플래너 보기
        def sunPlaner():
            window = tk.Toplevel()
            window.title("스터디플래너 보기")
            window.geometry("500x500")
            window.resizable(width="False", height="False")

            readTxt = open('Sun_studyPlan.txt', 'rt', encoding='UTF8')
            readTxt = readTxt.readline()
            txt = readTxt.split("\n")

            textLable = tk.Label(window, height=30, width=50, text=readTxt, wraplength=300)
            textLable.place(x=70, y=20)

            window.configure(background="RosyBrown")
            window.mainloop()

        # 942x542 크기의 창 생성
        self.root = tk.Tk()
        self.root.title("스터디플래너")
        self.root.geometry("942x542")
        self.root.resizable(width="False", height="False")

        #상단 메뉴 버튼
        self.button1 = tk.Button(self.root, text="시간 체크", bg="gray", fg="white", width="70", height="2", overrelief="solid", command=count).place(x=0, y=0)
        self.button2 = tk.Button(self.root, text="스터디 플래너", bg="RosyBrown3", fg="white", width="70", height="2",overrelief="solid").place(x=471, y=0)

        # 왼쪽 '스터디 플래너 작성' 버튼
        self.buttonA = tk.Button(self.root, text="월요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window)
        self.buttonB = tk.Button(self.root, text="화요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window2)
        self.buttonC = tk.Button(self.root, text="수요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window3)
        self.buttonD = tk.Button(self.root, text="목요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window4)
        self.buttonE = tk.Button(self.root, text="금요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window5)
        self.buttonF = tk.Button(self.root, text="토요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window6)
        self.buttonG = tk.Button(self.root, text="일요일 플래너 작성", bg="RosyBrown3", fg="white", width="30", height="2", overrelief="solid", command=generate_new_window7)

        # 오른쪽 '스터디 플래너 보기' 버튼
        self.buttonA1 = tk.Button(self.root, text="월요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=monPlaner)
        self.buttonB2 = tk.Button(self.root, text="화요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=tuesPlaner)
        self.buttonC3 = tk.Button(self.root, text="수요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=wedPlaner)
        self.buttonD4 = tk.Button(self.root, text="목요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=thursPlaner)
        self.buttonE5 = tk.Button(self.root, text="금요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=friPlaner)
        self.buttonF6 = tk.Button(self.root, text="토요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=satPlaner)
        self.buttonG7 = tk.Button(self.root, text="일요일 플래너 보기", bg="RosyBrown3", fg="white", width="70", height="2", command=sunPlaner)

        # 왼쪽 '스터디 플래너 작성' 버튼 위치
        self.buttonA.place(x=70, y=140)
        self.buttonB.place(x=70, y=190)
        self.buttonC.place(x=70, y=240)
        self.buttonD.place(x=70, y=290)
        self.buttonE.place(x=70, y=340)
        self.buttonF.place(x=70, y=390)
        self.buttonG.place(x=70, y=440)

        # 오른쪽 '스터디 플래너 보기' 버튼 위치
        self.buttonA1.place(x=340, y=140)
        self.buttonB2.place(x=340, y=190)
        self.buttonC3.place(x=340, y=240)
        self.buttonD4.place(x=340, y=290)
        self.buttonE5.place(x=340, y=340)
        self.buttonF6.place(x=340, y=390)
        self.buttonG7.place(x=340, y=440)

        # 배경 색 지정
        self.root.configure(background="RosyBrown")
        self.root.mainloop()
Planerlist()
