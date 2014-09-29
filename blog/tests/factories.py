import factory

from blog.models import Author,Comment,Post
from anee.tests.projects import UserFactory

class AuthorFactory(factory.Factory):
	FACTORY_FOR = Author
	user = factory.SubFactory(UserFactory)
	message = "A message"