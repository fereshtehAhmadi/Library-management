from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from loan.models import LoanModel, DebtModel
from accounts.models import CustomUserModel
from books.models import Book, BookRequest, Author, Categorie, Publishers
from extra.models import BookMarck, LikeBook, Comment, LikeComment
from faker import Faker
from random import randint, choice


fake = Faker()

def create_user(num=5, staff=False):
    return [
        User.objects.create_user(
            username=fake.unique.first_name(),
            first_name = fake.name(),
            last_name = fake.name(),
            email = fake.name() + '@gmail.com',
            password = 'passwd@2',
            is_staff = staff,
        )
    ]


def create_custom_user(users_list):
    national_code_list = [
        '0029382764', '0093847365',
        '0028493939', '0028484839',
        '0028383839', '0024833939',
        '0024949393', '0024032220',
    ]
    return [
        CustomUserModel.objects.create(
            birthday=fake.date(),
            phone= '09123456789',
            gender=choice(['M', 'F']),
            address=fake.address(),
            national_code=choice(national_code_list),
            user=user_obj,
            condition= True,
        )
        for user_obj in users_list
    ]
    
    
def create_publishers(num=10):
    return [
        Publishers.objects.create(
            name=fake.name(),
        )
        for _ in range(num)
    ]


def create_category(num=6):
    cat_list = ['novel', 'adventure', 'mystic', 'romance', 'crime', 'joke', ]

    cat_obj_list = []
    for _ in range(num):
        random_category = choice(cat_list)
        cat_list.remove(random_category)
        cat_obj_list.append(Categorie.objects.create(category=random_category))
    else:
        return cat_obj_list


def create_author(num=10):
    return [Author.objects.create(name=fake.name(), description=fake.text()) for _ in range(num)]



def create_book(custom_user_list, pub_list, cate_list, author_list, num=20):
    for _ in range(num):
        book_obj = Book.objects.create(
            name = fake.name(),
            description = fake.text(),
            translator = fake.name(),
            user = choice(custom_user_list),
            publishers = choice(pub_list)
        )
        book_obj.author.add(choice(author_list))
        book_obj.category.add(choice(cate_list))
        book_obj.save()
    return book_obj
    
    

def create_comment(custom_user_list,num=20):
    for _ in range(num):
        book_list = Book.objects.all()
        comment_obj = Comment.objects.create(
            user = choice(custom_user_list),
            book = choice(book_list),
            title = fake.name(),
            content = fake.text(),
        )
    return comment_obj
  
  

def create_like_book(user_list, num=20):
    for _ in range(num):
        book_list = Book.objects.all()
        like_book_obj = LikeBook.objects.create(
            user = choice(user_list),
            book = choice(book_list),
            vote = choice(['L', 'D']),
        )
    return like_book_obj

    
def create_loan(custom_user_list, num=5):
    for _ in range(num):
        book_list = Book.objects.all()
        loan_obj = LoanModel.objects.create(
            user = choice(custom_user_list),
            book = choice(book_list),
            status = choice(['S', 'T', 'R']),
        )
    return loan_obj


def create_debt():
    loan_obj = LoanModel.objects.filter(status='T')
    for loan in loan_obj:
        debt_obj = DebtModel.objects.create(
            loan = loan,
            user = loan.user,
            book = loan.book,
            amount = 2000,
        )
    return debt_obj



def create_book_request(custom_user_list, num=5):
    BookRequest.objects.create(
        name = fake.name(),
        author =  fake.name(),
        translator = fake.name(),
        publisher = fake.name(),
        user = choice(custom_user_list),
    )
    


class Command(BaseCommand):
    help = 'Populates database with dummy-data.'

    def handle(self, *args, **kwargs):
        user_list = create_user(5, staff=False)
        staff_list = create_user(5, staff=True)
        custom_user_list = create_custom_user(staff_list)
        pub_list = create_publishers()
        cate_list = create_category()
        author_list = create_author()
        book_list = create_book(custom_user_list, pub_list, cate_list, author_list, 20)
        comment_list = create_comment(custom_user_list, 30)
        like_book_list = create_like_book(user_list, 50)
        loan_list = create_loan(custom_user_list, 5)
        debt_list = create_debt()
        book_request_list = create_book_request(custom_user_list, 5)

        self.stdout.write("Database has been populated successfully.")
        
# python manage.py populate_db