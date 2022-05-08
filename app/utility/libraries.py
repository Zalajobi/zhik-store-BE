from imagekitio import ImageKit
import cloudinary
import os


def setup_imageKit():
    return ImageKit(private_key=os.getenv('IMAGEKIT_PRIVATE_KEY'), public_key=os.getenv('IMAGEKIT_PUBLIC_KEY'),
                    url_endpoint=os.getenv('IMAGEKIT_URL_ENDPOINT'))


def setup_cloudinary():
    return cloudinary.config(cloud_name=os.getenv('CLOUDINARY_NAME'), api_key=os.getenv('CLOUDINARY_KEY'),
                             api_secret=os.getenv('SECRET_KEY'))
