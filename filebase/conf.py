from django.conf import settings as settings
from django.core.files.storage import DefaultStorage


def _get_or_default(local_setting_name, setting_default):
    global_setting_name = 'FILEBASE_{}'.format(local_setting_name)
    setting_value = getattr(
        settings,
        global_setting_name,
        setting_default,
    )
    globals()[local_setting_name] = setting_value
    if not getattr(settings, global_setting_name, None):
        setattr(settings, global_setting_name, setting_value)


# where to store files
_get_or_default('FILE_STORAGE', DefaultStorage())


# where to store thumbnails
_get_or_default('THUMBNAIL_STORAGE', DefaultStorage())


# upload to (within storage). can be a callable
_get_or_default('UPLOAD_TO', 'files')


# put thumbnails in (within its storage). can be a callable
_get_or_default('THUMBNAIL_TO', 'thumbs')


# thumb sizes
_get_or_default(
    'IMAGE_SIZES',
    {
        'LIST': (100, 70),
        'FIELD': (220, 150),
    }
)

# just because?
_get_or_default('STATIC_URL', settings.STATIC_URL + "filebase/")
