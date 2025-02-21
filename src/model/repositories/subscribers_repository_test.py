from .subscribers_repository import SubscribersRepository
import pytest

@pytest.mark.skip("insert in BD")
def test_insert():
    subscriber_info = {
        "name":"meu nome",
        "email":"meu@email.com",
        "link":"",
        "evento_id" : 1
    }
    subs_repo = SubscribersRepository()
    subs_repo.insert(subscriber_info)
@pytest.mark.skip("select in BD")
def test_select_subscriber():
    email = "meu@email.com"
    evento_id = 1

    subs_repo = SubscribersRepository()
    resp = subs_repo.select_subscriber(email, evento_id)
    print(resp.nome)
