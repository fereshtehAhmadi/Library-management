from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from loan.models import LoanModel, DebtModel
from accounts.models import CustomUserModel
from books.models import Book, BookRequest, Author, Categorie, Publishers
from extra.models import BookMarck, LikeBook, Comment, LikeComment
from faker import Faker
from random import randint, choice

# fake = Faker()
#
#
# def create_publishers(num=6):
#     if num:
#         for _ in num:
#             Publishers.objects.get_or_create(name=fake.name())
#     else:
#         for _ in range(5):
#             Publishers.objects.get_or_create(name=fake.name())
#
#
# def create_author(num=None):
#     if num:
#         for _ in num:
#             Author.objects.get_or_create(name=fake.name(), desc=fake.text())
#     else:
#         for _ in range(10):
#             Author.objects.get_or_create(name=fake.name(), desc=fake.text())
#
#
# def create_debt(num=None):
#     if num:
#         for _ in num:
#             DebtModel.objects.get_or_create(amount=0)
#     else:
#         for _ in range(10):
#             DebtModel.objects.get_or_create(amount=0)
#
#
# def create_user(num=None):
#     phone_num_list = [
#         '09013255112', '09921476367',
#         '09303294928', '09383724948',
#         '09928372849', '09123394928',
#     ]
#     gender_list = [
#         'M', 'F',
#     ]
#     national_code_list = [
#         '0024367011', '0024756374',
#         '0024582738', '0024757483',
#         '0024857388', '0024632619',
#     ]
#
#     if num:
#         for iteration_num in num:
#             if iteration_num < num // 2:
#                 user_obj = User.objects.create_user(
#                     username=fake.unique.first_name(),
#                     password='passwd@2',
#                     is_staff=True,
#                 )
#                 CustomUserModel.objects.create(
#                     age=randint(10, 31),
#                     phone_number=fake.sentence(ext_word_list=phone_num_list),
#                     gender=choice(gender_list),
#                     address=fake.address(),
#                     national_code=choice(national_code_list),
#                     user=user_obj,
#                 )
#             else:
#                 user_obj = User.objects.create_user(
#                     username=fake.unique.first_name(),
#                     password='passwd@2',
#                 )
#                 CustomUserModel.objects.create(
#                     user=user_obj,
#                     age=randint(10, 31),
#                     phone_number=fake.sentence(ext_word_list=phone_num_list),
#                     gender=choice(gender_list),
#                     address=fake.address(),
#                     national_code=choice(national_code_list),
#                 )
#
#     else:
#         for iteration_num in range(10):
#             if iteration_num < 5:
#                 user_obj = User.objects.create_user(
#                     username=fake.unique.first_name(),
#                     password='passwd@2',
#                 )
#                 CustomUserModel.objects.create(
#                     user=user_obj,
#                     age=randint(10, 31),
#                     phone_number=fake.sentence(ext_word_list=phone_num_list),
#                     gender=choice(gender_list),
#                     address=fake.address(),
#                     national_code=choice(national_code_list),
#                 )
#             else:
#                 user_obj = User.objects.create_user(
#                     username=fake.unique.first_name(),
#                     password='passwd@2',
#                     is_staff=True,
#                 )
#                 CustomUserModel.objects.create(
#                     age=randint(10, 31),
#                     phone_number=fake.sentence(ext_word_list=phone_num_list),
#                     gender=choice(gender_list),
#                     address=fake.address(),
#                     national_code=choice(national_code_list),
#                     user=user_obj,
#                 )
#
#
# def create_category(num=None):
#     categories = [
#         'novel', 'action', 'adventure',
#         'classic', 'comic', 'graphic',
#         'detective', 'mystery', 'fantasy',
#         'horror', 'historical', 'fiction',
#         'sci-fi', 'romance', 'thrillers',
#         'essay', 'memoir', 'poetry',
#         'self-help', 'self-development',
#     ]
#     if num:
#         while True:
#             random_category_name = choice(categories)
#             if not CategoryModel.objects.filter(name=random_category_name).exists():
#                 CategoryModel.objects.create(name=random_category_name)
#
#             if CategoryModel.objects.all().count() == num:
#                 break
#
#     else:
#         while True:
#             random_category_name = choice(categories)
#             if not CategoryModel.objects.filter(name=random_category_name).exists():
#                 CategoryModel.objects.create(name=random_category_name)
#
#             if CategoryModel.objects.all().count() == 10:
#                 break
#
#
# def create_book(num=None):
#     pass
#
#
# def create_bookmark(num=None):
#     pass
#
#
# def create_comment(num=None):
#     pass
#
#
# def create_like(num=None):
#     pass
#
#
# def create_loan(num=None):
#     pass
#

# # publisher
# publisher_material = {
#     'afagh': 'Tehran Province, Tehran, Karabakh, Cobra',
#     'yas': 'Tehran Province, Tehran, khiabane fakhre razi. k. fatehi darian',
#     'al yasin': 'Tehran, Tehran Province, Eslamshahr, Sayyad-e-Shirazi, University bus stop',
# }
# pub_objects = [PublisherModel.objects.get_or_create(name=pub, address=pub_address) for pub, pub_address in
#                publisher_material.items()]
# # author
# author_material = {
#     ''
# }
# # debt
# # user
# # category
# # custom user
# # book
# # loan
# users_info = {'user_1': 'passwd@2', 'user_2': 'passwd@2', 'user_3': 'passwd@2'}
# user_objects = (
#     User.objects.create_user(username=username, password=password)
#     for username, password in users_info.items()
# )
#
# [CustomUserModel.objects.get_or_create(user=user, age=randint(20, 45), ) for user in user_objects]
###################
# author_obj = AuthorModel.objects.create(
#     name='authe_1',
#     desc='desc_1',
# )
# user_obj = User.objects.create_user(username='user_1', password='passwd@2')
# custom_user_obj = CustomUserModel.objects.create(
#     age=20,
#     phone_number='09127338239',
#     gender='M',
#     address='addre_1',
#     national_code='0029382748',
#     debt=debt_obj,
#     user=user_obj,
# )
# loan_obj = LoanModel.objects.create(
#     user=custom_user_obj,
#     status='C',
# )
# book_obj = Book.objects.create(
#     name='book_1',
#     description='desc_1',
#     translator='translator_1',
#     publishers=pub_obj,
#     user=custom_user_obj,
#     loan=loan_obj,
# )
# book_obj.category.add(category_obj)
# book_obj.author.add(author_obj)
# book_obj.save()
#
# bookmark_obj = BookmarkModel.objects.create(
#     user=custom_user_obj,
# )
# bookmark_obj.book.add(book_obj)
# bookmark_obj.save()
#
# comment_obj = CommentModel(
#     user=custom_user_obj,
#     book=book_obj,
#     title='comm_1',
#     content='content_1',
# )
# c_obj = CustomUserModel.objects.get(id=1)
########################

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