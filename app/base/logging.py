import apache_log_parser

from pythonjsonlogger.jsonlogger import JsonFormatter
from pythonjsonlogger.jsonlogger import merge_record_extra


class CustomJSONFormatter(JsonFormatter):
    # These use mixed camel case and underscores for some reason, reminds me of
    # PHP's standard lib
    # https://docs.python.org/3/library/logging.html#logrecord-attributes
    attributes = (
        'levelname', 'message', 'processName', 'name', 'asctime'
    )

    log_line_fmt = '%h %l %u %t "%r" %>s %b "%{Referer}i" "%{User-Agent}i"'

    required_access_log_fields = (
        'remote_host',
        'remote_logname',
        'remote_user',
        'request_first_line',
        'request_header_referer',
        'request_header_user_agent',
        'request_header_user_agent__browser__family',
        'request_header_user_agent__browser__version_string',
        'request_header_user_agent__is_mobile',
        'request_header_user_agent__os__family',
        'request_header_user_agent__os__version_string',
        'request_http_ver',
        'request_method',
        'request_url',
        'request_url_fragment',
        'request_url_hostname',
        'request_url_netloc',
        'request_url_path',
        'request_url_port',
        'request_url_query',
        'request_url_query_simple_dict',
        'request_url_scheme',
        'response_bytes_clf',
        'status',
        'time_received_utc_isoformat',
    )

    def _parse_access_log(self, log_line):
        line_parser = apache_log_parser.make_parser(self.log_line_fmt)
        try:
            access_log_dict = line_parser(log_line)
        except apache_log_parser.LineDoesntMatchException:
            # Failed because format is not expected or incorrect
            access_log_dict = {}

        parsed_access_log_dict = {}
        for field in self.required_access_log_fields:
            if access_log_dict.get(field):
                parsed_access_log_dict[field] = access_log_dict[field]

        return parsed_access_log_dict

    def add_fields(self, log_record, record, message_dict):
        """
        Override this method to implement custom logic for adding fields.
        """
        for field in self.attributes:
            log_record[field] = record.__dict__.get(field)

        access_log_dict = self._parse_access_log(
            record.__dict__.get('message', '')
        )

        log_record.update(message_dict)
        log_record.update(access_log_dict)
        merge_record_extra(record, log_record, reserved=self._skip_fields)
