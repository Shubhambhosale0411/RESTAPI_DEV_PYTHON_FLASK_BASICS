import json
import mysql.connector
from flask import make_response
class user_model():
    def __init__(self):
        try:
        #connection establishment code
            self.con=mysql.connector.connect(host="localhost",user="root",password="Shubham@123",database="flask_tutorial")
            self.con.autocommit=True
            self.cur=self.con.cursor(dictionary=True)
            print("connection sucessful")
        except:
            print("some error")
    def user_getall_model(self):
        #connection establishment  not everytime so we use constructor
        #query execution code
        self.cur.execute("SELECT * FROM users")
        #result of above cur.execute value is stored using fetchall command
        result=self.cur.fetchall()
        if len(result)>0:
            #return {"Payload":result}  #json prettfie
            #return json.dumps(result) #html/text normal format
            return make_response({"Payload":result},200)
        else:
            return "no data found"
        
    def user_addone_model(self,data):
        self.cur.execute(f"INSERT INTO users(name, email, phone, role, password) VALUES('{data['name']}', '{data['email']}', '{data['phone']}', '{data['role']}', '{data['password']}')")
        print(data)
        #print(data["email"])
        return "user created sucessfully"
        
    def user_update_model(self,data):
        self.cur.execute(f"UPDATE users SET name='{data['name']}', email='{data['email']}', phone='{data['phone']}' WHERE id={data['id']}")
        if self.cur.rowcount>0:
            return "user updated sucessfully"
        else:
            return "nothing updated"
        
    def user_delete_model(self,id):
        self.cur.execute(f"DELETE FROM users WHERE id={id}")
        if self.cur.rowcount>0:
            return "user deleted sucessfully"
        else:
            return "nothing deleted"
        

    def user_patch_model(self,data,id):
        qry="UPDATE users SET "
        #print(data)
        for key in data:
            qry= qry + f"{key}='{data[key]}',"
        #print(qry)
        qry= qry[:-1]+ f" WHERE id={id}"
        #qry+=f" WHERE id={id}"
        #UPDATE users SET col=name,col=name WHERE id={id}
        #return qry
        self.cur.execute(qry)
        
        if self.cur.rowcount>0:
            return "user updated sucessfully"
        else:
            return "nothing updated"
        
    def user_pagination_model(self,limit,page):
        limit=int(limit)
        page=int(page)
        start=(page*limit)-limit
        qry=f"SELECT * FROM users LIMIT {start}, {limit}"
        self.cur.execute(qry)
        
        result=self.cur.fetchall()
        if len(result)>0:
            res=make_response({"Payload":result,"page_no":page,"limit":limit},200)
            return res
        else:
            return make_response({"message":"no data found"},204)
        
    def user_upload_avatar_model(self,uid,filepath):
        self.cur.execute(f"UPDATE users SET avatar='{filepath}' WHERE id={uid}")
        if self.cur.rowcount>0:
            return make_response({"message":"avtar uploaded"},201)
        else:
            return make_response({"message":"not uploaded"},202)
        