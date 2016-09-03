# -*- coding: utf-8 -*-
"""Base command for search-related management commands."""
import logging

from django.core.management.base import BaseCommand

from elasticsearch.exceptions import TransportError

logger = logging.getLogger(__name__)


class BaseSearchCommand(BaseCommand):

    """Base class for commands that interact with the search index."""

    description = "Base search command."

    def add_arguments(self, parser):
        """Add default base options of --noinput and indexes."""
        parser.add_argument(
            '--noinput',
            action='store_false',
            dest='interactive',
            default=True,
            help='Do no display user prompts - may affect data.'
        )
        parser.add_argument(
            'indexes',
            nargs='*',
            help="Names of indexes on which to run the command."
        )

    def do_index_command(self, index, interactive):
        """Run a command against a named index."""
        raise NotImplementedError()

    def handle(self, *args, **options):
        """Run do_index_command on each specified index and log the output."""
        for index in options.pop('indexes'):
            data = {}
            try:
                print "calling do_index_command", index, options
                data = self.do_index_command(index, **options)
            except TransportError as ex:
                logger.warn("ElasticSearch threw an error: %s", ex)
                data = {
                    "index": index,
                    "status": ex.status_code,
                    "reason": ex.info['error']['reason']
                }
            finally:
                logger.info(data)