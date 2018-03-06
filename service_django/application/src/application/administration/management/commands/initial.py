from __future__ import unicode_literals
from src.application.help import models as models___application___help
from src.application.security import models as models___application___security
from django_celery_beat import models as models___django_celery_beat
from django.conf import settings
from django.core import management
import os
import shutil


class Command(management.base.BaseCommand):
    help = 'Management utility to initial the application.'

    def handle(self, *args, **options):
        self.stdout.write('')
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('%s %s %s' % ('*' * 3, 'Management utility to initial the application.', '*' * 49))
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Running makemigrations.....', '+' * 68))
        self.stdout.write('%s' % ('+' * 100))
        management.call_command('makemigrations', '--no-input')
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Running migrate.....', '+' * 75))
        self.stdout.write('%s' % ('+' * 100))
        management.call_command('migrate', '--no-input')
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Running collectstatic.....', '+' * 69))
        self.stdout.write('%s' % ('+' * 100))
        management.call_command('collectstatic', '--no-input')
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Running compilemessages.....', '+' * 67))
        self.stdout.write('%s' % ('+' * 100))
        management.call_command('compilemessages')
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Deleting all entered data.....', '+' * 65))
        self.stdout.write('%s' % ('+' * 100))
        management.call_command('flush', '--no-input')
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Deleting all into media root.....', '+' * 62))
        self.stdout.write('%s' % ('+' * 100))
        folder___media_root = settings.MEDIA_ROOT
        if os.path.exists(folder___media_root):
            list___dir = [os.path.join(folder___media_root, x) for x in os.listdir(folder___media_root)]
            files = filter(lambda c: os.path.isfile(c), list___dir)
            [os.remove(x) for x in files]
            dirs = filter(lambda c: os.path.isdir(c), list___dir)
            [shutil.rmtree(x) for x in dirs]
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Creating localuser \"administrator\".....', '+' * 56))
        self.stdout.write('%s' % ('+' * 100))
        instance___localuser = models___application___security.LOCALUser(
            is_active=True,
            identifier='administrator',
            email='administrator@local.cu',
            password='',
            is_superuser=True
        )
        instance___localuser.save()
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Creating permissions of the application.....', '+' * 51))
        self.stdout.write('%s' % ('+' * 100))
        list_dict___permission = [
            {'identifier': 'application_security_localuser_list', 'name': 'security localuser ___list___'},
            {'identifier': 'application_security_localuser_create', 'name': 'security localuser ___create___'},
            {'identifier': 'application_security_localuser_detail', 'name': 'security localuser ___detail___'},
            {'identifier': 'application_security_localuser_update', 'name': 'security localuser ___update___'},
            {'identifier': 'application_security_localuser_delete', 'name': 'security localuser ___delete___'},
            {'identifier': 'application_security_localuserrequest_list', 'name': 'security localuser request ___list___'},
            {'identifier': 'application_security_localuserrequest_detail', 'name': 'security localuser request ___detail___'},
            {'identifier': 'application_security_localuserrequest_approve', 'name': 'security localuser request ___approve___'},
            {'identifier': 'application_security_localuserrequest_disapprove', 'name': 'security localuser request ___disapprove___'},
            {'identifier': 'application_security_ldapuser_list', 'name': 'security ldapuser ___list___'},
            {'identifier': 'application_security_ldapuser_create', 'name': 'security ldapuser ___create___'},
            {'identifier': 'application_security_ldapuser_detail', 'name': 'security ldapuser ___detail___'},
            {'identifier': 'application_security_ldapuser_update', 'name': 'security ldapuser ___update___'},
            {'identifier': 'application_security_ldapuser_delete', 'name': 'security ldapuser ___delete___'},
            {'identifier': 'application_security_ldapuserrequest_list', 'name': 'security ldapuser request ___list___'},
            {'identifier': 'application_security_ldapuserrequest_detail', 'name': 'security ldapuser request ___detail___'},
            {'identifier': 'application_security_ldapuserrequest_approve', 'name': 'security ldapuser request ___approve___'},
            {'identifier': 'application_security_ldapuserrequest_disapprove', 'name': 'security ldapuser request ___disapprove___'},
            {'identifier': 'application_security_ldapuserimported_list', 'name': 'security ldapuser imported ___list___'},
            {'identifier': 'application_security_ldapuserimported_detail', 'name': 'security ldapuser imported ___detail___'},
            {'identifier': 'application_security_ldapuserimported_update', 'name': 'security ldapuser imported ___update___'},
            {'identifier': 'application_security_ldapuserimported_delete', 'name': 'security ldapuser imported ___delete___'},
            {'identifier': 'application_security_group_list', 'name': 'security group ___list___'},
            {'identifier': 'application_security_group_create', 'name': 'security group ___create___'},
            {'identifier': 'application_security_group_detail', 'name': 'security group ___detail___'},
            {'identifier': 'application_security_group_update', 'name': 'security group ___update___'},
            {'identifier': 'application_security_group_delete', 'name': 'security group ___delete___'},
            {'identifier': 'application_security_permission_list', 'name': 'security permission ___list___'},
            {'identifier': 'application_security_permission_detail', 'name': 'security permission ___detail___'},
            {'identifier': 'application_security_permission_update', 'name': 'security permission ___update___'},
            {'identifier': 'application_help_document_list', 'name': 'help document ___list___'},
            {'identifier': 'application_help_document_create', 'name': 'help document ___create___'},
            {'identifier': 'application_help_document_detail', 'name': 'help document ___detail___'},
            {'identifier': 'application_help_document_update', 'name': 'help document ___update___'},
            {'identifier': 'application_help_document_delete', 'name': 'help document ___delete___'},
        ]
        for x in list_dict___permission:
            instance___permission = models___application___security.Permission(
                is_active=True,
                identifier=x['identifier'],
                name=x['name']
            )
            instance___permission.save()
        self.stdout.write('')
        #
        self.stdout.write('%s' % ('+' * 100))
        self.stdout.write('%s %s %s' % ('+' * 3, 'Celery.....', '+' * 84))
        self.stdout.write('%s' % ('+' * 100))
        # instervalschedule, boolean___created = models___django_celery_beat.IntervalSchedule.objects.get_or_create(
        #     every=10,
        #     period=models___django_celery_beat.IntervalSchedule.SECONDS,
        # )
        crontabschedule, boolean___created = models___django_celery_beat.CrontabSchedule.objects.get_or_create(
            minute='*',  # */1
            hour='0,8,9,10,11,12,13,14,15,16,17,18',  # 0,12 # midnight and noon
            day_of_week='*',
            day_of_month='*',
            month_of_year='*',
        )
        models___django_celery_beat.PeriodicTask.objects.create(
            # interval=instervalschedule,
            crontab=crontabschedule,
            name='PeriodicTask 001',
            task='src.application.security.tasks.___task___application___security___ldap___synchronize___',
        )
        self.stdout.write('')
        # #
        # self.stdout.write('%s' % ('+' * 100))
        # self.stdout.write('%s %s %s' % ('+' * 3, 'Optional.....', '+' * 82))
        # self.stdout.write('%s' % ('+' * 100))
        # #
        # int___count = 1
        # while int___count <= 30:
        #     string___count = ''
        #     if 1 <= int___count < 10:
        #         string___count = '00%s' % (int___count,)
        #     elif 10 <= int___count < 100:
        #         string___count = '0%s' % (int___count,)
        #     elif 100 <= int___count < 1000:
        #         string___count = '%s' % (int___count,)
        #     #
        #     instance___localuser = models___application___security.LOCALUser(
        #         is_active=True,
        #         identifier='enier%s' % (string___count,),
        #         email='enier%s@local.cu' % (string___count,),
        #         first_name='Enier%s' % (string___count,),
        #         last_name='Ramos Garcia',
        #         password='',
        #         detail='Detail'
        #     )
        #     instance___localuser.save()
        #     #
        #     instance___ldapuser = models___application___security.LDAPUser(
        #         is_active=True,
        #         identifier='enier%s' % (string___count,),
        #         email='enier%s@ldap.cu' % (string___count,),
        #         first_name='Enier%s' % (string___count,),
        #         last_name='Ramos Garcia',
        #         password='',
        #         detail='Detail'
        #     )
        #     instance___ldapuser.save()
        #     #
        #     int___count += 1
        # #
        # int___count = 1
        # while int___count <= 30:
        #     string___count = ''
        #     if 1 <= int___count < 10:
        #         string___count = '00%s' % (int___count,)
        #     elif 10 <= int___count < 100:
        #         string___count = '0%s' % (int___count,)
        #     elif 100 <= int___count < 1000:
        #         string___count = '%s' % (int___count,)
        #     instance___document = models___application___help.Document(
        #         is_active=True,
        #         title_en='title%s-en' % (string___count,),
        #         title_es='title%s-es' % (string___count,),
        #         content_en='content%s-en' % (string___count,),
        #         content_es='content%s-es' % (string___count,),
        #     )
        #     instance___document.save()
        #     int___count += 1
        # #
        self.stdout.write('')
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('%s %s %s' % ('*' * 3, 'Congratulations, the application is in its initial state.', '*' * 38))
        self.stdout.write('%s' % ('*' * 100))
        self.stdout.write('')
        #
        management.call_command('celery')
