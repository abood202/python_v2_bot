from info import *
from btn import manage_btn

#*اختيار الجنس تم
#*ازرار عادية وازرار مضمنة

#!عمل ازرار للكتب
#!عمل ازرار للخاص
#!عمل ازرار

#?عندما ينضم الاعضاء وغيرو (تم)
#?للتعامل مع الازرار المضمنة لاختيار الجنس اثناء الانضمام
def cback(call):
    """
    عندما ينضم الاعضاء

    للتعامل مع الازرار المضمنة لاختيار الجنس اثناء الانضمام
    """
    user_id = call.from_user.id
    full_name = call.from_user.full_name
    call_text = call.data
    message = call.message
    chat_id = message.chat.id
    message_id = message.message_id
    gender_list = ["Male","Female"]
    with open("backend/Chat_Data.json", 'r') as f:
        data = json.load(f)

    gender = data["Groups"][f"{chat_id}"]["chat_member"][0][f"{user_id}"]["Gender"]
    admins = list(data["Groups"][f"{chat_id}"]["Admins"])
    moderators = list(data["Groups"][f"{chat_id}"]["Moderators"])

    if gender in gender_list:
        pass

    elif call_text == "ولد":
        select_gender = {
            "Gender": "Male"
        }
        data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(select_gender)
        with open('backend/Chat_Data.json', 'w') as f:
            json.dump(data, f)

        bot.restrict_chat_member(chat_id,user_id,
                can_send_messages=True,
                can_invite_users=True)
        bot.delete_message(chat_id,message_id)
    
    elif call_text == "بنت":
        select_gender = {
            "Gender": "Female"
        }
        data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(select_gender)
        with open('backend/Chat_Data.json', 'w') as f:
            json.dump(data, f)
     
        bot.restrict_chat_member(chat_id,user_id,
        can_send_messages=True,
        can_invite_users=True)

        bot.delete_message(chat_id,message_id)

    if call_text == "حذف":
        if user_id in (admins + moderators):
            bot.delete_message(chat_id,message_id)

#?زر اختيار الجنس
def gender_select(message,chat_id,message_text,user_id,gender):
    """
    زر اختيار الجنس
    
    ازار لوحة المفاتيح
    """
    boy_girl =['ولد','بنت']
    gender_list = ["Male","Female"]
    full_name = message.from_user.full_name
    
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True,is_persistent=True, one_time_keyboard =True,selective=True)
    btn1=types.KeyboardButton('ولد')
    btn2=types.KeyboardButton('بنت')
    markup.add(btn1,btn2)

    remove_keybord = types.ReplyKeyboardRemove(selective=None)
    if gender in gender_list:
        pass
    else:
        if message_text in boy_girl:
            with open("backend/Chat_Data.json", 'r') as f:
                data = json.load(f)

            if message_text == "ولد":
                bot.send_message(chat_id,"حسنا مرحبا بك",reply_markup =remove_keybord)
                select_gender = {
                    "Gender": "Male"
                }
                data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(select_gender)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)
                
            elif message_text == "بنت":
                bot.send_message(chat_id,"حسنا مرحبا بك",reply_markup = remove_keybord)
                select_gender = {
                    "Gender": "Female"
                }
                data['Groups'][f"{chat_id}"]["chat_member"][0][f"{user_id}"].update(select_gender)
                with open('backend/Chat_Data.json', 'w') as f:
                    json.dump(data, f)

        elif message_text not in boy_girl:
            m = f"[{full_name}](tg://user?id={user_id})"
            bot.reply_to(message,f"({m}) ~ قم بالاختيار",parse_mode="markdown", reply_markup=markup)
 



