# (◕‿-)     (>‿◠)✌

from sqlite3 import connect
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets,QtGui
from PyQt5.QtWidgets import QDialog,QApplication,QWidget
from db_connection import connection
from datastructures.Dictionary import Dictionary
import csv  
# import time
from datastructures.Hash_table import HashTable
from datastructures.Linked_list import LinkedList



class Home(QDialog):
    def __init__(self):
        super(Home,self).__init__()
        loadUi("home.ui",self)
        self.push_PC.setStyleSheet("QPushButton::hover"
                                "{"
                                "background-color : rgb(98, 98, 98);"
                                "color: rgb(255,255,252);"
                                "}")
        
        self.push_CO.setStyleSheet("QPushButton::hover"
                                "{"
                                "background-color : rgb(98, 98, 98);"
                                "color: rgb(255,255,252);"
                                "}")
        
        self.push_EC.setStyleSheet("QPushButton::hover"
                                "{"
                                "background-color : rgb(98, 98, 98);"
                                "color: rgb(255,255,252);"
                                "}")
        
        
        self.push_CO.clicked.connect(self.gotologin_CO)
        self.push_PC.clicked.connect(self.gotologin_PC)
        self.push_EC.clicked.connect(self.gotologin_EC)
    
    def gotologin_CO(self):
        login=LoginScreen(role="Collection Officer")
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # widget.setFixedHeight(435)
        # widget.setFixedWidth(344)
        widget.setFixedSize(344,435)
    
    def gotologin_PC(self):
        login=LoginScreen(role="Police Commissioner")
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # widget.setFixedHeight(435)
        # widget.setFixedWidth(344)
        widget.setFixedSize(344,435)
    
    def gotologin_EC(self):
        login=LoginScreen(role="Election Commissioner")
        widget.addWidget(login)
        widget.setCurrentIndex(widget.currentIndex()+1)
        # widget.setFixedHeight(435)
        # widget.setFixedWidth(344)
        widget.setFixedSize(344,435)
        
        

