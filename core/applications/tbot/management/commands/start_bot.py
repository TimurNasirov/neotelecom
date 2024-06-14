from django.core.management.base import BaseCommand

from applications.tbot.bot_core import t_bot


class Command(BaseCommand):
    help = 'Creating telegram log polling listener bot.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--category',
            action='store_true',
            dest='category',
            help='Стягивает и заливает все категории перед загрузкой ффида',
        )

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS(f'Starting bot!'))
        try:
            t_bot.polling(none_stop=True)
        except KeyboardInterrupt:
            self.stdout.write(self.style.SUCCESS('Stop bot!'))
            return
        except Exception as e:
            self.stdout.write(self.style.ERROR(f'Error on bot work :: {e}'))
        self.stdout.write(self.style.SUCCESS('Stop bot!'))
