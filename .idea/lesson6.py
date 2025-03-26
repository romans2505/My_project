from pip._internal import resolution


class Image:
    def __init__(self, title, resolution , extension):
        self.title = title
        self.resolution = resolution
        self.extention = extension

    def resize(self, new_resolution):
        self.resolution = new_resolution

my_image = Image('Tim', '1920 x 1080', '.gpeg')
print(my_image.title, my_image.resolution, my_image.extention)

my_image.resize('3840 x 2160')

print(my_image.title, my_image.resolution, my_image.extention)

