from dishka import Provider, Scope, make_container, provide

from src.core.bank_operation import BankService, IBankOperationRepository
from src.core.user import IUserRepository, UserService
from src.data_access.bank_repository import BankOperationRepository
from src.data_access.user_repository import UserRepository


class ServiceProvider(Provider):
    scope = Scope.REQUEST

    @provide
    def provide_user_repo(self) -> IUserRepository:
        return UserRepository()

    @provide
    def provide_user_service(self, user_repo: IUserRepository) -> UserService:
        return UserService(user_repo)

    @provide
    def provide_bank_repo(self) -> IBankOperationRepository:
        return BankOperationRepository()

    @provide
    def provide_bank_service(self, bank_repo: IBankOperationRepository) -> BankService:
        return BankService(bank_repo)


container_factory = make_container(ServiceProvider())
