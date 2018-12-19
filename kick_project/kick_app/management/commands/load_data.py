import csv
from django.core.management import BaseCommand
from kick_app.models import kick_campaign

class Command(BaseCommand):
    help = 'Load a questions csv file into the database'

    def add_arguments(self, parser):
        parser.add_argument('--path', type=str)

    def handle(self, *args, **kwargs):
        path = kwargs['path']
        kick_campaign.objects.all().delete()
        with open(path, 'rt') as f:
            reader = csv.reader(f, dialect='excel')
            rowCount = 0
            for row in reader:
                if rowCount != 0:
                    campaign = kick_campaign.objects.create(
                        backers_count=row[0],
                        blurb=row[1],
                        category=row[2],
                    )
                rowCount += 1