class LoginScreen(QDialog):
    def __init__(self,role):
        self.role=role
        super(LoginScreen,self).__init__()
        loadUi("loginscreen.ui",self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.login.clicked.connect(self.loginfunction)
        self.back.clicked.connect(self.gobacktohome)
        
    def loginfunction(self):
        username=self.username.text()
        password=self.password.text()
        self.username.clear()
        self.password.clear()
        self.error.clear()
        #validation
        if len(username)<=0 or len(password)<=0:
            self.error.setText("*required fields cannot be empty")
        
        else:
            con,cur=connection()
            cur.execute('select password,role from users where user_id=\''+username+"\'")
            try:
                current=cur.fetchone()
                db_password=current[0]
                db_role=current[1]
            except:
                db_password=-1
                
            if db_password==-1:
                self.error.setText("*Invalid username or password")
            else:
                if self.role.lower()==db_role.lower():
                    if password==db_password :
                        if db_role.lower()=="collection officer":
                            page=CO_page()
                            widget.addWidget(page)
                            widget.setCurrentIndex(widget.currentIndex()+1)
                            # widget.setFixedHeight(435)
                            # widget.setFixedWidth(344)
                            widget.setFixedSize(1427,545)
                            print("Successfully Logged in.")
                            
                        elif db_role.lower()=="police commissioner":
                            page=PC_page()
                            widget.addWidget(page)
                            widget.setCurrentIndex(widget.currentIndex()+1)
                            # widget.setFixedHeight(435)
                            # widget.setFixedWidth(344)
                            widget.setFixedSize(1381,545)
                            print("Successfully Logged in.")
                            
                        elif db_role.lower()=="election commissioner":
                            page=EC_page()
                            widget.addWidget(page)
                            widget.setCurrentIndex(widget.currentIndex()+1)
                            # widget.setFixedHeight(435)
                            # widget.setFixedWidth(344)
                            widget.setFixedSize(1427,545)
                            print("Successfully Logged in.")
                            
                        # print(db_role)
                    else:
                        self.error.setText("*Invalid username or password")
                else:
                    self.error.setText("*Role Mismatch")
        
    def gobacktohome(self):
        home=Home()
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedHeight(811)
        widget.setFixedWidth(1023)
    
   
class CO_page(QDialog):
    def __init__(self):
        super(CO_page,self).__init__()
        loadUi("CO_page.ui",self)
        self.back.clicked.connect(self.gobacktologin)
        self.nominee_details.setColumnWidth(0,100)
        self.nominee_details.setColumnWidth(6,30)
        self.nominee_details.setColumnWidth(7,200)
        self.load_data()
        self.add.clicked.connect(self.add_candidate)
        self.submit.clicked.connect(self.save)
        
    
    def save(self):
        self.saving.clear()
        if self.send.isChecked()==True:
            self.saving.setText("Sent!")
            self.close_application()
        else:
            self.saving.setText("↻ saving...")
            self.close_application()
 
    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Close',
                                            "Save and Exit?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        
    def add_candidate(self):
        name=self.name.text()
        address=self.address.text()
        reg_id=self.reg_id.text()
        adhaar=self.adhaar.text()
        age=self.age.text()
        dob=self.dob.text()
        num=self.num.text()
        edu=self.edu.text()
        self.name.clear()
        self.address.clear()
        self.reg_id.clear()
        self.adhaar.clear()
        self.age.clear()
        self.dob.clear()
        self.num.clear()
        self.edu.clear()
        if len(name)<=0 or len(address)<=0 or len(reg_id)<=0 or len(adhaar)<=0 or len(dob)<=0 or len(age)<=0 or len(num)<=0 or len(edu)<=0:
            self.error.setText("*reuired fields cannot be empty")
        else:
            data=[name,address,reg_id,num,adhaar,dob,age,edu]
            with open(r'spreadsheets\Nominee_details.csv', 'a',newline='\n') as f:
                writer = csv.writer(f)
                writer.writerow(data)

        self.load_data()
        
        
        
    def load_data(self):
        row_count=0
        rows = []
        file = open(r"spreadsheets\Nominee_details.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            d=Dictionary()
            d['Name'],d['Address'],d['Registration ID'],d['mobile No'],d['Adhaar No'],d['DOB'],d['Age'],d['Educational Qualification']=row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
            rows.append(d)
        self.nominee_details.setRowCount(len(rows))
        for candidate in rows:
            self.nominee_details.setItem(row_count,0,QtWidgets.QTableWidgetItem(candidate['Name']))
            self.nominee_details.setItem(row_count,1,QtWidgets.QTableWidgetItem(candidate['Address']))
            self.nominee_details.setItem(row_count,2,QtWidgets.QTableWidgetItem(candidate['Registration ID']))
            self.nominee_details.setItem(row_count,3,QtWidgets.QTableWidgetItem(candidate['mobile No']))
            self.nominee_details.setItem(row_count,4,QtWidgets.QTableWidgetItem(candidate['Adhaar No']))
            self.nominee_details.setItem(row_count,5,QtWidgets.QTableWidgetItem(candidate['DOB']))
            self.nominee_details.setItem(row_count,6,QtWidgets.QTableWidgetItem(candidate['Age']))
            self.nominee_details.setItem(row_count,7,QtWidgets.QTableWidgetItem(candidate['Educational Qualification']))
            row_count+=1
            
    def gobacktologin(self):
        home=LoginScreen(role="Collection Officer")
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(344,435)
            

class PC_page(QDialog):
    def __init__(self):
        super(PC_page,self).__init__()
        loadUi("PC_page.ui",self)
        self.back.clicked.connect(self.gobacktologin)
        self.record.setColumnWidth(3,150)
        self.record.setColumnWidth(8,150)
        self.record.setColumnWidth(5,200)
        self.record.setColumnWidth(1,150)
        self.load_data()
        self.submit.clicked.connect(self.close_application)
        self.candidates.clicked.connect(self.load_only_criminal_candidates)
        self.criminals.clicked.connect(self.load_data)

    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Close',
                                            "Save and Exit?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        
    def load_data(self):
        row_count=0
        self.record.setRowCount(len(records))
        for criminals in records:
            h.insert(str(criminals[8]),criminals[:-1])
            self.record.setItem(row_count,0,QtWidgets.QTableWidgetItem(criminals[0]))
            self.record.setItem(row_count,1,QtWidgets.QTableWidgetItem(criminals[1]))
            self.record.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(criminals[2])))
            self.record.setItem(row_count,3,QtWidgets.QTableWidgetItem(criminals[3]))
            self.record.setItem(row_count,4,QtWidgets.QTableWidgetItem(criminals[4]))
            self.record.setItem(row_count,5,QtWidgets.QTableWidgetItem(criminals[5]))
            self.record.setItem(row_count,6,QtWidgets.QTableWidgetItem(criminals[6]))
            self.record.setItem(row_count,7,QtWidgets.QTableWidgetItem(str(criminals[7])))
            self.record.setItem(row_count,8,QtWidgets.QTableWidgetItem(str(criminals[8])))
            row_count+=1
            
    def load_only_criminal_candidates(self):
        row_count=0
        # for adhaar in nominee_adhaar:
        #     try:
        #         item=h.find(str(adhaar))
        #         if item!=None:
        #             criminal_nominees.append(item+(adhaar.value,))
        #             criminal_nominees_adhaar.add_node(adhaar.value)
        #     except:
        #         pass
        self.record.setRowCount(len(criminal_nominees))
        
        for item in criminal_nominees:
            self.record.setItem(row_count,0,QtWidgets.QTableWidgetItem(item[0]))
            self.record.setItem(row_count,1,QtWidgets.QTableWidgetItem(item[1]))
            self.record.setItem(row_count,2,QtWidgets.QTableWidgetItem(str(item[2])))
            self.record.setItem(row_count,3,QtWidgets.QTableWidgetItem(item[3]))
            self.record.setItem(row_count,4,QtWidgets.QTableWidgetItem(item[4]))
            self.record.setItem(row_count,5,QtWidgets.QTableWidgetItem(item[5]))
            self.record.setItem(row_count,6,QtWidgets.QTableWidgetItem(item[6]))
            self.record.setItem(row_count,7,QtWidgets.QTableWidgetItem(str(item[7])))
            self.record.setItem(row_count,8,QtWidgets.QTableWidgetItem(str(item[8])))
            row_count+=1
                
        

    def gobacktologin(self):
        home=LoginScreen(role="police commissioner")
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(344,435)


