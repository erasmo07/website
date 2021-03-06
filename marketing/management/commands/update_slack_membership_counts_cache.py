from django.core.management.base import BaseCommand

from marketing.tasks import update_slack_membership_cache


class Command(BaseCommand):
    help = 'Force an update of the slack membership counts'

    def handle(self, *args, **options):
        update_slack_membership_cache()
