class Application(object):
    name = None

    def __init__(self, app_name=None, **kwargs):
        self.app_name = app_name
        for key, value in kwargs.items():
            setattr(self, key, value)

    def get_urls(self):
        """
        Return the url patterns for this app.
        """
        return []

    @property
    def urls(self):
        # We set the application and instance namespace here
        return self.get_urls(), self.app_name, self.name
        