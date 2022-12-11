class BaseError(Exception):
    message = 'Unknown error.'


class NotEnoughSpaceError(BaseError):
    message = 'Not enough space.'


class UnknownProductError(BaseError):
    message = 'Unknown product.'


class NotEnoughProductError(BaseError):
    message = 'Not enough product.'


class InvalidRequestError(BaseError):
    message = 'Invalid request.'


class UnknownStorageError(BaseError):
    message = 'Unknown storage.'


class TooManyDifferentProductsError(BaseError):
    message = 'Too many different products.'
