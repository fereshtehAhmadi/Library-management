from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from loan.models import LoanModel, DebtModel
from accounts.models import CustomUserModel
from books.models import Book, BookRequest, Author, Categorie, Publishers
from extra.models import BookMarck, LikeBook, Comment, LikeComment
from faker import Faker
from random import randint, choice


fake = Faker()


def create_debt(num=10):
    return [DebtModel.objects.create(amount=0) for _ in range(num)]


def create_publishers(num=10):
    return [
        Publishers.objects.create(
            name=fake.name(),
        )
        for _ in range(num)
    ]


def create_category(num=20):
    cat_list = ['novel', 'adventure', 'mystic', 'romance', 'crime', 'joke', ]

    cat_obj_list = []
    for _ in range(num):
        random_category = choice(cat_list)
        cat_list.remove(random_category)
        cat_obj_list.append(CategoryModel.objects.create(category=random_category))
    else:
        return cat_obj_list


def create_author(num=20):
    return [Author.objects.create(name=fake.name(), description=fake.text()) for _ in range(num)]


def create_user(num=5, staff=False):
    return [
        User.objects.create_user(
            username=fake.unique.first_name(),
            password='passwd@2',
            is_staff=staff,
        )
    ]


def create_custom_user(users_list, debt_list):
    national_code_list = [
        '0029382764', '0093847365',
        '0028493939', '0028484839',
        '0028383839', '0024833939',
        '0024949393', '0024032220',
    ]
    return [
        CustomUserModel.objects.create(
            age=randint(18, 35),
            phone= +12125553648,
            gender=choice(['M', 'F']),
            address=fake.address(),
            national_code=choice(national_code_list),
            user=user_obj,
        )
        for user_obj in users_list
    ]


def create_loan(num=5):
    LoanModel.objects.create(
        user=user_obj,
        book=book_obj,
        status=choice(['S', 'T', 'R', 'C']),
    )
    

def create_comment(num=20):
    Comment.objects.create(
        user=user_obj,
        book=book_obj,
        title=fake.name(),
        content=fake.text(),
    )
    
def create_like_book(num=5):
    LikeBook(
        user=user_obj,
        book=book_obj,
        vote=choice(['L', 'D']),
    )
    


class Command(BaseCommand):
    help = 'Populates database with dummy-data.'

    def handle(self, *args, **kwargs):
        debt_list = create_debt()
        pub_list = create_publishers()
        cate_list = create_category()
        author_list = create_author()
        user_list = create_user()
        staff_list = create_user(staff=True)
        custom_user_list = create_custom_user(user_list.extend(staff_list), debt_list)
        loan_list = create_loan()
        comment_list = create_comment()
        # book_list = create_book()
        # bookmark_list = create_bookmark()

        self.stdout.write("Database has been populated successfully.")