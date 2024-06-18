import csv 
import random
import datetime

class book:
    all=[]
    def __init__(self,name_book,auther_book,number_page,cat,price,quant,rel_date):
            self.name_book=name_book
            self.auther_book=auther_book
            self.number_page=number_page
            self.cat=cat
            self.price=price
            self.quant=quant
            self.rel_date=rel_date
            self.id_book=self.id_maker()
            self.all=[]
            book.all.append(self)

    @classmethod
    def remp_book_file(cls):
        
        with open("data_book.csv","a") as f:
            writer=csv.writer(f)
            #writer.writerow(["ID_book","book_name","Auther","Page_number","category","Price","release_date"])
            for i in all:
                writer.writerow([i.id_book,i.name_book,i.auther_book,i.number_page,i.cat,i.price,i.quant,i.rel_date])
        f.close()


    @classmethod
    def print_books_from_csv(cls):
        with open("data_book.csv", "r") as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                 print("|".join(row))
        f.close()
    
    @classmethod 
    def update_or_add_book(cls,name_book,auther_book,number_page,cat,price,quant,rel_date):
        if cls.is_book_in_lib(name_book):
            with open("data_book.csv","r", newline='') as f:
                read = csv.reader(f)
                rows = list(read)
            with open("data_book.csv","w", newline='') as f:
                write = csv.writer(f)
                for row in rows:
                    if name_book==row[1]:
                        row[6]=str(int(row[6])+1)
                        write.writerow(row)
                    else:
                        write.writerow(row)
            print("book ("+name_book+") has been updated")
            f.close()
        else:
            cls.id_book=cls.id_maker()
            with open("data_book.csv","a", newline='') as f:
                writer=csv.writer(f)
                #writer.writerow(["ID_book","book_name","Auther","Page_number","category","Price","release_date"])
                writer.writerow([cls.id_book, name_book, auther_book, number_page, cat, price, quant, rel_date])
            print("book ("+name_book+") has been added")
            f.close()


    @staticmethod
    def is_book_in_lib(name_book):
        with open("data_book.csv", "r") as f:
            reader = csv.reader(f)
            print(reader)
            for row in reader:
                if name_book==row[1]:
                    return True
            return False
        f.close()

    def __repr__(self):
        return f"{self.name_book}|{self.auther_book}|{self.number_page}|{self.cat}|{self.price}|{self.quant}|{self.rel_date}|{self.id_book}"

    
    
    def id_maker(self):
        #craete id book
        #the first letter of the (book,auther,np)+nbline(two numbers)
        name= self.name_book[:2]
        auth=self.auther_book[:2]
        nb=str(self.number_page)
        nb=nb[:2]
        characters="#$&"
        x=random.choice(characters)
        rel_date=str(self.rel_date)
        dat=rel_date[:2]+rel_date[8:]
        return f"{name}{auth}{x}{nb}{dat}"
    
    #crate method from list to atrubit 
         
   
                    
#create a book
    #book1=book("cooking book","philps",1100,"cook",5.5,10,datetime.date.today())

#printing the book atribute
    #book1__repr__()

#adding it to csv file
    #book.remp_()

#verifying if the book is already in the csv file
    #print(book1.is_book_in_lib())
book.update_or_add_book("cooking book","philps",1100,"cook",5.5,10,datetime.date.today())