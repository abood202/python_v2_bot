from info import *
from call_back import start
#?هنا التعامل مع الكتب والازرار

def filter_books():
    
    with open("backend/book_name.json",'r',encoding='utf-8') as f:
        data = json.load(f)
    book_s = data["book"]

    list_books = list(book_s.keys())
    lst=[]

    user_books = {
        "books":{}
    }

    for x in list_books:
        i = x
        i = filter_txt(i)
        lst.append(i)
        if i in (user_books["books"]):
            new_book = {
                f"(1){i}":book_s[x]
            }            
            user_books["books"].update(new_book)
        else:
            new_book = {
                i:book_s[x]
            }            
            user_books["books"].update(new_book)

    with open("backend/BOOK.json","w")as f:
        json.dump(user_books, f, indent=4)



def get_book(text_messge,user_id,chat_id,message,full_name,Send_book):

    msg = bot.reply_to(message=message,text=f"[{full_name}](tg://user?id={user_id}) إنتظر جاري البحث...",parse_mode="markdown")
    msg_to_del= msg.id
    
    filter_books()
    
    with open("backend/BOOK.json",'r',encoding='utf-8') as f:
        data = json.load(f)

    books = data["books"]

    list_book = list(books.keys())
    lst=[]
    for i in list_book:
        i = filter_txt(i)
        lst.append(i)
    
    # print(books.keys())
    user_books = {"books":{},
                "id message":0
                }    

    # قائمة لتخزين الكتب مع درجة التشابه
    priority_books = []

    # حساب درجة التشابه لكل كتاب
    for book in lst:
        similarity_score = jaccard_similarity(text_messge, book)
        priority_books.append((book, similarity_score))

    # ترتيب القائمة حسب درجة التشابه
    priority_books.sort(key=lambda x: x[1], reverse=True)

    # عرض أكثر الكتب تشابهًا
    most_similar_books = [book for book, score in priority_books if score > 0]

    # print("أكثر الكتب تشابهًا:")
    for book in most_similar_books:
        new_book = {
            book:books[book]
        }            
        user_books["books"].update(new_book)

    user_books["id message"] = message.id

    books_user = user_books["books"]

    if len(books_user) > 0:
        with open(f"user_books/{user_id}.json", "w",encoding="utf-8") as f:
            json.dump(user_books, f, ensure_ascii=False, indent=4)
        
        start(message,user_id,msg_to_del)
    
    else:
        bot.reply_to(message,text=f"([{full_name}](tg://user?id={user_id}))\nليس لدي هذا الكتاب انتظر احد المشرفين",parse_mode="markdown")
        bot.delete_message(chat_id=chat_id,message_id=msg_to_del)

#?تصفية الجملة
def filter_txt(txt):
    if "_" in txt:
        txt = txt.replace("_"," ")
    if "-" in txt:
        txt = txt.replace("-"," ")    
    if "أ" in txt:
        txt = txt.replace("أ","ا")
    if "إ" in txt:
        txt = txt.replace("إ","ا")
    if "آ" in txt:
        txt = txt.replace("آ","ا")
    if "ة" in txt:
        txt = txt.replace("ة","ه")
    if "ى" in txt:
        txt = txt.replace("ى","ي")
    if "،" in txt:
        txt = txt.replace("،"," ")
    if ".pdf" in txt:
        txt = txt.replace(".pdf","")
    if ".PDF" in txt:
        txt = txt.replace(".PDF","")
    if ".Pdf" in txt:
        txt = txt.replace(".Pdf","")
    txt = " ".join(txt.split())
    return txt

#الاكثر تشابه
# دالة لحساب مقياس Jaccard بين جملتين
def jaccard_similarity(query, book):
    query_tokens = set(word_tokenize(query.lower()))
    book_tokens = set(word_tokenize(book.lower()))
    intersection = query_tokens.intersection(book_tokens)
    union = query_tokens.union(book_tokens)
    return len(intersection) / len(union)
