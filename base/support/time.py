import time


class Time(object):
    @staticmethod
    def current():
        return time.time()

    @staticmethod
    def sleep(seconds):
        time.sleep(seconds)

    @staticmethod
    def format(time, time_format_string='%a, %d-%B-%y %H:%M'):
        return Time.format_time(time, time_format_string, True)

    @staticmethod
    def to_time(time_string, should_format=False, time_format_string='%a, %d-%B-%y %H:%M', reference=time.time()):

        operator, value, figure = Time.split(time_string)

        calculated_time = Time.merge_time(reference, Time.get_callable(figure)() * value, operator)

        return Time.format_time(calculated_time, time_format_string, should_format)

    @staticmethod
    def get_operator(time_string):
        if '-' in time_string:
            return '-'

        if '+' in time_string:
            return '+'

        raise Exception("This {} format is not supported".format(time_string))

    @staticmethod
    def get_value(user_format):
        user_format = user_format.split(' ')

        if len(user_format) > 1:
            return int(user_format[1])

        return None

    @staticmethod
    def format_time(calculated_time, time_format, should_format):

        if calculated_time is None:
            raise Exception('Calculated Time is None')

        if not should_format:
            return int(calculated_time)

        formatted_time = None

        try:
            formatted_time = time.strftime(time_format, time.localtime(calculated_time))
        except Exception as e:
            raise e

        return formatted_time

    @staticmethod
    def merge_time(reference, calculated, operator):

        if operator is '+':
            return reference + calculated
        elif operator is '-':
            return reference - calculated

        raise Exception("Operator {} is not supported".format(operator))

    @staticmethod
    def split(time_string):

        operator = Time.get_operator(time_string)
        value = Time.get_value(time_string)
        figure = Time.get_figure(time_string)

        Time.validate(operator, value, figure)

        return operator, value, figure

    @staticmethod
    def get_figure(time_string):

        if 'minutes' in time_string:
            return 'minutes'

        if 'hours' in time_string:
            return 'hours'

        if 'days' in time_string:
            return 'days'

        if 'weeks' in time_string:
            return 'weeks'

        if 'months' in time_string:
            return 'months'

        if 'years' in time_string:
            return 'years'

        raise Exception("Tthis {} format is not supported.".format(time_string))

    @staticmethod
    def get_minutes_span():
        return 60

    @staticmethod
    def get_hours_span():
        return Time.get_minutes_span() * 60

    @staticmethod
    def get_days_span():
        return Time.get_hours_span() * 24

    @staticmethod
    def get_weeks_span():
        return Time.get_days_span() * 7

    @staticmethod
    def get_months_span():
        return Time.get_days_span() * 30

    @staticmethod
    def get_years_span():
        return Time.get_days_span() * 365

    @staticmethod
    def validate(operator, value, figure):
        if operator not in ['-', '+']:
            raise Exception("Invalid Operator {}".format(operator))

        if value is None:
            raise Exception("Value is None")

        if figure not in ['minutes', 'hours', 'days', 'weeks', 'months', 'years']:
            raise Exception("Invalid time span {} provided.".format(figure))

    @staticmethod
    def get_callable(figure):
        return getattr(Time, "get_{}_span".format(figure))
