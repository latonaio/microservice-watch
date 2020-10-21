from aion.logger import lprint


class TemplateMatchingSummaryWatch():
    def __init__(self, key):
        '''
        Args:
            key (str): 'vehicle' or 'trigger'
        '''
        self.key = key

    def print_template_matching(self, metadata):
        _metadata = metadata[self.key]
        if _metadata['status']:
            if self.key == 'vehicle':
                lprint(f"{self.key}: {_metadata['name']}")
            elif self.key == 'trigger':
                lprint('trigger')
                lprint(f"vehicle: {_metadata['values'][0]['vehicle_name']}")

            for t in _metadata['values']:
                lprint(f"template_id: {t['template_id']}, matching_rate: {t['matching_rate']}")
        else:
            lprint("no detect...")

        end = metadata['end']
        if end['status']:
            lprint(f"End")
            for t in end['values']:
                lprint(f"template_id: {t['template_id']}, matching_rate: {t['matching_rate']}")