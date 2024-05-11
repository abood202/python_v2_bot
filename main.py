from info import *
from Add_New_member import addmember
from call_back import select_book
from message_handel import handel_message,private_message
from command import bot_command
import shutil


shutil.rmtree("__pycache__",ignore_errors=True)

#?اوامر البوت
@bot.message_handler(commands=['start','help'])
def send_command(message):
    shutil.rmtree("__pycache__",ignore_errors=True)

    chat_type = message.chat.type # supergroup , private #
    chat_id = message.chat.id
    if chat_type == "private":
        bot_command(message)

with open("backend/Chat_Data.json", 'r') as f:
    data_groups_ = json.load(f)
with open("backend/Users_Data.json", 'r') as f:
    data_private_ = json.load(f)

#?للتعامل مع الملفات والنصوص
@bot.message_handler(content_types=['document','text'])
def send_text_file(message): 
    shutil.rmtree("__pycache__",ignore_errors=True)
    chat_type = message.chat.type #supergroup,private,channel
    user_id = message.from_user.id
    chat_id = message.chat.id
    if chat_type == "supergroup":
        x = bot.send_message(chat_id,".")
        print(x)
        global data_groups_
        global data_private_
        dat,data_private = handel_message(message,data_groups_,data_private_)
        data_groups_.update(dat)
        data_private_.update(data_private)
        # # حفظ التحديثات إذا لزم الأمر
        with open("backend/Chat_Data.json", 'w') as f:
            json.dump(data_groups_, f)
        with open("backend/Users_Data.json", 'w') as f:
            json.dump(data_private_, f)

    elif chat_type == "private":
        private_message(message)

#?للتعامل مع الاعضاء المنضمين والمغادرين
@bot.chat_member_handler()
def handleUserUpdates(message:types.ChatMemberUpdated):
    shutil.rmtree("__pycache__",ignore_errors=True)

    chat_type = message.chat.type    
    if chat_type == "supergroup":        
        addmember(message)

#?اذا تم تعديل الرسالة
@bot.edited_message_handler(func=lambda message: True,content_types=['document','text'])
def edited_message(message):
    shutil.rmtree("__pycache__",ignore_errors=True)
    global data_groups_
    chat_type = message.chat.type
    if chat_type == "supergroup":
        global data_groups_
        global data_private_
        dat,data_private = handel_message(message,data_groups_,data_private_)
        data_groups_.update(dat)
        data_private_.update(data_private)
        # # حفظ التحديثات إذا لزم الأمر
        with open("backend/Chat_Data.json", 'w') as f:
            json.dump(data_groups_, f)
        with open("backend/Users_Data.json", 'w') as f:
            json.dump(data_private_, f)

#?البوت يغادر المجموعة المختلفة
@bot.my_chat_member_handler()
def leave(message:types.ChatMemberUpdated):
    shutil.rmtree("__pycache__",ignore_errors=True)

    update = message.new_chat_member
    can_delete = update.can_delete_messages#?حذف الرسائل
    can_restrict = update.can_restrict_members#?تقييد الاعضاء
    can_change = update.can_change_info#?يمكن تغيير المعلومات
    can_invite = update.can_invite_users#?يمكن دعوة المستخدمين
    can_manage = update.can_manage_chat#?يمكن ادارة الدردشة
    can_promote = update.can_promote_members#?ترقية الاعضاء

    try:
        if update.status !="administrator":        
            bot.send_message(message.chat.id,"لايمكنني البقاء كعضو في المجموعة")
            bot.leave_chat(message.chat.id)
        else:            
            if can_delete and can_restrict and can_change and can_invite and can_manage:
                pass
            else:
                bot.send_message(message.chat.id,"""
تأكد من اعطائي الصلاحيات المناسبة عند اضافتي
1)- إدارة المجموعة
2)- حذف الرسائل
3)- دعوة مستخدم
4)- حظر مستخدم
""")
                bot.leave_chat(message.chat.id)
    except:
        pass

#?تسجيل اي كتاب جديد
@bot.channel_post_handler(content_types=["document"])
def file_chanel(message):
    shutil.rmtree("__pycache__",ignore_errors=True)

    chat_id = message.chat.id
    if chat_id == -1001939329726:
        if message.document:
            with open("backend/book_name.json",'r',encoding='utf-8') as f:
                data = json.load(f)
            books = list(data["book"])
            file_name = message.document.file_name
            message_id = message.id

            if file_name in books:
                pass
            else:
                new_data = {
                    file_name:message_id
                }
                data['book'].update(new_data)
                with open("backend/book_name.json", 'w',encoding="utf-8") as f:
                    json.dump(data, f,indent=4)

#?ازرار اختيار
@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    shutil.rmtree("__pycache__",ignore_errors=True)
    global data_groups_ 
    dat = select_book(call)
    data_groups_.update(dat)
    # # حفظ التحديثات إذا لزم الأمر
    with open("backend/Chat_Data.json", 'w') as f:
        json.dump(data_groups_, f)


print("Bot is started")
bot.infinity_polling()