class EC_page(QDialog):
    def __init__(self):
        super(EC_page,self).__init__()
        loadUi("EC_page.ui",self)
        self.back.clicked.connect(self.gobacktologin)
        self.nominee_details.setSelectionBehavior(QtWidgets.QTableView.SelectRows)
        self.nominee_details.setColumnWidth(0,100)
        self.nominee_details.setColumnWidth(6,30)
        self.nominee_details.setColumnWidth(7,200)
        self.nominee_details.setColumnWidth(9,200)
        self.load_data()
        self.submit.clicked.connect(self.close_application)
        self.nominee_details.selectionModel().selectionChanged.connect(self.on_selectionChanged)
        self.accepted.stateChanged.connect(self.disablerejected)
        self.rejected.stateChanged.connect(self.disableaccepted)
        self.update.clicked.connect(self.decide)
        

    def on_selectionChanged(self,selected):
        global row
        row=(selected.indexes()[0].row())


    def disablerejected(self):
        if self.accepted.isChecked()==True:
            self.rejected.setChecked(False)
    
    def disableaccepted(self):
        if self.rejected.isChecked()==True:
            self.accepted.setChecked(False)

    def decide(self):
        model = self.nominee_details.model()
        indexes = self.nominee_details.selectionModel().selectedRows(column=2)
        for index in indexes:
            adhaar_no=model.data(model.index(index.row(), 4))
        con,cur=connection()
        cur.execute("select adhaar_no from selected_candidates")
        element=[]
        for a in cur.fetchall():
            element.append(a[0])
        if self.accepted.isChecked()==True:
            self.rejected.setChecked(False)
            self.nominee_details.setItem(row,9,QtWidgets.QTableWidgetItem("Accepted"))
            # print("rejected",type(element),type(adhaar_no),int(adhaar_no) in element)
            if int(adhaar_no) in element:
                cur.execute('update selected_candidates set accepted_rejected ="Accepted" where adhaar_no="{}"'.format(adhaar_no))
            else:
                cur.execute('insert into selected_candidates values("{}","{}")'.format(adhaar_no,"Accepted"))
        if self.rejected.isChecked()==True:
            self.accepted.setChecked(False)
            self.nominee_details.setItem(row,9,QtWidgets.QTableWidgetItem("Rejected"))
            # print("rejected",element,adhaar_no,adhaar_no in element)
            if int(adhaar_no) in element:
                cur.execute('update selected_candidates set accepted_rejected ="Rejected" where adhaar_no="{}"'.format(adhaar_no))
            else:
                cur.execute('insert into selected_candidates values("{}","{}")'.format(adhaar_no,"Rejected"))
            
        con.commit()
        con.close()


    def close_application(self):
        choice = QtWidgets.QMessageBox.question(self, 'Close',
                                            "Save and Exit?",
                                            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)
        if choice == QtWidgets.QMessageBox.Yes:
            print("Naaaaaaoooww!!!!")
            sys.exit()
        else:
            pass
        
        
    def load_data(self):
        row_count=0
        rows = []
        file = open(r"spreadsheets\Nominee_details.csv")
        csvreader = csv.reader(file)
        header = next(csvreader)
        for row in csvreader:
            d=Dictionary()
            d['Name'],d['Address'],d['Registration ID'],d['mobile No'],d['Adhaar No'],d['DOB'],d['Age'],d['Educational Qualification']=row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]
            rows.append(d)
        self.nominee_details.setRowCount(len(rows))
        for candidate in rows:
            self.nominee_details.setItem(row_count,0,QtWidgets.QTableWidgetItem(candidate['Name']))
            self.nominee_details.setItem(row_count,1,QtWidgets.QTableWidgetItem(candidate['Address']))
            self.nominee_details.setItem(row_count,2,QtWidgets.QTableWidgetItem(candidate['Registration ID']))
            self.nominee_details.setItem(row_count,3,QtWidgets.QTableWidgetItem(candidate['mobile No']))
            self.nominee_details.setItem(row_count,4,QtWidgets.QTableWidgetItem(candidate['Adhaar No']))
            self.nominee_details.setItem(row_count,5,QtWidgets.QTableWidgetItem(candidate['DOB']))
            self.nominee_details.setItem(row_count,6,QtWidgets.QTableWidgetItem(candidate['Age']))
            self.nominee_details.setItem(row_count,7,QtWidgets.QTableWidgetItem(candidate['Educational Qualification']))
            if str(candidate['Adhaar No']) in criminal_nominees_adhaar.values:
                    for i in criminal_nominees:
                        if i[-1]==str(candidate['Adhaar No']):
                            self.nominee_details.setItem(row_count,8,QtWidgets.QTableWidgetItem(i[3]))
            else:
                self.nominee_details.setItem(row_count,8,QtWidgets.QTableWidgetItem("NIL"))
            
            row_count+=1
            
    def gobacktologin(self):
        home=LoginScreen(role="Collection Officer")
        widget.addWidget(home)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setFixedSize(344,435)
            
                    