#?الجزء الخاص بالكتب
def start(message,user_id,msg):
    with open(f"user_books/{user_id}.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    books = data["books"]
    btns = []
    small_list = []
    count = 1

    for i in books:
        if count == 10:
            btns.append(small_list)
            small_list = []
            count = 1
        count+=1
        small_list.append(i)
    
    btns.append(small_list)
    send_buttons_page(message.chat.id, 1,message,btns,books)
    bot.delete_message(chat_id=message.chat.id,message_id=msg)
    
def select_book(call):
    data = call.data
    old_user_id = call.message.json["reply_to_message"]["from"]["id"]
    new_user_id = call.from_user.id
    full_name = call.from_user.full_name
    chat_id = call.message.json["chat"]["id"]
    message_type = call.message.content_type
    message_id = call.message.id
    chat_type = call.message.chat.type

    if chat_type == "supergroup":
        with open("backend/Chat_Data.json", 'r') as f:
            data_chat = json.load(f)
        Moderators_list = list(data_chat['Groups'][f'{chat_id}']['Moderators'])
        Admin_list = list(data_chat['Groups'][f'{chat_id}']['Admins'])
        All_admin = Admin_list + Moderators_list

        try:
            # print(old_user_id,new_user_id)
            if (old_user_id == new_user_id) or (new_user_id in All_admin):
                with open(f"user_books/{old_user_id}.json",'r',encoding='utf-8') as f:
                    data_book = json.load(f)
                books = data_book["books"]
                #?دي عشان يعمل للمستغدم اعادة توجية بالملف
                id_message = data_book["id message"]
                btns = []
                small_list = []
                count = 1
                for i in books:
                    if count == 10:
                        btns.append(small_list)
                        small_list = []
                        count = 1
                    count+=1
                    small_list.append(i)
                
                btns.append(small_list)

                if '_' in data:
                    data = call.data.split('_')
                    if data[1].isdigit():
                        page_number = int(data[1])            
                        if data[0] == 'prev':
                            page_number -= 1
                            edit_buttons_page(call.message.chat.id, call.message.message_id, page_number,btns,books)
                        elif data[0] == 'next':
                            page_number += 1
                            edit_buttons_page(call.message.chat.id, call.message.message_id, page_number,btns,books)
                    
                    elif data[1] == "qut":
                        bot.send_message(chat_id=chat_id,text=f"([{full_name}](tg://user?id={new_user_id}))\nليس لدي هذا الكتاب انتظر احد المشرفين",parse_mode="markdown",reply_to_message_id=id_message)

                else:
                    try:
                        for i in books:
                            if int(data) == books[i]:
                                id_book = books[i]
                                break
                        bot.copy_message(chat_id=chat_id,from_chat_id="-1001939329726",message_id=id_book)
                        bot.send_message(chat_id=chat_id,text=".",reply_to_message_id=id_message)
                        bot.delete_message(chat_id=chat_id,message_id=message_id)

                    except:
                        bot.delete_message(chat_id=chat_id,message_id=message_id)

            else:
                message_user = bot.send_message(chat_id=chat_id,text=f"[{full_name}](tg://user?id={old_user_id}) هذا ليس طلبك اطلب الكتاب بنفسك",parse_mode="markdown")
                remove_message(chat_id, message_user.id, 20)

        except:
            bot.delete_message(chat_id=chat_id,message_id=message_id)

    elif chat_type=="private":
        with open(f"Admins_bot/{new_user_id}.json",'r',encoding='utf-8') as f:
            data_group = json.load(f)
        Groups = data_group["Groups"]
        new_data = manage_btn(call,Groups,data,new_user_id,chat_id,message_id)

        return new_data

        
def delete_message(chat_id, message_id, delay):
    time.sleep(delay)  # انتظر الفترة المحددة
    try:
        bot.delete_message(chat_id, message_id)  # حذف الرسالة
    except:
        pass

# الاستدعاء لحذف الرسالة بعد فترة محددة
def remove_message(chat_id, message_id, delay):
    thread = threading.Thread(target=delete_message, args=(chat_id, message_id, delay))
    thread.start()

def send_buttons_page(chat_id, page_number, message,btns,books):
    markup = types.InlineKeyboardMarkup(row_width=2)  # تحديد عرض الصف ليكون 2 زر في كل صف
    if len(btns) == 1:
        buttons = btns[page_number - 1]
        for button_text in buttons:
            id_book = books[button_text]
            markup.add(types.InlineKeyboardButton(button_text, callback_data=f'{id_book}'))
        message_user = bot.reply_to(message=message, text=f'الصفحة {page_number}', reply_markup=markup)
        message_id = message_user.id
        user_id=message.from_user.id
        remove_message(chat_id, message_id, 120)

    else:
        buttons = btns[page_number - 1]
        for button_text in buttons:
            id_book = books[button_text]
            markup.add(types.InlineKeyboardButton(button_text, callback_data=f'{id_book}'))
        if page_number > 1:
            markup.add(types.InlineKeyboardButton('التالية', callback_data=f'next_{page_number}'),
                    types.InlineKeyboardButton('السابقة', callback_data=f'prev_{page_number}'))
        if page_number == 1:
            markup.add(types.InlineKeyboardButton('التالية', callback_data=f'next_{page_number}'))
        message_user =  bot.reply_to(message=message, text=f'الصفحة {page_number}', reply_markup=markup)
        message_id = message_user.id
        # استدعاء الدالة لحذف الرسالة بعد 5 دقائق
        remove_message(chat_id, message_id, 120)

def edit_buttons_page(chat_id, message_id, page_number,btns,books):
    markup = types.InlineKeyboardMarkup(row_width=2)  # تحديد عرض الصف ليكون 2 زر في كل صف
    if len(btns) == 1:
        buttons = btns[page_number - 1]
        for button_text in buttons:
            id_book = books[button_text]
            markup.add(types.InlineKeyboardButton(button_text, callback_data=f'{id_book}'))
        bot.edit_message_text(f'الصفحة {page_number}', chat_id, message_id, reply_markup=markup)
    elif page_number < len(btns):
        buttons = btns[page_number - 1]
        for button_text in buttons:
            id_book = books[button_text]
            markup.add(types.InlineKeyboardButton(button_text, callback_data=f'{id_book}'))
        if page_number > 1:
            markup.add(types.InlineKeyboardButton('التالية', callback_data=f'next_{page_number}')
                    ,types.InlineKeyboardButton('السابقة', callback_data=f'prev_{page_number}'))
        if page_number == 1:
            markup.add(types.InlineKeyboardButton('التالية', callback_data=f'next_{page_number}'))
        bot.edit_message_text(f'الصفحة {page_number}', chat_id, message_id, reply_markup=markup)
    else:
        buttons = btns[page_number - 1]
        for button_text in buttons:
            id_book = books[button_text]
            markup.add(types.InlineKeyboardButton(button_text, callback_data=f'{id_book}'))
        markup.add(types.InlineKeyboardButton('لم اجد ما اريد', callback_data=f'x_qut'),
                   types.InlineKeyboardButton('السابقة', callback_data=f'prev_{page_number}'))
        bot.edit_message_text(f'الصفحة {page_number}', chat_id, message_id, reply_markup=markup)
