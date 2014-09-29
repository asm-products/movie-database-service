from os.path import join
from anee.settings import *

TEST_APPS=(
	'django_nose',
	'django_jasmine',
	'django_coverage',
	)
INSTALLED_APPS = INSTALLED_APPS + TEST_APPS

DATABASES = {
    'default' : {
      'ENGINE' : 'django_mongodb_engine',
      'NAME' : 'anee_tests'
   }
}

PASSWORD_HASHERS = (
	'django.contrib.auth.hashers.MD5PasswordHasher'
	)

TEST_RUNNER = 'anee.test_runner.NoseCoverageTestRunner'

COVERAGE_MODULE_EXCLUDES = [
'tests$', 'settings$', 'urls$', 'locale$',
'migrations', 'fixtures', 'admin$', 'django_extensions',
]
COVERAGE_MODULE_EXCLUDES += EXTERNAL_APPS
COVERAGE_REPORT_HTML_OUTPUT_DIR = os.path.join(__file__, '../../coverage')