# CO:
# 1046222077
# Harold+27914

# PC:
# 1062050703
# Ben+28336

# EC:
# 1041514813
# Madora+27788


        
#main
if __name__=="__main__":
    nominee_adhaar=LinkedList()
    file = open(r"spreadsheets\Nominee_details.csv")
    csvreader = csv.reader(file)
    header = next(csvreader)
    for i in csvreader:
        nominee_adhaar.add_node(i[4])


    criminal_nominees=[]
    con,cur=connection()
    cur.execute("drop table selected_candidates")
    cur.execute("create table selected_candidates(adhaar_no integer,accepted_rejected char(10))")
    cur.execute("select * from police_records")
    records=[]
    for row in cur:
        records.append(row)


    h=HashTable(len(records))
    criminal_nominees_adhaar=LinkedList()


    for criminals in records:
        h.insert(str(criminals[8]),criminals[:-1])


    for adhaar in nominee_adhaar:
        try:
            item=h.find(str(adhaar))
            if item!=None:
                criminal_nominees.append(item+(adhaar.value,))
                criminal_nominees_adhaar.add_node(adhaar.value)
        except:
            pass
    
    # print("\n\n",records)

    # # all candidate details
    # nominee_adhaar=LinkedList()
    # file = open(r"spreadsheets\Nominee_details.csv")
    # csvreader = csv.reader(file)
    # header = next(csvreader)
    # for i in csvreader:
    #     nominee_adhaar.add_node(i[4])
    # #criminal nominees
    # con,cur=connection()
    # cur.execute("select * from police_records")
    # records=[]
    # for row in cur:
    #     records.append(row)
    # h=HashTable(len(records))
    # criminal_nominees=[]
    # criminal_nominees_adhaar=LinkedList()

    # running the App
    app= QApplication(sys.argv)
    home=Home()
    widget= QtWidgets.QStackedWidget()
    widget.addWidget(home)
    widget.setFixedHeight(811)
    widget.setFixedWidth(1023)
    widget.setWindowTitle("Election Nomination System")
    widget.setWindowIcon(QtGui.QIcon("Dependencies\logo.png"))
    
    widget.show()
    try:
        sys.exit(app.exec())
    except:
        print("Exiting...")