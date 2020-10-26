from django_oauth_usp.accounts.models import UserModel
from ..models import Solicitation


def make_user_data(**kwargs: dict) -> dict:
    default = dict(login='778899', main_email='main@test.com',
                   password='92874', name='Marc Stold Further',
                   user_type='I ', is_staff=False, is_active=True)
    user_data = dict(default, **kwargs)

    return user_data


def make_solicitation_data(requester: int, answerable: int,
                           **kwargs: dict) -> dict:
    default = dict(requester=requester, phone='9999999', bond='ic',
                   departament='ast', answerable=answerable,
                   status='open', slug='lkjasdlkajsd')

    solicitation_data = dict(default, **kwargs)

    return solicitation_data


def make_user(user_data: dict) -> UserModel:
    return UserModel.objects.create(**user_data)


def make_solicitation(solicitation_data: dict) -> Solicitation:
    return Solicitation.objects.create(**solicitation_data)
