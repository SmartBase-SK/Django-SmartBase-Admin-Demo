import logging

from django.contrib import messages
from django.db.utils import ProgrammingError
from django.shortcuts import redirect
from django.utils.deprecation import MiddlewareMixin
from psycopg.errors import InsufficientPrivilege


class ReadOnlyModeMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        if isinstance(exception, (InsufficientPrivilege, ProgrammingError)):
            if request.path.startswith('/sb-admin/'):
                messages.warning(request, "Database is operating in readonly mode. Not possible to save any data.")
                logging.error(exception)
                return redirect(request.META.get('HTTP_REFERER', '/sb-admin/'))

        return None
