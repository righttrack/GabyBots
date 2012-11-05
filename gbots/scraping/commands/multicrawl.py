from gbots.util import loggers
from optparse import Values
from scrapy.commands import crawl
from scrapy.exceptions import UsageError
from gbots.scraping.models import WebSource

__author__ = 'jeffmay'

logger = loggers.getLogger(__name__)

class Command(crawl.Command):

    def run(self, args, opts):
        if hasattr(opts, "spargs"):
            spargs = opts.spargs
        else:
            spargs = {}
        # Use id argument over names argument
        if "id" in spargs:
            if "names" in spargs:
                raise UsageError("Cannot use -a arguments 'id' and 'names' together.", print_help=True)
            super(Command, self).run(args, opts)
        else:
            # Get a list of web source names from the command line
            aliases = []
            if "alias" in spargs:
                aliases = spargs["alias"].split()
            if len(aliases) > 0:
                sources = WebSource.objects.filter(alias__in=aliases)
            else:
                sources = WebSource.objects.all()
            # Process sources for required id argument
            if len(sources) == 0:
                raise UsageError("Could not find any sources matching alias(es): %s" % ', '.join(aliases))
            logger.info("Found sources for aliases: %s" % ', '.join(aliases))
            for source in sources:
                # Run the scraper on the sources
                eachopts = Values(vars(opts))
                source_opts = dict(id=source.id)
                eachopts.spargs.update(source_opts)
                super(Command, self).run(args, eachopts)
