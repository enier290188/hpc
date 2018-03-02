from __future__ import unicode_literals
from django.core import management
import os


class Command(management.base.BaseCommand):
    help = 'Management utility to celery.'

    def handle(self, *args, **options):
        self.stdout.write('')
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('%s %s %s' % ('*' * 3, 'Management utility to celery.', '*' * 66))
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('')
        #
        os.system('sh /service_django/commands/celery.sh')
