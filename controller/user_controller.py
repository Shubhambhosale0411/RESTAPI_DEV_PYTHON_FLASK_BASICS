from app import app
from model.user_model import user_model
from flask import request,send_file
from datetime import datetime
obj=user_model()
#read
@app.route('/user/getall')
def user_getall_controller():
    return obj.user_getall_model()
#create
@app.route('/user/addone',methods=["POST"])
def user_addone_controller():
    # in post we have request.form
    #print(request.form)
    return obj.user_addone_model(request.form)
#update
@app.route('/user/update',methods=["PUT"])
def user_update_controller():
    # in post we have request.form
    #print(request.form)
    return obj.user_update_model(request.form)

#delete
@app.route('/user/delete/<id>',methods=["DELETE"])
def user_delete_controller(id):
    # in post we have request.form
    #print(request.form)
    return obj.user_delete_model(id)

#patch
@app.route('/user/patch/<id>',methods=["PATCH"])
def user_patch_controller(id):
    # in post we have request.form
    return obj.user_patch_model(request.form,id)

#pagination
@app.route('/user/getall/limit/<limit>/page/<page>',methods=["GET"])
def user_pagination_controller(limit,page):
    # in post we have request.form
    return obj.user_pagination_model(limit,page)


#upload
#upload file from postman to server
#save file in filesystem with unique filename
#upload filepath in database 
@app.route('/user/<uid>/upload/avatar',methods=["PUT"])
def user_upload_avatar_controller(uid):
    #print(request.files)
    file=request.files['avatar']
    #file.save(f"uploads/{file.filename}")  #here filename is id_photo

    #name
    uniquefilename=str(datetime.now().timestamp()).replace(",","")
    #filename
    filenamesplit=file.filename.split(".")
    #extension
    ext=filenamesplit[-1]
    file.save(f"uploads/{uniquefilename}.{ext}")
    finalpath=f"uploads/{uniquefilename}.{ext}"
    return obj.user_upload_avatar_model(uid,finalpath)


@app.route('/uploads/<filename>')
def user_getavatar_controller(filename):
    return send_file(f"uploads/{filename}")